"""Small filesystem core for the in-game LSSB mod manager.

Only catalogued or signed first-party mod archives can be renamed.
Plans bind exact bytes even when later releases are recognised automatically.
A surviving journal deliberately requires manual recovery.
This module does not import Ren'Py or inspect game saves.
"""
import datetime
import base64
import hashlib
import hmac
import json
import os
from pathlib import Path
import re
import stat
import struct
import uuid


RELEASE_MAGIC = b"\nLSSB-RELEASE-V1\n"
RELEASE_DOMAIN = b"LSSB localization release v1\0"
MOD_RELEASE_DOMAIN = b"LSSB first-party mod release v2\0"
RELEASE_COMPONENTS = {
    "localization_ru": "zzzzzz_lssb_localization_ru.rpa",
    "visual_quality": "zzzzz_lssb_visual_quality.rpa",
    "startup_fast": "zzzzzzz_lssb_startup_fast.rpa",
}
RELEASE_MAX_JSON = 8192
RELEASE_KEY_ID = "lssb-localization-20261021"
# Public verification key only. The private signing key is never distributed.
RELEASE_KEYS = {RELEASE_KEY_ID: (int(
    "d61f1e84aff38380042a973917df3101c1ff7d33401df3cfb47ad0a088ccc7d994309503b91cee4a0407c1a96d125cd3bddd9b116744bf19d3403f42ff003e69373d87af82ecf90c8dd8f070f891a0245f52a22fab628ae7136871a7a54be5a6260571ca98ca25fb4b1be3e6a0ac18de88a2f379997b32b625f53ed94c7b76575b1888c9ab51d9edf93c4494b23762dc504997dd891d011eb40b7cee969897a6080ba665b54312e43a5bd611698187ad4fa6452222fdb5741926422bd0765183a1c182e5c59543b2e1343fb7db9ed771cac1f43109853dbc386da7954fa568a4a8f220feda3bcc6b44c098c3eb625a0a17a8420037b42b35e0c68c882a96a5a0f45c5b9bde11defc8172fdd77433a78e616d54e48778714c3564935554413e5bf99c812a71302c8d7f7e22349caae13f4b124ec9cac30377118b62b555f5cef6188fd799f78491a5cbff45540a723f0906d00a14d9afae8265dafd64325b992a3df98c7590c1ff18f9ef73ed7efd9be7264262897a692e7787f0023120490b1b",
    16), 65537)}


def release_message(payload):
    domain = MOD_RELEASE_DOMAIN if payload.get("schema") == 2 else RELEASE_DOMAIN
    return domain + json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")


def _unique_release_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate release key")
        result[key] = value
    return result


def _verify_release_signature(message, signature, key_id):
    """RSA-PSS/SHA-256, fixed 32-byte salt; RFC 8017 section 9.1.2.

    Verification uses only public operations and the standard library so the
    game does not need a cryptography package. Signing uses cryptography.
    """
    key = RELEASE_KEYS.get(key_id)
    if key is None:
        return False
    modulus, exponent = key
    size = (modulus.bit_length() + 7) // 8
    if len(signature) != size or int.from_bytes(signature, "big") >= modulus:
        return False
    bits = modulus.bit_length() - 1
    length = (bits + 7) // 8
    decoded = pow(int.from_bytes(signature, "big"), exponent, modulus).to_bytes(size, "big")
    if any(decoded[:size-length]):
        return False
    encoded = decoded[size-length:]
    if length < 66 or encoded[-1] != 0xbc:
        return False
    masked, digest = encoded[:-33], encoded[-33:-1]
    unused = 8 * length - bits
    if masked[0] & (0xff << (8-unused) if unused else 0):
        return False
    mask = b"".join(hashlib.sha256(digest + struct.pack(">I", counter)).digest()
                    for counter in range((len(masked) + 31) // 32))[:len(masked)]
    data = bytearray(a ^ b for a, b in zip(masked, mask))
    data[0] &= 0xff >> unused
    padding = length - 66
    if any(data[:padding]) or data[padding] != 1:
        return False
    expected = hashlib.sha256(b"\0" * 8 + hashlib.sha256(message).digest() + data[-32:]).digest()
    return hmac.compare_digest(digest, expected)


def read_release_footer(stream, file_size):
    """Read bounded JSON, never the RPA's pickle index or executable payload.

    Returns None for a legacy archive. A present but invalid footer raises.
    The caller hashes the signed prefix using this same opened file handle.
    """
    tail_size = len(RELEASE_MAGIC) + 4
    if file_size < tail_size + 34:
        return None
    stream.seek(file_size - tail_size)
    tail = stream.read(tail_size)
    if not tail.endswith(RELEASE_MAGIC):
        return None
    size = struct.unpack(">I", tail[:4])[0]
    prefix_size = file_size - tail_size - size
    if not 0 < size <= RELEASE_MAX_JSON or prefix_size < 34:
        raise ValueError("invalid release size")
    stream.seek(prefix_size)
    envelope = json.loads(stream.read(size).decode("utf-8"), object_pairs_hook=_unique_release_pairs)
    if not isinstance(envelope, dict) or set(envelope) != {"key_id", "payload", "signature"}:
        raise ValueError("invalid release envelope")
    payload = envelope["payload"]
    fields = {"schema", "owner", "id", "filename", "version", "archive_size", "archive_sha256"}
    if (not isinstance(payload, dict) or set(payload) != fields
            or type(payload["schema"]) is not int or payload["schema"] not in (1, 2)
            or payload["owner"] != "lssb-russian-mods"
            or not isinstance(payload["id"], str)
            or payload["id"] not in RELEASE_COMPONENTS
            or (payload["schema"] == 1) != (payload["id"] == "localization_ru")
            or payload["filename"] != RELEASE_COMPONENTS[payload["id"]]
            or not isinstance(payload["version"], str)
            or not re.fullmatch(r"[0-9]{1,5}\.[0-9]{1,5}\.[0-9]{1,5}(?:-[A-Za-z0-9][A-Za-z0-9.-]{0,31})?", payload["version"])
            or type(payload["archive_size"]) is not int or payload["archive_size"] != prefix_size
            or not isinstance(payload["archive_sha256"], str)
            or not re.fullmatch(r"[a-f0-9]{64}", payload["archive_sha256"])
            or not isinstance(envelope["key_id"], str) or not isinstance(envelope["signature"], str)):
        raise ValueError("invalid release identity")
    signature = base64.b64decode(envelope["signature"], validate=True)
    if not _verify_release_signature(release_message(payload), signature, envelope["key_id"]):
        raise ValueError("invalid release signature")
    return payload


class ManagerError(Exception):
    def __init__(self, code, message):
        self.code = code
        super().__init__(message)


class ManagerCore:
    OWNER = "lssb-in-game-mod-manager"
    SCHEMA = 1
    DATA_DIR = "lssb_mod_manager_data"
    MAX_JSON = 131072
    _HEADER = re.compile(br"RPA-3\.0 [0-9a-fA-F]{16} [0-9a-fA-F]{8}\n")

    def __init__(self, game_dir, catalog):
        self.game_dir = Path(os.path.abspath(os.fspath(game_dir)))
        self.data_dir = self.game_dir / self.DATA_DIR
        self.catalog = []
        self.by_id = {}
        self._hash_cache = {}
        self.status_error = None
        seen_names = set()
        for item in catalog:
            item = dict(item)
            key, name, digest = item.get("id"), item.get("filename"), item.get("sha256")
            if (not isinstance(key, str) or not re.fullmatch(r"[a-z0-9_]{1,64}", key)
                    or key in self.by_id or not isinstance(name, str)
                    or not re.fullmatch(r"[A-Za-z0-9_-]+\.rpa", name)
                    or name.lower() in seen_names or not isinstance(digest, str)
                    or not re.fullmatch(r"[a-f0-9]{64}", digest)):
                raise ManagerError("catalog", "Неверный каталог модов.")
            conflicts = item.get("incompatible_files", [])
            if (not isinstance(conflicts, list) or any(not isinstance(n, str)
                    or not re.fullmatch(r"[A-Za-z0-9_-]+\.rpa", n)
                    or n.lower() == name.lower() for n in conflicts)):
                raise ManagerError("catalog", "Неверный список несовместимых архивов.")
            seen_names.add(name.lower())
            self.catalog.append(item)
            self.by_id[key] = item
        self._check_directory(self.game_dir)
        self._builtin_catalog = list(self.catalog)
        self._refresh_external_mods()

    def _refresh_external_mods(self):
        """Discover opt-in author metadata; never execute an archive to identify it."""
        self._check_directory(self.game_dir)
        paths = sorted(self.game_dir.glob("*.lssb-mod.json"))
        if len(paths) > 64:
            raise ManagerError("metadata", "Слишком много описаний сторонних модов (максимум 64).")
        additions = []
        names = {item["filename"].lower() for item in self._builtin_catalog}
        for path in paths:
            try:
                before = self._file_info(path)
                if before is None or not 0 < before.st_size <= RELEASE_MAX_JSON:
                    raise ValueError("size")
                flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
                with os.fdopen(os.open(path, flags), "rb") as stream:
                    if self._identity(os.fstat(stream.fileno())) != self._identity(before):
                        raise ValueError("changed")
                    item = json.loads(stream.read(RELEASE_MAX_JSON + 1).decode("utf-8"),
                                      object_pairs_hook=_unique_release_pairs)
                    if self._identity(os.fstat(stream.fileno())) != self._identity(before):
                        raise ValueError("changed")
                after = self._file_info(path)
                if after is None or self._identity(after) != self._identity(before):
                    raise ValueError("changed")
                if (not isinstance(item, dict) or set(item) != {
                        "schema", "id", "filename", "name", "description", "version", "sha256"}
                        or type(item["schema"]) is not int or item["schema"] != 1
                        or not isinstance(item["id"], str)
                        or not re.fullmatch(r"[a-z0-9_]{1,48}", item["id"])
                        or item["filename"] != "zz_mod_" + item["id"] + ".rpa"
                        or path.name != "zz_mod_" + item["id"] + ".lssb-mod.json"
                        or item["filename"].lower() in names
                        or "external_" + item["id"] in {row["id"] for row in self._builtin_catalog}
                        or not isinstance(item["version"], str)
                        or not re.fullmatch(r"[0-9]{1,5}\.[0-9]{1,5}\.[0-9]{1,5}(?:-[A-Za-z0-9][A-Za-z0-9.-]{0,31})?", item["version"])
                        or not isinstance(item["sha256"], str)
                        or not re.fullmatch(r"[a-f0-9]{64}", item["sha256"])):
                    raise ValueError("identity")
                for field, limit in (("name", 64), ("description", 160)):
                    text = item[field]
                    if (not isinstance(text, str) or not 0 < len(text) <= limit
                            or any(ord(c) < 32 or c in "{}[]" for c in text)):
                        raise ValueError("display text")
                names.add(item["filename"].lower())
                additions.append(dict(item, id="external_" + item["id"], external=True))
            except (OSError, ValueError, TypeError, UnicodeError, RecursionError, ManagerError):
                raise ManagerError("metadata", "Описание стороннего мода повреждено или недоступно: " + path.name) from None
        self.catalog = self._builtin_catalog + additions
        self.by_id = {item["id"]: item for item in self.catalog}

    @staticmethod
    def _is_reparse(info):
        return stat.S_ISLNK(info.st_mode) or bool(
            getattr(info, "st_file_attributes", 0) & 0x400)

    @staticmethod
    def _identity(info):
        return (info.st_size, info.st_mtime_ns, info.st_dev, info.st_ino)

    def _check_directory(self, path):
        # lstat every component: resolve() would conceal a junction/symlink.
        for part in reversed((path,) + tuple(path.parents)):
            try:
                info = part.lstat()
            except OSError:
                raise ManagerError("directory", "Папка игры или менеджера недоступна.") from None
            if self._is_reparse(info) or not stat.S_ISDIR(info.st_mode):
                raise ManagerError("unsafe_path", "Путь проходит через ссылку или неподходящую папку.")

    def _file_info(self, path):
        self._check_directory(path.parent)
        try:
            info = path.lstat()
        except FileNotFoundError:
            return None
        except OSError:
            raise ManagerError("file", "Не удалось проверить файл.") from None
        if self._is_reparse(info) or not stat.S_ISREG(info.st_mode):
            raise ManagerError("unsafe_file", "Обнаружена ссылка или файл неподходящего типа.")
        return info

    def _fingerprint(self, path, fresh=False):
        before = self._file_info(path)
        if before is None:
            return None
        identity = self._identity(before)
        cached = self._hash_cache.get(str(path))
        if not fresh and cached and cached[0] == identity:
            return cached[1]
        try:
            flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
            with os.fdopen(os.open(path, flags), "rb") as stream:
                if self._identity(os.fstat(stream.fileno())) != identity:
                    raise ManagerError("changed", "Файл изменился во время проверки.")
                release, release_error = None, False
                try:
                    release = read_release_footer(stream, before.st_size)
                except (ValueError, UnicodeError, TypeError, OverflowError, RecursionError, struct.error):
                    release_error = True
                stream.seek(0)
                header = stream.read(34)
                valid_header = bool(self._HEADER.fullmatch(header))
                if valid_header:
                    valid_header = 34 <= int(header[8:24], 16) < (release["archive_size"] if release else before.st_size)
                hasher = hashlib.sha256(header)
                # The signed archive is a prefix of the complete file. Copy the
                # SHA state exactly at its boundary instead of hashing it twice.
                prefix_end = release["archive_size"] if release else None
                position = len(header)
                prefix_digest = hasher.hexdigest() if prefix_end == position else None
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    if prefix_end is not None and position < prefix_end <= position + len(chunk):
                        split = prefix_end - position
                        hasher.update(chunk[:split])
                        prefix_digest = hasher.copy().hexdigest()
                        hasher.update(chunk[split:])
                    else:
                        hasher.update(chunk)
                    position += len(chunk)
                if release and prefix_digest != release["archive_sha256"]:
                    release, release_error = None, True
                if self._identity(os.fstat(stream.fileno())) != identity:
                    raise ManagerError("changed", "Файл изменился во время проверки.")
            after = self._file_info(path)
            if after is None or self._identity(after) != identity:
                raise ManagerError("changed", "Файл изменился во время проверки.")
        except OSError:
            raise ManagerError("read", "Не удалось прочитать архив мода.") from None
        result = {"digest": hasher.hexdigest(), "valid_header": valid_header,
                  "release": release, "release_error": release_error}
        self._hash_cache[str(path)] = (identity, result)
        return result

    @staticmethod
    def _automatic_component(item):
        return RELEASE_COMPONENTS.get(item["id"]) == item["filename"]

    def _recognized(self, item, result):
        if not result or not result["valid_header"] or result["release_error"]:
            return False
        if result["release"]:
            return (self._automatic_component(item)
                    and result["release"]["id"] == item["id"]
                    and result["release"]["filename"] == item["filename"])
        return result["digest"] == item["sha256"]

    def _control_path(self, kind):
        return self.data_dir / {"pending": "pending.json", "journal": "journal.json",
                                "result": "last_result.json"}[kind]

    def _ensure_data_dir(self):
        self._check_directory(self.game_dir)
        try:
            self.data_dir.mkdir(exist_ok=True)
        except OSError:
            raise ManagerError("write", "Не удалось создать папку настроек менеджера.") from None
        self._check_directory(self.data_dir)

    def _validate_actions(self, actions, historical=False):
        if not isinstance(actions, list) or not actions or len(actions) > (max(len(self._builtin_catalog), len(RELEASE_COMPONENTS)) + 64 if historical else len(self.catalog)):
            raise ManagerError("control", "План менеджера повреждён; файлы сохранены.")
        seen = set()
        for action in actions:
            if not isinstance(action, dict) or set(action) != {
                    "id", "enabled", "source", "destination", "sha256"}:
                raise ManagerError("control", "План менеджера повреждён; файлы сохранены.")
            key = action["id"]
            historical_external = (historical and isinstance(key, str)
                                   and re.fullmatch(r"external_[a-z0-9_]{1,48}", key))
            historical_builtin = historical and isinstance(key, str) and key in RELEASE_COMPONENTS
            if (not isinstance(key, str) or (key not in self.by_id and not historical_external and not historical_builtin) or key in seen
                    or type(action["enabled"]) is not bool):
                raise ManagerError("control", "План менеджера не соответствует каталогу.")
            seen.add(key)
            item = self.by_id.get(key) or {"filename": RELEASE_COMPONENTS[key] if historical_builtin else "zz_mod_" + key[9:] + ".rpa"}
            active, disabled = item["filename"], item["filename"] + ".disabled"
            source, target = (disabled, active) if action["enabled"] else (active, disabled)
            if (action["source"] != source or action["destination"] != target
                    or not isinstance(action["sha256"], str)
                    or not re.fullmatch(r"[a-f0-9]{64}", action["sha256"])
                    or (not historical and not item.get("external") and not self._automatic_component(item)
                        and action["sha256"] != item["sha256"])):
                raise ManagerError("control", "План менеджера не соответствует каталогу.")

    def _validate_document(self, value, kind):
        base = {"owner", "schema", "kind", "transaction_id", "created_at", "actions"}
        extra = {"pending": set(), "journal": {"phase", "completed"},
                 "result": {"outcome"}}[kind]
        if (not isinstance(value, dict) or set(value) != base | extra
                or value.get("owner") != self.OWNER or type(value.get("schema")) is not int
                or value.get("schema") != self.SCHEMA or value.get("kind") != kind
                or not isinstance(value.get("transaction_id"), str)
                or not re.fullmatch(r"[a-f0-9]{32}", value["transaction_id"])
                or not isinstance(value.get("created_at"), str)
                or not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", value["created_at"])):
            raise ManagerError("control", "Файл состояния менеджера неизвестен или повреждён; он сохранён.")
        # Completed receipts describe past files; they never authorize renames.
        # Pending plans and recovery journals must still match current digests.
        self._validate_actions(value["actions"], historical=(kind == "result"))
        if kind == "journal":
            completed = value["completed"]
            if (value["phase"] not in ("applying", "rolling_back", "recovery_required")
                    or not isinstance(completed, list)
                    or any(not isinstance(key, str) for key in completed)
                    or len(completed) != len(set(completed))
                    or not set(completed) <= {a["id"] for a in value["actions"]}):
                raise ManagerError("control", "Журнал менеджера повреждён; он сохранён.")
        if kind == "result" and value["outcome"] not in (
                "applied", "rolled_back", "recovery_required"):
            raise ManagerError("control", "Результат менеджера повреждён; он сохранён.")
        return value

    def _read_document(self, kind):
        if not os.path.lexists(self.data_dir):
            self._check_directory(self.game_dir)
            return None
        path = self._control_path(kind)
        info = self._file_info(path)
        if info is None:
            return None
        if info.st_size > self.MAX_JSON:
            raise ManagerError("control", "Файл состояния менеджера имеет неверный размер.")
        try:
            # Reject duplicate JSON keys rather than silently taking the last one.
            def unique_pairs(pairs):
                result = {}
                for key, item in pairs:
                    if key in result:
                        raise ValueError("duplicate key")
                    result[key] = item
                return result
            with path.open("rb") as stream:
                raw = stream.read(self.MAX_JSON + 1)
            if len(raw) > self.MAX_JSON:
                raise ValueError("oversized document")
            after = self._file_info(path)
            if after is None or self._identity(info) != self._identity(after):
                raise ManagerError("changed", "Состояние менеджера изменилось во время чтения.")
            value = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_pairs)
        except (OSError, ValueError, UnicodeError):
            raise ManagerError("control", "Файл состояния менеджера неизвестен или повреждён; он сохранён.") from None
        return self._validate_document(value, kind)

    def _write_document(self, value, expected=None, require_absent=False):
        kind = value["kind"]
        self._validate_document(value, kind)
        self._ensure_data_dir()
        current = self._read_document(kind)
        if require_absent and current is not None:
            raise ManagerError("conflict", "Другая операция менеджера уже началась.")
        if expected is not None and current != expected:
            raise ManagerError("changed", "Состояние менеджера изменено; запись остановлена.")
        path = self._control_path(kind)
        temporary = self.data_dir / ("." + kind + "." + uuid.uuid4().hex + ".tmp")
        created_identity = None
        try:
            with temporary.open("xb") as stream:
                created_identity = self._identity(os.fstat(stream.fileno()))
                stream.write((json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
                stream.flush()
                os.fsync(stream.fileno())
                created_identity = self._identity(os.fstat(stream.fileno()))
            if self._read_document(kind) != current:
                raise ManagerError("changed", "Состояние менеджера изменено; запись остановлена.")
            self._check_directory(self.data_dir)
            if current is None:
                self._rename(temporary, path)
            else:
                os.replace(temporary, path)
        except OSError:
            raise ManagerError("write", "Не удалось сохранить состояние менеджера.") from None
        finally:
            if created_identity is not None:
                try:
                    current_info = self._file_info(temporary)
                    if current_info and self._identity(current_info) == created_identity:
                        temporary.unlink()
                except (OSError, ManagerError):
                    pass

    def _remove_document(self, value):
        if self._read_document(value["kind"]) != value:
            raise ManagerError("changed", "Состояние менеджера изменено; удаление остановлено.")
        try:
            self._control_path(value["kind"]).unlink()
        except OSError:
            raise ManagerError("write", "Не удалось удалить подтверждённый файл состояния менеджера.") from None

    def _check_no_journal(self):
        if self._read_document("journal") is not None:
            raise ManagerError("recovery_required", "Предыдущее применение прервано. Нужна проверка файлов; переключение заблокировано.")

    def pending(self):
        return self._read_document("pending")

    def last_result(self):
        return self._read_document("result")

    def scan(self):
        self.status_error = None
        try:
            self._refresh_external_mods()
            self._check_no_journal()
            self.pending()
        except ManagerError as error:
            self.status_error = str(error)
        rows = []
        for item in self.catalog:
            row = dict(item, state="missing", can_toggle=False, enabled=None,
                       actual_path=None, digest=None, reason="Архив не найден.")
            try:
                self._check_incompatible(item)
                active = self.game_dir / item["filename"]
                disabled = self.game_dir / (item["filename"] + ".disabled")
                active_info, disabled_info = self._file_info(active), self._file_info(disabled)
                if active_info and disabled_info:
                    row.update(state="conflict", reason="Есть и включённая, и выключенная копия.")
                elif active_info or disabled_info:
                    enabled = active_info is not None
                    source = active if enabled else disabled
                    # Re-read automatic mods on refresh even when a copier retained
                    # size and timestamps. Actual rename always rechecks all bytes.
                    result = self._fingerprint(source, fresh=self._automatic_component(item) or item.get("external", False))
                    if result is None:
                        raise ManagerError("changed", "Архив исчез во время проверки.")
                    recognised = self._recognized(item, result)
                    if recognised and self._automatic_component(item) and result["release"]:
                        row.update(version=result["release"]["version"],
                                   sha256=result["digest"], recognition="signed-release")
                    elif recognised and item.get("external"):
                        row["recognition"] = "author-manifest"
                    row.update(state=("enabled" if enabled else "disabled") if recognised else "changed",
                               enabled=enabled, actual_path=str(source), digest=result["digest"],
                               can_toggle=recognised, reason="" if recognised else (
                                   "Архив повреждён или подпись выпуска недействительна."
                                   if result["release_error"] else "Архив изменён или его версия неизвестна."))
            except ManagerError as error:
                row.update(state="conflict", reason=str(error), can_toggle=False)
            if self.status_error:
                row.update(can_toggle=False, reason=self.status_error)
            rows.append(row)
        return rows

    def stage(self, desired):
        rows = {row["id"]: row for row in self.scan()}
        self._check_no_journal()
        self.pending()  # Never replace a corrupt or foreign pending file.
        if not isinstance(desired, dict) or any(
                key not in self.by_id or type(enabled) is not bool for key, enabled in desired.items()):
            raise ManagerError("selection", "Неверный выбор модов.")
        actions = []
        for item in self.catalog:
            key = item["id"]
            if key not in desired:
                continue
            row = rows[key]
            if not row["can_toggle"]:
                raise ManagerError("unavailable", row["reason"] or "Мод нельзя переключить.")
            if row["enabled"] == desired[key]:
                continue
            active, disabled = item["filename"], item["filename"] + ".disabled"
            source, target = (disabled, active) if desired[key] else (active, disabled)
            actions.append(dict(id=key, enabled=desired[key], source=source,
                                destination=target, sha256=row["digest"]))
        if not actions:
            self.cancel()
            return None
        pending = dict(owner=self.OWNER, schema=self.SCHEMA, kind="pending",
                       transaction_id=uuid.uuid4().hex,
                       created_at=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                       actions=actions)
        # Fresh verification when staging also catches edits with retained timestamps.
        self._preflight(actions)
        self._write_document(pending)
        return pending

    def cancel(self):
        self._check_no_journal()
        pending = self.pending()
        if pending is not None:
            self._remove_document(pending)
            return True
        return False

    def _check_incompatible(self, item):
        for name in item.get("incompatible_files", []):
            if self._file_info(self.game_dir / name) is not None:
                raise ManagerError("conflict", "Перенесите старый отдельный архив " + name + " из game в резервную папку и перезапустите игру.")

    def _preflight(self, actions, reverse=False):
        self._refresh_external_mods()
        self._validate_actions(actions)
        self._check_directory(self.game_dir)
        for action in actions:
            if not reverse:
                self._check_incompatible(self.by_id[action["id"]])
            source = self.game_dir / action["destination" if reverse else "source"]
            target = self.game_dir / action["source" if reverse else "destination"]
            if self._file_info(target) is not None:
                raise ManagerError("conflict", "Целевое имя уже занято; файлы сохранены.")
            result = self._fingerprint(source, fresh=True)
            if (not self._recognized(self.by_id[action["id"]], result)
                    or result["digest"] != action["sha256"]):
                raise ManagerError("changed", "Архив изменён или отсутствует; применение остановлено.")

    def _rename(self, source, target):
        if os.path.lexists(target):
            raise FileExistsError("destination exists")
        if os.name == "nt":
            # Windows os.rename is non-replacing, unlike os.replace.
            os.rename(source, target)
        else:
            # Exclusive hard-link creation provides non-replacement on POSIX too.
            os.link(source, target, follow_symlinks=False)
            try:
                os.unlink(source)
            except OSError:
                os.unlink(target)
                raise

    def _result(self, pending, outcome):
        result = dict(pending, kind="result", outcome=outcome)
        self._write_document(result)
        return result

    def apply_pending(self):
        """Call only at the end of the engine's exit, once RPA handles are closed."""
        self._check_no_journal()
        pending = self.pending()
        if pending is None:
            return None
        self._preflight(pending["actions"])
        # Validate the result slot before modifying any archives.
        self.last_result()
        journal = dict(pending, kind="journal", phase="applying", completed=[])
        self._write_document(journal, require_absent=True)
        completed = []
        try:
            if self.pending() != pending:
                raise ManagerError("changed", "План изменён; применение остановлено.")
            for action in pending["actions"]:
                self._preflight([action])
                self._rename(self.game_dir / action["source"], self.game_dir / action["destination"])
                completed.append(action)
                self._preflight([action], reverse=True)
                next_journal = dict(journal, completed=[a["id"] for a in completed])
                self._write_document(next_journal, expected=journal)
                journal = next_journal
            self._preflight(pending["actions"], reverse=True)
            result = self._result(pending, "applied")
        except (ManagerError, OSError):
            # Roll back only files demonstrably matching this transaction.
            rollback_ok = True
            try:
                next_journal = dict(journal, phase="rolling_back")
                self._write_document(next_journal, expected=journal)
                journal = next_journal
            except ManagerError:
                rollback_ok = False
            for action in reversed(completed):
                try:
                    self._preflight([action], reverse=True)
                    self._rename(self.game_dir / action["destination"], self.game_dir / action["source"])
                except (ManagerError, OSError):
                    rollback_ok = False
                    break
            if rollback_ok:
                try:
                    self._preflight(pending["actions"])
                    self._result(pending, "rolled_back")
                    self._remove_document(journal)
                except ManagerError:
                    rollback_ok = False
            if not rollback_ok:
                try:
                    next_journal = dict(journal, phase="recovery_required")
                    self._write_document(next_journal, expected=journal)
                    self._result(pending, "recovery_required")
                except ManagerError:
                    pass
                raise ManagerError("recovery_required", "Применение прервано. Журнал сохранён; нужна проверка файлов.") from None
            raise ManagerError("rolled_back", "Не удалось применить изменения. Исходное состояние восстановлено; план сохранён.") from None
        # If cleanup fails, leave the journal to block further mutations.
        try:
            self._remove_document(pending)
            self._remove_document(journal)
        except ManagerError:
            raise ManagerError("recovery_required", "Моды переключены, но журнал не закрыт. Нужна проверка файлов.") from None
        self._hash_cache.clear()
        return result


class ScanJob:
    """One read-only scan; publish its complete result via a thread-safe queue.

    The UI owns this object and polls it. The worker never calls the engine,
    changes store variables, stages a plan, or mutates game files.
    """
    def __init__(self, game_dir, catalog, factory=ManagerCore):
        import queue
        import threading
        self._results = queue.Queue(maxsize=1)
        self._thread = threading.Thread(target=self._run,
            args=(game_dir, [dict(item) for item in catalog], factory),
            name="LSSB mod validation", daemon=True)
        self._thread.start()

    def _run(self, game_dir, catalog, factory):
        try:
            controller = factory(game_dir, catalog)
            rows = controller.scan()
            issue = controller.status_error or ""
            choices = {row["id"]: row["enabled"] for row in rows if row["can_toggle"]}
            notice = ""
            if not issue:
                pending = controller.pending()
                if pending:
                    for action in pending["actions"]:
                        if action["id"] in choices:
                            choices[action["id"]] = action["enabled"]
                    notice = "Сохранённый выбор ещё не применён. Проверьте его перед выходом."
                else:
                    last = controller.last_result()
                    if last:
                        notice = ("Предыдущие изменения успешно применены." if last.get("outcome") == "applied"
                            else "Предыдущие изменения не применены. Проверьте состояние файлов.")
            result = dict(controller=controller, rows=rows, choices=choices, issue=issue, notice=notice)
        except Exception as exc:
            result = dict(controller=None, rows=[], choices={}, issue=str(exc), notice="")
        self._results.put(result)

    def poll(self):
        import queue
        try:
            return self._results.get_nowait()
        except queue.Empty:
            return None
