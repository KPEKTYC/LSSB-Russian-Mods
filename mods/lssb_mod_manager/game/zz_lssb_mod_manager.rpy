# In-game manager for the installed LSSB mods. No external application.
init 1005 python in lssb_mm:
    import renpy as engine
    import types as _types
    from store import config, renpy as api
    _constant = True
    _core_module = _types.ModuleType('lssb_mod_manager_core')
    exec(compile('"""Small filesystem core for the in-game LSSB mod manager.\n\nOnly catalogued or signed first-party mod archives can be renamed.\nPlans bind exact bytes even when later releases are recognised automatically.\nA surviving journal deliberately requires manual recovery.\nThis module does not import Ren\'Py or inspect game saves.\n"""\nimport datetime\nimport base64\nimport hashlib\nimport hmac\nimport json\nimport os\nfrom pathlib import Path\nimport re\nimport stat\nimport struct\nimport uuid\n\n\nRELEASE_MAGIC = b"\\nLSSB-RELEASE-V1\\n"\nRELEASE_DOMAIN = b"LSSB localization release v1\\0"\nMOD_RELEASE_DOMAIN = b"LSSB first-party mod release v2\\0"\nRELEASE_COMPONENTS = {\n    "localization_ru": "zzzzzz_lssb_localization_ru.rpa",\n    "visual_quality": "zzzzz_lssb_visual_quality.rpa",\n    "startup_fast": "zzzzzzz_lssb_startup_fast.rpa",\n}\nRELEASE_MAX_JSON = 8192\nRELEASE_KEY_ID = "lssb-localization-20261021"\n# Public verification key only. The private signing key is never distributed.\nRELEASE_KEYS = {RELEASE_KEY_ID: (int(\n    "d61f1e84aff38380042a973917df3101c1ff7d33401df3cfb47ad0a088ccc7d994309503b91cee4a0407c1a96d125cd3bddd9b116744bf19d3403f42ff003e69373d87af82ecf90c8dd8f070f891a0245f52a22fab628ae7136871a7a54be5a6260571ca98ca25fb4b1be3e6a0ac18de88a2f379997b32b625f53ed94c7b76575b1888c9ab51d9edf93c4494b23762dc504997dd891d011eb40b7cee969897a6080ba665b54312e43a5bd611698187ad4fa6452222fdb5741926422bd0765183a1c182e5c59543b2e1343fb7db9ed771cac1f43109853dbc386da7954fa568a4a8f220feda3bcc6b44c098c3eb625a0a17a8420037b42b35e0c68c882a96a5a0f45c5b9bde11defc8172fdd77433a78e616d54e48778714c3564935554413e5bf99c812a71302c8d7f7e22349caae13f4b124ec9cac30377118b62b555f5cef6188fd799f78491a5cbff45540a723f0906d00a14d9afae8265dafd64325b992a3df98c7590c1ff18f9ef73ed7efd9be7264262897a692e7787f0023120490b1b",\n    16), 65537)}\n\n\ndef release_message(payload):\n    domain = MOD_RELEASE_DOMAIN if payload.get("schema") == 2 else RELEASE_DOMAIN\n    return domain + json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")\n\n\ndef _unique_release_pairs(pairs):\n    result = {}\n    for key, value in pairs:\n        if key in result:\n            raise ValueError("duplicate release key")\n        result[key] = value\n    return result\n\n\ndef _verify_release_signature(message, signature, key_id):\n    """RSA-PSS/SHA-256, fixed 32-byte salt; RFC 8017 section 9.1.2.\n\n    Verification uses only public operations and the standard library so the\n    game does not need a cryptography package. Signing uses cryptography.\n    """\n    key = RELEASE_KEYS.get(key_id)\n    if key is None:\n        return False\n    modulus, exponent = key\n    size = (modulus.bit_length() + 7) // 8\n    if len(signature) != size or int.from_bytes(signature, "big") >= modulus:\n        return False\n    bits = modulus.bit_length() - 1\n    length = (bits + 7) // 8\n    decoded = pow(int.from_bytes(signature, "big"), exponent, modulus).to_bytes(size, "big")\n    if any(decoded[:size-length]):\n        return False\n    encoded = decoded[size-length:]\n    if length < 66 or encoded[-1] != 0xbc:\n        return False\n    masked, digest = encoded[:-33], encoded[-33:-1]\n    unused = 8 * length - bits\n    if masked[0] & (0xff << (8-unused) if unused else 0):\n        return False\n    mask = b"".join(hashlib.sha256(digest + struct.pack(">I", counter)).digest()\n                    for counter in range((len(masked) + 31) // 32))[:len(masked)]\n    data = bytearray(a ^ b for a, b in zip(masked, mask))\n    data[0] &= 0xff >> unused\n    padding = length - 66\n    if any(data[:padding]) or data[padding] != 1:\n        return False\n    expected = hashlib.sha256(b"\\0" * 8 + hashlib.sha256(message).digest() + data[-32:]).digest()\n    return hmac.compare_digest(digest, expected)\n\n\ndef read_release_footer(stream, file_size):\n    """Read bounded JSON, never the RPA\'s pickle index or executable payload.\n\n    Returns None for a legacy archive. A present but invalid footer raises.\n    The caller hashes the signed prefix using this same opened file handle.\n    """\n    tail_size = len(RELEASE_MAGIC) + 4\n    if file_size < tail_size + 34:\n        return None\n    stream.seek(file_size - tail_size)\n    tail = stream.read(tail_size)\n    if not tail.endswith(RELEASE_MAGIC):\n        return None\n    size = struct.unpack(">I", tail[:4])[0]\n    prefix_size = file_size - tail_size - size\n    if not 0 < size <= RELEASE_MAX_JSON or prefix_size < 34:\n        raise ValueError("invalid release size")\n    stream.seek(prefix_size)\n    envelope = json.loads(stream.read(size).decode("utf-8"), object_pairs_hook=_unique_release_pairs)\n    if not isinstance(envelope, dict) or set(envelope) != {"key_id", "payload", "signature"}:\n        raise ValueError("invalid release envelope")\n    payload = envelope["payload"]\n    fields = {"schema", "owner", "id", "filename", "version", "archive_size", "archive_sha256"}\n    if (not isinstance(payload, dict) or set(payload) != fields\n            or type(payload["schema"]) is not int or payload["schema"] not in (1, 2)\n            or payload["owner"] != "lssb-russian-mods"\n            or not isinstance(payload["id"], str)\n            or payload["id"] not in RELEASE_COMPONENTS\n            or (payload["schema"] == 1) != (payload["id"] == "localization_ru")\n            or payload["filename"] != RELEASE_COMPONENTS[payload["id"]]\n            or not isinstance(payload["version"], str)\n            or not re.fullmatch(r"[0-9]{1,5}\\.[0-9]{1,5}\\.[0-9]{1,5}(?:-[A-Za-z0-9][A-Za-z0-9.-]{0,31})?", payload["version"])\n            or type(payload["archive_size"]) is not int or payload["archive_size"] != prefix_size\n            or not isinstance(payload["archive_sha256"], str)\n            or not re.fullmatch(r"[a-f0-9]{64}", payload["archive_sha256"])\n            or not isinstance(envelope["key_id"], str) or not isinstance(envelope["signature"], str)):\n        raise ValueError("invalid release identity")\n    signature = base64.b64decode(envelope["signature"], validate=True)\n    if not _verify_release_signature(release_message(payload), signature, envelope["key_id"]):\n        raise ValueError("invalid release signature")\n    return payload\n\n\nclass ManagerError(Exception):\n    def __init__(self, code, message):\n        self.code = code\n        super().__init__(message)\n\n\nclass ManagerCore:\n    OWNER = "lssb-in-game-mod-manager"\n    SCHEMA = 1\n    DATA_DIR = "lssb_mod_manager_data"\n    MAX_JSON = 131072\n    _HEADER = re.compile(br"RPA-3\\.0 [0-9a-fA-F]{16} [0-9a-fA-F]{8}\\n")\n\n    def __init__(self, game_dir, catalog):\n        self.game_dir = Path(os.path.abspath(os.fspath(game_dir)))\n        self.data_dir = self.game_dir / self.DATA_DIR\n        self.catalog = []\n        self.by_id = {}\n        self._hash_cache = {}\n        self.status_error = None\n        seen_names = set()\n        for item in catalog:\n            item = dict(item)\n            key, name, digest = item.get("id"), item.get("filename"), item.get("sha256")\n            if (not isinstance(key, str) or not re.fullmatch(r"[a-z0-9_]{1,64}", key)\n                    or key in self.by_id or not isinstance(name, str)\n                    or not re.fullmatch(r"[A-Za-z0-9_-]+\\.rpa", name)\n                    or name.lower() in seen_names or not isinstance(digest, str)\n                    or not re.fullmatch(r"[a-f0-9]{64}", digest)):\n                raise ManagerError("catalog", "Неверный каталог модов.")\n            seen_names.add(name.lower())\n            self.catalog.append(item)\n            self.by_id[key] = item\n        self._check_directory(self.game_dir)\n        self._builtin_catalog = list(self.catalog)\n        self._refresh_external_mods()\n\n    def _refresh_external_mods(self):\n        """Discover opt-in author metadata; never execute an archive to identify it."""\n        self._check_directory(self.game_dir)\n        paths = sorted(self.game_dir.glob("*.lssb-mod.json"))\n        if len(paths) > 64:\n            raise ManagerError("metadata", "Слишком много описаний сторонних модов (максимум 64).")\n        additions = []\n        names = {item["filename"].lower() for item in self._builtin_catalog}\n        for path in paths:\n            try:\n                before = self._file_info(path)\n                if before is None or not 0 < before.st_size <= RELEASE_MAX_JSON:\n                    raise ValueError("size")\n                flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)\n                with os.fdopen(os.open(path, flags), "rb") as stream:\n                    if self._identity(os.fstat(stream.fileno())) != self._identity(before):\n                        raise ValueError("changed")\n                    item = json.loads(stream.read(RELEASE_MAX_JSON + 1).decode("utf-8"),\n                                      object_pairs_hook=_unique_release_pairs)\n                    if self._identity(os.fstat(stream.fileno())) != self._identity(before):\n                        raise ValueError("changed")\n                after = self._file_info(path)\n                if after is None or self._identity(after) != self._identity(before):\n                    raise ValueError("changed")\n                if (not isinstance(item, dict) or set(item) != {\n                        "schema", "id", "filename", "name", "description", "version", "sha256"}\n                        or type(item["schema"]) is not int or item["schema"] != 1\n                        or not isinstance(item["id"], str)\n                        or not re.fullmatch(r"[a-z0-9_]{1,48}", item["id"])\n                        or item["filename"] != "zz_mod_" + item["id"] + ".rpa"\n                        or path.name != "zz_mod_" + item["id"] + ".lssb-mod.json"\n                        or item["filename"].lower() in names\n                        or "external_" + item["id"] in {row["id"] for row in self._builtin_catalog}\n                        or not isinstance(item["version"], str)\n                        or not re.fullmatch(r"[0-9]{1,5}\\.[0-9]{1,5}\\.[0-9]{1,5}(?:-[A-Za-z0-9][A-Za-z0-9.-]{0,31})?", item["version"])\n                        or not isinstance(item["sha256"], str)\n                        or not re.fullmatch(r"[a-f0-9]{64}", item["sha256"])):\n                    raise ValueError("identity")\n                for field, limit in (("name", 64), ("description", 160)):\n                    text = item[field]\n                    if (not isinstance(text, str) or not 0 < len(text) <= limit\n                            or any(ord(c) < 32 or c in "{}[]" for c in text)):\n                        raise ValueError("display text")\n                names.add(item["filename"].lower())\n                additions.append(dict(item, id="external_" + item["id"], external=True))\n            except (OSError, ValueError, TypeError, UnicodeError, RecursionError, ManagerError):\n                raise ManagerError("metadata", "Описание стороннего мода повреждено или недоступно: " + path.name) from None\n        self.catalog = self._builtin_catalog + additions\n        self.by_id = {item["id"]: item for item in self.catalog}\n\n    @staticmethod\n    def _is_reparse(info):\n        return stat.S_ISLNK(info.st_mode) or bool(\n            getattr(info, "st_file_attributes", 0) & 0x400)\n\n    @staticmethod\n    def _identity(info):\n        return (info.st_size, info.st_mtime_ns, info.st_dev, info.st_ino)\n\n    def _check_directory(self, path):\n        # lstat every component: resolve() would conceal a junction/symlink.\n        for part in reversed((path,) + tuple(path.parents)):\n            try:\n                info = part.lstat()\n            except OSError:\n                raise ManagerError("directory", "Папка игры или менеджера недоступна.") from None\n            if self._is_reparse(info) or not stat.S_ISDIR(info.st_mode):\n                raise ManagerError("unsafe_path", "Путь проходит через ссылку или неподходящую папку.")\n\n    def _file_info(self, path):\n        self._check_directory(path.parent)\n        try:\n            info = path.lstat()\n        except FileNotFoundError:\n            return None\n        except OSError:\n            raise ManagerError("file", "Не удалось проверить файл.") from None\n        if self._is_reparse(info) or not stat.S_ISREG(info.st_mode):\n            raise ManagerError("unsafe_file", "Обнаружена ссылка или файл неподходящего типа.")\n        return info\n\n    def _fingerprint(self, path, fresh=False):\n        before = self._file_info(path)\n        if before is None:\n            return None\n        identity = self._identity(before)\n        cached = self._hash_cache.get(str(path))\n        if not fresh and cached and cached[0] == identity:\n            return cached[1]\n        try:\n            flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)\n            with os.fdopen(os.open(path, flags), "rb") as stream:\n                if self._identity(os.fstat(stream.fileno())) != identity:\n                    raise ManagerError("changed", "Файл изменился во время проверки.")\n                release, release_error = None, False\n                try:\n                    release = read_release_footer(stream, before.st_size)\n                except (ValueError, UnicodeError, TypeError, OverflowError, RecursionError, struct.error):\n                    release_error = True\n                stream.seek(0)\n                header = stream.read(34)\n                valid_header = bool(self._HEADER.fullmatch(header))\n                if valid_header:\n                    valid_header = 34 <= int(header[8:24], 16) < (release["archive_size"] if release else before.st_size)\n                hasher = hashlib.sha256(header)\n                # The signed archive is a prefix of the complete file. Copy the\n                # SHA state exactly at its boundary instead of hashing it twice.\n                prefix_end = release["archive_size"] if release else None\n                position = len(header)\n                prefix_digest = hasher.hexdigest() if prefix_end == position else None\n                for chunk in iter(lambda: stream.read(1024 * 1024), b""):\n                    if prefix_end is not None and position < prefix_end <= position + len(chunk):\n                        split = prefix_end - position\n                        hasher.update(chunk[:split])\n                        prefix_digest = hasher.copy().hexdigest()\n                        hasher.update(chunk[split:])\n                    else:\n                        hasher.update(chunk)\n                    position += len(chunk)\n                if release and prefix_digest != release["archive_sha256"]:\n                    release, release_error = None, True\n                if self._identity(os.fstat(stream.fileno())) != identity:\n                    raise ManagerError("changed", "Файл изменился во время проверки.")\n            after = self._file_info(path)\n            if after is None or self._identity(after) != identity:\n                raise ManagerError("changed", "Файл изменился во время проверки.")\n        except OSError:\n            raise ManagerError("read", "Не удалось прочитать архив мода.") from None\n        result = {"digest": hasher.hexdigest(), "valid_header": valid_header,\n                  "release": release, "release_error": release_error}\n        self._hash_cache[str(path)] = (identity, result)\n        return result\n\n    @staticmethod\n    def _automatic_component(item):\n        return RELEASE_COMPONENTS.get(item["id"]) == item["filename"]\n\n    def _recognized(self, item, result):\n        if not result or not result["valid_header"] or result["release_error"]:\n            return False\n        if result["release"]:\n            return (self._automatic_component(item)\n                    and result["release"]["id"] == item["id"]\n                    and result["release"]["filename"] == item["filename"])\n        return result["digest"] == item["sha256"]\n\n    def _control_path(self, kind):\n        return self.data_dir / {"pending": "pending.json", "journal": "journal.json",\n                                "result": "last_result.json"}[kind]\n\n    def _ensure_data_dir(self):\n        self._check_directory(self.game_dir)\n        try:\n            self.data_dir.mkdir(exist_ok=True)\n        except OSError:\n            raise ManagerError("write", "Не удалось создать папку настроек менеджера.") from None\n        self._check_directory(self.data_dir)\n\n    def _validate_actions(self, actions, historical=False):\n        if not isinstance(actions, list) or not actions or len(actions) > (len(self._builtin_catalog) + 64 if historical else len(self.catalog)):\n            raise ManagerError("control", "План менеджера повреждён; файлы сохранены.")\n        seen = set()\n        for action in actions:\n            if not isinstance(action, dict) or set(action) != {\n                    "id", "enabled", "source", "destination", "sha256"}:\n                raise ManagerError("control", "План менеджера повреждён; файлы сохранены.")\n            key = action["id"]\n            historical_external = (historical and isinstance(key, str)\n                                   and re.fullmatch(r"external_[a-z0-9_]{1,48}", key))\n            if (not isinstance(key, str) or (key not in self.by_id and not historical_external) or key in seen\n                    or type(action["enabled"]) is not bool):\n                raise ManagerError("control", "План менеджера не соответствует каталогу.")\n            seen.add(key)\n            item = self.by_id.get(key) or {"filename": "zz_mod_" + key[9:] + ".rpa"}\n            active, disabled = item["filename"], item["filename"] + ".disabled"\n            source, target = (disabled, active) if action["enabled"] else (active, disabled)\n            if (action["source"] != source or action["destination"] != target\n                    or not isinstance(action["sha256"], str)\n                    or not re.fullmatch(r"[a-f0-9]{64}", action["sha256"])\n                    or (not historical and not item.get("external") and not self._automatic_component(item)\n                        and action["sha256"] != item["sha256"])):\n                raise ManagerError("control", "План менеджера не соответствует каталогу.")\n\n    def _validate_document(self, value, kind):\n        base = {"owner", "schema", "kind", "transaction_id", "created_at", "actions"}\n        extra = {"pending": set(), "journal": {"phase", "completed"},\n                 "result": {"outcome"}}[kind]\n        if (not isinstance(value, dict) or set(value) != base | extra\n                or value.get("owner") != self.OWNER or type(value.get("schema")) is not int\n                or value.get("schema") != self.SCHEMA or value.get("kind") != kind\n                or not isinstance(value.get("transaction_id"), str)\n                or not re.fullmatch(r"[a-f0-9]{32}", value["transaction_id"])\n                or not isinstance(value.get("created_at"), str)\n                or not re.fullmatch(r"\\d{4}-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ", value["created_at"])):\n            raise ManagerError("control", "Файл состояния менеджера неизвестен или повреждён; он сохранён.")\n        # Completed receipts describe past files; they never authorize renames.\n        # Pending plans and recovery journals must still match current digests.\n        self._validate_actions(value["actions"], historical=(kind == "result"))\n        if kind == "journal":\n            completed = value["completed"]\n            if (value["phase"] not in ("applying", "rolling_back", "recovery_required")\n                    or not isinstance(completed, list)\n                    or any(not isinstance(key, str) for key in completed)\n                    or len(completed) != len(set(completed))\n                    or not set(completed) <= {a["id"] for a in value["actions"]}):\n                raise ManagerError("control", "Журнал менеджера повреждён; он сохранён.")\n        if kind == "result" and value["outcome"] not in (\n                "applied", "rolled_back", "recovery_required"):\n            raise ManagerError("control", "Результат менеджера повреждён; он сохранён.")\n        return value\n\n    def _read_document(self, kind):\n        if not os.path.lexists(self.data_dir):\n            self._check_directory(self.game_dir)\n            return None\n        path = self._control_path(kind)\n        info = self._file_info(path)\n        if info is None:\n            return None\n        if info.st_size > self.MAX_JSON:\n            raise ManagerError("control", "Файл состояния менеджера имеет неверный размер.")\n        try:\n            # Reject duplicate JSON keys rather than silently taking the last one.\n            def unique_pairs(pairs):\n                result = {}\n                for key, item in pairs:\n                    if key in result:\n                        raise ValueError("duplicate key")\n                    result[key] = item\n                return result\n            with path.open("rb") as stream:\n                raw = stream.read(self.MAX_JSON + 1)\n            if len(raw) > self.MAX_JSON:\n                raise ValueError("oversized document")\n            after = self._file_info(path)\n            if after is None or self._identity(info) != self._identity(after):\n                raise ManagerError("changed", "Состояние менеджера изменилось во время чтения.")\n            value = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_pairs)\n        except (OSError, ValueError, UnicodeError):\n            raise ManagerError("control", "Файл состояния менеджера неизвестен или повреждён; он сохранён.") from None\n        return self._validate_document(value, kind)\n\n    def _write_document(self, value, expected=None, require_absent=False):\n        kind = value["kind"]\n        self._validate_document(value, kind)\n        self._ensure_data_dir()\n        current = self._read_document(kind)\n        if require_absent and current is not None:\n            raise ManagerError("conflict", "Другая операция менеджера уже началась.")\n        if expected is not None and current != expected:\n            raise ManagerError("changed", "Состояние менеджера изменено; запись остановлена.")\n        path = self._control_path(kind)\n        temporary = self.data_dir / ("." + kind + "." + uuid.uuid4().hex + ".tmp")\n        created_identity = None\n        try:\n            with temporary.open("xb") as stream:\n                created_identity = self._identity(os.fstat(stream.fileno()))\n                stream.write((json.dumps(value, ensure_ascii=False, indent=2) + "\\n").encode("utf-8"))\n                stream.flush()\n                os.fsync(stream.fileno())\n                created_identity = self._identity(os.fstat(stream.fileno()))\n            if self._read_document(kind) != current:\n                raise ManagerError("changed", "Состояние менеджера изменено; запись остановлена.")\n            self._check_directory(self.data_dir)\n            if current is None:\n                self._rename(temporary, path)\n            else:\n                os.replace(temporary, path)\n        except OSError:\n            raise ManagerError("write", "Не удалось сохранить состояние менеджера.") from None\n        finally:\n            if created_identity is not None:\n                try:\n                    current_info = self._file_info(temporary)\n                    if current_info and self._identity(current_info) == created_identity:\n                        temporary.unlink()\n                except (OSError, ManagerError):\n                    pass\n\n    def _remove_document(self, value):\n        if self._read_document(value["kind"]) != value:\n            raise ManagerError("changed", "Состояние менеджера изменено; удаление остановлено.")\n        try:\n            self._control_path(value["kind"]).unlink()\n        except OSError:\n            raise ManagerError("write", "Не удалось удалить подтверждённый файл состояния менеджера.") from None\n\n    def _check_no_journal(self):\n        if self._read_document("journal") is not None:\n            raise ManagerError("recovery_required", "Предыдущее применение прервано. Нужна проверка файлов; переключение заблокировано.")\n\n    def pending(self):\n        return self._read_document("pending")\n\n    def last_result(self):\n        return self._read_document("result")\n\n    def scan(self):\n        self.status_error = None\n        try:\n            self._refresh_external_mods()\n            self._check_no_journal()\n            self.pending()\n        except ManagerError as error:\n            self.status_error = str(error)\n        rows = []\n        for item in self.catalog:\n            row = dict(item, state="missing", can_toggle=False, enabled=None,\n                       actual_path=None, digest=None, reason="Архив не найден.")\n            try:\n                active = self.game_dir / item["filename"]\n                disabled = self.game_dir / (item["filename"] + ".disabled")\n                active_info, disabled_info = self._file_info(active), self._file_info(disabled)\n                if active_info and disabled_info:\n                    row.update(state="conflict", reason="Есть и включённая, и выключенная копия.")\n                elif active_info or disabled_info:\n                    enabled = active_info is not None\n                    source = active if enabled else disabled\n                    # Re-read automatic mods on refresh even when a copier retained\n                    # size and timestamps. Actual rename always rechecks all bytes.\n                    result = self._fingerprint(source, fresh=self._automatic_component(item) or item.get("external", False))\n                    if result is None:\n                        raise ManagerError("changed", "Архив исчез во время проверки.")\n                    recognised = self._recognized(item, result)\n                    if recognised and self._automatic_component(item) and result["release"]:\n                        row.update(version=result["release"]["version"],\n                                   sha256=result["digest"], recognition="signed-release")\n                    elif recognised and item.get("external"):\n                        row["recognition"] = "author-manifest"\n                    row.update(state=("enabled" if enabled else "disabled") if recognised else "changed",\n                               enabled=enabled, actual_path=str(source), digest=result["digest"],\n                               can_toggle=recognised, reason="" if recognised else (\n                                   "Архив повреждён или подпись выпуска недействительна."\n                                   if result["release_error"] else "Архив изменён или его версия неизвестна."))\n            except ManagerError as error:\n                row.update(state="conflict", reason=str(error), can_toggle=False)\n            if self.status_error:\n                row.update(can_toggle=False, reason=self.status_error)\n            rows.append(row)\n        return rows\n\n    def stage(self, desired):\n        rows = {row["id"]: row for row in self.scan()}\n        self._check_no_journal()\n        self.pending()  # Never replace a corrupt or foreign pending file.\n        if not isinstance(desired, dict) or any(\n                key not in self.by_id or type(enabled) is not bool for key, enabled in desired.items()):\n            raise ManagerError("selection", "Неверный выбор модов.")\n        actions = []\n        for item in self.catalog:\n            key = item["id"]\n            if key not in desired:\n                continue\n            row = rows[key]\n            if not row["can_toggle"]:\n                raise ManagerError("unavailable", row["reason"] or "Мод нельзя переключить.")\n            if row["enabled"] == desired[key]:\n                continue\n            active, disabled = item["filename"], item["filename"] + ".disabled"\n            source, target = (disabled, active) if desired[key] else (active, disabled)\n            actions.append(dict(id=key, enabled=desired[key], source=source,\n                                destination=target, sha256=row["digest"]))\n        if not actions:\n            self.cancel()\n            return None\n        pending = dict(owner=self.OWNER, schema=self.SCHEMA, kind="pending",\n                       transaction_id=uuid.uuid4().hex,\n                       created_at=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),\n                       actions=actions)\n        # Fresh verification when staging also catches edits with retained timestamps.\n        self._preflight(actions)\n        self._write_document(pending)\n        return pending\n\n    def cancel(self):\n        self._check_no_journal()\n        pending = self.pending()\n        if pending is not None:\n            self._remove_document(pending)\n            return True\n        return False\n\n    def _preflight(self, actions, reverse=False):\n        self._refresh_external_mods()\n        self._validate_actions(actions)\n        self._check_directory(self.game_dir)\n        for action in actions:\n            source = self.game_dir / action["destination" if reverse else "source"]\n            target = self.game_dir / action["source" if reverse else "destination"]\n            if self._file_info(target) is not None:\n                raise ManagerError("conflict", "Целевое имя уже занято; файлы сохранены.")\n            result = self._fingerprint(source, fresh=True)\n            if (not self._recognized(self.by_id[action["id"]], result)\n                    or result["digest"] != action["sha256"]):\n                raise ManagerError("changed", "Архив изменён или отсутствует; применение остановлено.")\n\n    def _rename(self, source, target):\n        if os.path.lexists(target):\n            raise FileExistsError("destination exists")\n        if os.name == "nt":\n            # Windows os.rename is non-replacing, unlike os.replace.\n            os.rename(source, target)\n        else:\n            # Exclusive hard-link creation provides non-replacement on POSIX too.\n            os.link(source, target, follow_symlinks=False)\n            try:\n                os.unlink(source)\n            except OSError:\n                os.unlink(target)\n                raise\n\n    def _result(self, pending, outcome):\n        result = dict(pending, kind="result", outcome=outcome)\n        self._write_document(result)\n        return result\n\n    def apply_pending(self):\n        """Call only at the end of the engine\'s exit, once RPA handles are closed."""\n        self._check_no_journal()\n        pending = self.pending()\n        if pending is None:\n            return None\n        self._preflight(pending["actions"])\n        # Validate the result slot before modifying any archives.\n        self.last_result()\n        journal = dict(pending, kind="journal", phase="applying", completed=[])\n        self._write_document(journal, require_absent=True)\n        completed = []\n        try:\n            if self.pending() != pending:\n                raise ManagerError("changed", "План изменён; применение остановлено.")\n            for action in pending["actions"]:\n                self._preflight([action])\n                self._rename(self.game_dir / action["source"], self.game_dir / action["destination"])\n                completed.append(action)\n                self._preflight([action], reverse=True)\n                next_journal = dict(journal, completed=[a["id"] for a in completed])\n                self._write_document(next_journal, expected=journal)\n                journal = next_journal\n            self._preflight(pending["actions"], reverse=True)\n            result = self._result(pending, "applied")\n        except (ManagerError, OSError):\n            # Roll back only files demonstrably matching this transaction.\n            rollback_ok = True\n            try:\n                next_journal = dict(journal, phase="rolling_back")\n                self._write_document(next_journal, expected=journal)\n                journal = next_journal\n            except ManagerError:\n                rollback_ok = False\n            for action in reversed(completed):\n                try:\n                    self._preflight([action], reverse=True)\n                    self._rename(self.game_dir / action["destination"], self.game_dir / action["source"])\n                except (ManagerError, OSError):\n                    rollback_ok = False\n                    break\n            if rollback_ok:\n                try:\n                    self._preflight(pending["actions"])\n                    self._result(pending, "rolled_back")\n                    self._remove_document(journal)\n                except ManagerError:\n                    rollback_ok = False\n            if not rollback_ok:\n                try:\n                    next_journal = dict(journal, phase="recovery_required")\n                    self._write_document(next_journal, expected=journal)\n                    self._result(pending, "recovery_required")\n                except ManagerError:\n                    pass\n                raise ManagerError("recovery_required", "Применение прервано. Журнал сохранён; нужна проверка файлов.") from None\n            raise ManagerError("rolled_back", "Не удалось применить изменения. Исходное состояние восстановлено; план сохранён.") from None\n        # If cleanup fails, leave the journal to block further mutations.\n        try:\n            self._remove_document(pending)\n            self._remove_document(journal)\n        except ManagerError:\n            raise ManagerError("recovery_required", "Моды переключены, но журнал не закрыт. Нужна проверка файлов.") from None\n        self._hash_cache.clear()\n        return result\n\n\nclass ScanJob:\n    """One read-only scan; publish its complete result via a thread-safe queue.\n\n    The UI owns this object and polls it. The worker never calls the engine,\n    changes store variables, stages a plan, or mutates game files.\n    """\n    def __init__(self, game_dir, catalog, factory=ManagerCore):\n        import queue\n        import threading\n        self._results = queue.Queue(maxsize=1)\n        self._thread = threading.Thread(target=self._run,\n            args=(game_dir, [dict(item) for item in catalog], factory),\n            name="LSSB mod validation", daemon=True)\n        self._thread.start()\n\n    def _run(self, game_dir, catalog, factory):\n        try:\n            controller = factory(game_dir, catalog)\n            rows = controller.scan()\n            issue = controller.status_error or ""\n            choices = {row["id"]: row["enabled"] for row in rows if row["can_toggle"]}\n            notice = ""\n            if not issue:\n                pending = controller.pending()\n                if pending:\n                    for action in pending["actions"]:\n                        if action["id"] in choices:\n                            choices[action["id"]] = action["enabled"]\n                    notice = "Сохранённый выбор ещё не применён. Проверьте его перед выходом."\n                else:\n                    last = controller.last_result()\n                    if last:\n                        notice = ("Предыдущие изменения успешно применены." if last.get("outcome") == "applied"\n                            else "Предыдущие изменения не применены. Проверьте состояние файлов.")\n            result = dict(controller=controller, rows=rows, choices=choices, issue=issue, notice=notice)\n        except Exception as exc:\n            result = dict(controller=None, rows=[], choices={}, issue=str(exc), notice="")\n        self._results.put(result)\n\n    def poll(self):\n        import queue\n        try:\n            return self._results.get_nowait()\n        except queue.Empty:\n            return None\n', 'lssb_mod_manager_core', 'exec'), _core_module.__dict__)
    ManagerCore = _core_module.ManagerCore
    ManagerError = _core_module.ManagerError
    catalog = [{'id': 'localization_ru', 'name': 'Русская локализация', 'description': 'Русский интерфейс, ветки персонажей, общие события, концерты, вступление, обучение и локации.', 'version': '1.88.0-own', 'filename': 'zzzzzz_lssb_localization_ru.rpa', 'sha256': 'd27a213832c227f5fd720478cfdff5510a5774ba742282a4f86fd416b48a2e37'}, {'id': 'visual_quality', 'name': 'Фоны, карта и интерфейс', 'description': 'Фоны высокого разрешения, чёткий интерфейс и настройка плавности.', 'version': '1.6.0-own', 'filename': 'zzzzz_lssb_visual_quality.rpa', 'sha256': '0cd8576c0f5e0b440e7281cfb515292830d8583becfa7da6d9bdd0226901e2a5'}, {'id': 'startup_fast', 'name': 'Быстрый запуск', 'description': 'Ускоряет подготовку изображений при запуске игры.', 'version': '1.2.0-own', 'filename': 'zzzzzzz_lssb_startup_fast.rpa', 'sha256': 'd132d49844d2dc1cf277c98fa1a2c7747a77d0af2eac23ab56763133c4ed6a52'}]
    version = '1.4.1-own'
    supported = (hasattr(getattr(config, 'python_exit_callbacks', None), 'append')
        and hasattr(getattr(config, 'always_shown_screens', None), 'append')
        and all(callable(getattr(api, name, None)) for name in ('show_screen', 'restart_interaction', 'quit')))
    controller = None
    rows = []
    choices = {}
    issue = ''
    notice = ''
    armed = False

    busy = False
    scan_job = None

    def refresh():
        global busy, scan_job, rows, choices, issue, notice
        if busy:
            return
        rows = [dict(item, version='…', enabled=False, can_toggle=False, state='checking', reason='') for item in catalog]
        choices = {}
        issue = ''
        notice = ''
        if not supported:
            issue = 'В движке недоступны функции безопасного переключения модов.'
            return
        try:
            scan_job = _core_module.ScanJob(config.gamedir, catalog)
            busy = True
        except Exception as exc:
            scan_job = None
            issue = str(exc)

    def poll_scan():
        global controller, rows, choices, issue, notice, busy, scan_job
        if not busy or scan_job is None:
            return
        result = scan_job.poll()
        if result is None:
            return
        controller = result['controller']
        rows = result['rows']
        choices = result['choices']
        issue = result['issue']
        notice = result['notice']
        scan_job = None
        busy = False
        api.restart_interaction()

    def open_manager():
        refresh()
        api.show_screen('lssb_mod_manager')
        api.restart_interaction()

    def toggle(mod_id):
        global choices, notice
        if issue or busy:
            return
        if any(row['id'] == mod_id and row['can_toggle'] for row in rows):
            choices = dict(choices)
            choices[mod_id] = not choices[mod_id]
            notice = ''
            api.restart_interaction()

    def changes():
        return [row for row in rows if row['can_toggle'] and choices.get(row['id']) != row['enabled']]

    def status(row):
        labels = {'checking': 'Проверяется', 'enabled': 'Включён', 'disabled': 'Отключён', 'missing': 'Не установлен',
                  'changed': 'Файл изменён', 'conflict': 'Конфликт файлов', 'recovery_required': 'Нужна проверка'}
        if row['can_toggle'] and choices.get(row['id']) != row['enabled']:
            return 'Будет включён' if choices[row['id']] else 'Будет отключён'
        return labels.get(row['state'], 'Недоступен')

    def discard():
        global issue
        if busy or controller is None:
            return
        try:
            controller.cancel()
            refresh()
        except Exception as exc:
            issue = str(exc)
        api.restart_interaction()

    def commit_and_exit():
        global armed, issue
        if busy or issue or controller is None:
            return
        try:
            plan = controller.stage({row['id']: choices[row['id']] for row in rows if row['can_toggle']})
            if not plan:
                refresh()
                return
            armed = True
        except Exception as exc:
            issue = str(exc)
            api.hide_screen('lssb_mm_confirm')
            api.restart_interaction()
            return
        # Bootstrap's native relaunch starts too early; apply in its late callback.
        if any(action['id'] == 'visual_quality' and not action['enabled'] for action in plan['actions']):
            import store
            performance = getattr(store, 'lssb_performance', None)
            if performance is not None and performance.supported:
                performance.restore_preferences()
        api.quit(relaunch=False, save=True)

    def late_apply():
        global armed
        if not armed or controller is None:
            return
        armed = False
        try:
            controller.apply_pending()
        except Exception as exc:
            # Core preserves its plan/journal on failures; report again on next open.
            try:
                api.log('LSSB Mod Manager: изменения не применены: ' + str(exc))
            except Exception:
                pass

    if supported:
        config.python_exit_callbacks.append(late_apply)
    # Engine overlay survives changes to the native main/game menu and language.
    if hasattr(getattr(config, 'always_shown_screens', None), 'append'):
        if 'lssb_mm_entry_overlay' not in config.always_shown_screens:
            config.always_shown_screens.append('lssb_mm_entry_overlay')

    def compatibility_notes():
        import store
        result = []
        compat = getattr(store, 'lssb_compat', None)
        if compat is not None:
            result.extend(compat.messages())
        startup = getattr(store, 'lssb_startup_fast', None)
        if startup is not None and not startup.enabled:
            result.append('Быстрый запуск: используется обычный запуск — реализация движка изменилась.')
        performance = getattr(store, 'lssb_performance', None)
        if performance is not None and not performance.supported:
            result.append('Плавность: используется штатная отрисовка — функции движка изменились.')
        return result

screen lssb_mm_entry_overlay():
    zorder 290
    if (renpy.get_screen('main_menu') or renpy.get_screen('game_menu') or renpy.get_screen('preferences')) and not renpy.get_screen('lssb_mod_manager'):
        textbutton "Моды" style "lssb_mm_entry" align (0.98, 0.03) action Function(lssb_mm.open_manager)
    key "shift_K_F10" action Function(lssb_mm.open_manager)

screen lssb_mod_manager():
    modal True
    zorder 300
    if lssb_mm.busy:
        timer 0.05 repeat True action Function(lssb_mm.poll_scan)
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action Hide("lssb_mod_manager")
    add Solid("#071a28eb")
    frame:
        style "lssb_mm_panel"
        xysize (1160, 640)
        align (0.5, 0.5)
        vbox:
            spacing 14
            hbox:
                xfill True
                vbox:
                    text "МЕНЕДЖЕР МОДОВ" style "lssb_mm_title"
                    text ("Love & Sex: Second Base · %s   |   Менеджер 1.4.1-own" % config.version) style "lssb_mm_subtitle"
                null width 28
                if renpy.has_screen('lssb_performance_settings'):
                    textbutton "Плавность" style "lssb_mm_button" action Show("lssb_performance_settings")
                    null width 12
                textbutton "Закрыть" style "lssb_mm_button" action Hide("lssb_mod_manager")
            hbox:
                spacing 24
                text "Выберите моды для следующего запуска игры." style "lssb_mm_text"
                textbutton ("Совместимость: есть замечания" if lssb_mm.compatibility_notes() else "Совместимость") style "lssb_mm_button" padding (12, 6) yminimum 30 action Show("lssb_mm_compatibility")
            viewport:
                xysize (1104, 366)
                mousewheel True
                draggable True
                scrollbars "vertical"
                has vbox
                spacing 8
                for row in lssb_mm.rows:
                    frame:
                        style "lssb_mm_card"
                        xysize (1080, 66)
                        hbox:
                            spacing 16
                            vbox:
                                xsize 534
                                text row['name'] style "lssb_mm_name"
                                text row['description'] style "lssb_mm_description"
                            text row['version'] style "lssb_mm_meta" xsize 62 yalign 0.5
                            vbox:
                                xsize 182
                                yalign 0.5
                                text lssb_mm.status(row) style "lssb_mm_status"
                                if row.get('reason'):
                                    text row['reason'] style "lssb_mm_description" size 12
                            textbutton (("ВКЛЮЧЁН" if lssb_mm.choices.get(row['id'], row['enabled']) else "ОТКЛЮЧЁН") if row['can_toggle'] else ("ПРОВЕРКА" if lssb_mm.busy else "НЕДОСТУПЕН")):
                                style "lssb_mm_toggle"
                                selected bool(lssb_mm.choices.get(row['id'], row['enabled']))
                                sensitive row['can_toggle'] and not lssb_mm.issue and not lssb_mm.busy
                                action Function(lssb_mm.toggle, row['id'])
            if lssb_mm.busy:
                text "Проверка модов… Окно можно закрыть." style "lssb_mm_subtitle"
            elif lssb_mm.issue:
                text lssb_mm.issue style "lssb_mm_error" xmaximum 1090
            elif lssb_mm.changes():
                text ("Изменений: %d. Они применятся после закрытия игры." % len(lssb_mm.changes())) style "lssb_mm_text"
            elif lssb_mm.notice:
                text lssb_mm.notice style "lssb_mm_subtitle"
            else:
                text "Все моды показаны в текущем состоянии. Файлы игры и сохранения не заменяются." style "lssb_mm_subtitle"
            hbox:
                spacing 16
                textbutton "Сбросить выбор" style "lssb_mm_button" action Function(lssb_mm.discard) sensitive not lssb_mm.busy and lssb_mm.controller is not None
                textbutton "Обновить список" style "lssb_mm_button" action Function(lssb_mm.refresh) sensitive not lssb_mm.busy
                null width 138
                textbutton "Применить и выйти":
                    style "lssb_mm_primary"
                    sensitive bool(lssb_mm.changes()) and not lssb_mm.issue and not lssb_mm.busy
                    action Show("lssb_mm_confirm")

screen lssb_mm_compatibility():
    modal True
    zorder 320
    key ["K_ESCAPE", "mouseup_3"] action Hide("lssb_mm_compatibility")
    add Solid("#071a28eb")
    frame:
        style "lssb_mm_panel"
        xysize (1000, 600)
        align (0.5, 0.5)
        vbox:
            spacing 20
            text "СОВМЕСТИМОСТЬ" style "lssb_mm_title"
            text "Обновление номера игры не отключает моды. Изменившиеся экраны используют штатный интерфейс." style "lssb_mm_text" xmaximum 940
            viewport:
                ysize 350
                mousewheel True
                draggable True
                scrollbars "vertical"
                vbox:
                    spacing 12
                    for note in lssb_mm.compatibility_notes():
                        text note style "lssb_mm_text" xmaximum 900
                    if not lssb_mm.compatibility_notes():
                        text "Несовместимые компоненты не обнаружены." style "lssb_mm_text"
            textbutton "Закрыть" style "lssb_mm_button" action Hide("lssb_mm_compatibility")

screen lssb_mm_confirm():
    modal True
    zorder 310
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action Hide("lssb_mm_confirm")
    add Solid("#041018d9")
    frame:
        style "lssb_mm_panel"
        xsize 780
        align (0.5, 0.5)
        vbox:
            spacing 18
            text "ПРИМЕНИТЬ ИЗМЕНЕНИЯ" style "lssb_mm_title" size 28
            for row in lssb_mm.changes():
                text (("Включить: " if lssb_mm.choices[row['id']] else "Отключить: ") + row['name']) style "lssb_mm_text"
            text "Игра закроется. При следующем запуске будет выбранный набор модов." style "lssb_mm_text" xmaximum 710
            if not main_menu:
                text "Перед выходом сохраните текущий прогресс." style "lssb_mm_error"
            hbox:
                spacing 24
                textbutton "Назад" style "lssb_mm_button" action Hide("lssb_mm_confirm")
                textbutton "Применить и выйти" style "lssb_mm_primary" action Function(lssb_mm.commit_and_exit)

style lssb_mm_panel is empty:
    background Solid("#173c50")
    padding (28, 24)
style lssb_mm_card is empty:
    background Solid("#214d63")
    padding (16, 8)
style lssb_mm_text is text:
    font "DejaVuSans.ttf"
    size 19
    color "#ecf6fc"
    outlines []
style lssb_mm_title is lssb_mm_text:
    font "DejaVuSans-Bold.ttf"
    size 30
style lssb_mm_subtitle is lssb_mm_text:
    size 16
    color "#b0cbd9"
style lssb_mm_name is lssb_mm_title:
    size 21
style lssb_mm_description is lssb_mm_subtitle:
    size 14
style lssb_mm_meta is lssb_mm_subtitle:
    size 16
style lssb_mm_status is lssb_mm_text:
    size 16
    color "#b9e9f7"
style lssb_mm_error is lssb_mm_text:
    color "#ffd095"
    size 16
style lssb_mm_button is button:
    background Solid("#32687c")
    hover_background Solid("#438ba0")
    insensitive_background Solid("#294b5c")
    padding (18, 12)
    yminimum 44
style lssb_mm_button_text is lssb_mm_text:
    size 17
    insensitive_color "#91aab7"
    align (0.5, 0.5)
style lssb_mm_toggle is lssb_mm_button:
    xsize 166
    selected_idle_background Solid("#157d85")
    selected_hover_background Solid("#239e9e")
style lssb_mm_toggle_text is lssb_mm_button_text:
    size 15
style lssb_mm_primary is lssb_mm_button:
    background Solid("#167f8c")
    hover_background Solid("#209fb0")
style lssb_mm_primary_text is lssb_mm_button_text
style lssb_mm_entry is lssb_mm_button:
    xsize 160
style lssb_mm_entry_text is lssb_mm_button_text
