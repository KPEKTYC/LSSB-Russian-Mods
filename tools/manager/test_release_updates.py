"""Automatic release discovery and byte-pinned transaction regression tests."""
import base64
import hashlib
import json
import os
from pathlib import Path
import struct
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from build import pack, release_signing_key
import manager_core as core_module
from manager_core import ManagerCore, ManagerError
import release_metadata as signer
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa


class ReleaseUpdateTests(unittest.TestCase):
    KEY_ID = "ephemeral-test-release-key"
    FILENAME = "zzzzzz_lssb_localization_ru.rpa"

    @classmethod
    def setUpClass(cls):
        cls.key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public = cls.key.public_key().public_numbers()
        for registry in (core_module.RELEASE_KEYS, signer.RELEASE_KEYS):
            patcher = mock.patch.dict(registry, {cls.KEY_ID: (public.n, public.e)})
            patcher.start()
            cls.addClassCleanup(patcher.stop)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.game = Path(self.temp.name) / "game"
        self.game.mkdir()
        self.key_path = Path(self.temp.name) / "ephemeral-key.pem"
        self.key_path.write_bytes(self.key.private_bytes(
            serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()))
        self.path = self.game / self.FILENAME
        pack({"translation.rpyc": b"legacy payload"}, self.path)
        self.legacy = self.path.read_bytes()
        self.catalog = [dict(id="localization_ru", name="Русская локализация",
                             filename=self.FILENAME, version="1.85.0-own",
                             sha256=hashlib.sha256(self.legacy).hexdigest())]
        self.core = ManagerCore(self.game, self.catalog)

    def signed(self, version="2.00.0-own", payload=b"new payload", path=None):
        path = path or self.path
        pack({"translation.rpyc": payload}, path)
        signer.sign_archive(path, version, self.key_path, self.KEY_ID)
        return path.read_bytes()

    def envelope(self):
        raw = self.path.read_bytes()
        tail = len(core_module.RELEASE_MAGIC) + 4
        size = struct.unpack(">I", raw[-tail:-len(core_module.RELEASE_MAGIC)])[0]
        return raw[:-tail-size], json.loads(raw[-tail-size:-tail])

    def rewrite(self, envelope, prefix=None):
        prefix = self.envelope()[0] if prefix is None else prefix
        data = json.dumps(envelope, sort_keys=True, separators=(",", ":")).encode()
        self.path.write_bytes(prefix + data + struct.pack(">I", len(data)) + core_module.RELEASE_MAGIC)

    def sign_envelope(self, envelope):
        signature = self.key.sign(core_module.release_message(envelope["payload"]),
                                  padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=32), hashes.SHA256())
        envelope["signature"] = base64.b64encode(signature).decode()

    def assert_blocked(self):
        before = self.path.read_bytes()
        self.assertFalse(self.core.scan()[0]["can_toggle"])
        with self.assertRaises(ManagerError):
            self.core.stage({"localization_ru": False})
        self.assertEqual(self.path.read_bytes(), before)
        self.assertFalse(self.path.with_name(self.FILENAME + ".disabled").exists())

    def test_same_manager_accepts_future_versions_and_pins_actual_bytes(self):
        for version in ("1.86.0-own", "99.00.0-test", "100.0.0-own"):
            raw = self.signed(version)
            row = self.core.scan()[0]
            self.assertTrue(row["can_toggle"])
            self.assertEqual(row["version"], version)
            self.assertEqual(row["recognition"], "signed-release")
            plan = self.core.stage({"localization_ru": False})
            self.assertEqual(plan["actions"][0]["sha256"], hashlib.sha256(raw).hexdigest())
            self.assertEqual(self.core.apply_pending()["outcome"], "applied")
            restarted = ManagerCore(self.game, self.catalog)
            self.assertEqual(restarted.scan()[0]["version"], version)
            self.assertFalse(restarted.scan()[0]["enabled"])
            restarted.stage({"localization_ru": True})
            restarted.apply_pending()
            self.assertEqual(self.path.read_bytes(), raw)
        self.assertEqual(self.catalog[0]["version"], "1.85.0-own")

    def test_disabled_archive_update_is_discovered_without_enabling_it(self):
        self.core.stage({"localization_ru": False})
        self.core.apply_pending()
        disabled = self.path.with_name(self.FILENAME + ".disabled")
        raw = self.signed("9.00.0-own", path=disabled)
        row = self.core.scan()[0]
        self.assertTrue(row["can_toggle"])
        self.assertFalse(row["enabled"])
        self.assertEqual(row["version"], "9.00.0-own")
        self.assertFalse(self.path.exists())
        self.core.stage({"localization_ru": True})
        self.core.apply_pending()
        self.assertEqual(self.path.read_bytes(), raw)

    def test_legacy_exact_hash_works_but_unsigned_replacement_is_blocked(self):
        self.assertTrue(self.core.scan()[0]["can_toggle"])
        pack({"translation.rpyc": b"unsigned update"}, self.path)
        self.assert_blocked()

    def test_payload_corruption_and_stripped_or_appended_footer_are_blocked(self):
        valid = self.signed()
        for transform in (lambda b: b[:40] + bytes([b[40] ^ 1]) + b[41:],
                          lambda b: b[:-len(core_module.RELEASE_MAGIC)],
                          lambda b: b + b"trailing bytes"):
            with self.subTest(transform=transform):
                self.path.write_bytes(transform(valid))
                self.assert_blocked()

    def test_version_or_digest_cannot_be_forged_without_the_release_key(self):
        valid = self.signed()
        for field, value in (("version", "777.0.0-own"), ("archive_sha256", "0" * 64)):
            with self.subTest(field=field):
                self.path.write_bytes(valid)
                prefix, envelope = self.envelope()
                envelope["payload"][field] = value
                self.rewrite(envelope, prefix)
                self.assert_blocked()

    def test_unknown_key_and_wrong_signature_encoding_or_scheme_are_blocked(self):
        valid = self.signed()
        variants = [("key_id", "unknown"), ("signature", "not base64"),
                    ("signature", base64.b64encode(b"\0" * 256).decode()),
                    ("signature", base64.b64encode(b"\xff" * 256).decode())]
        for field, value in variants:
            with self.subTest(field=field, value=value[:30]):
                self.path.write_bytes(valid)
                prefix, envelope = self.envelope()
                envelope[field] = value
                self.rewrite(envelope, prefix)
                self.assert_blocked()
        for scheme in (padding.PKCS1v15(), padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=20)):
            self.path.write_bytes(valid)
            prefix, envelope = self.envelope()
            signature = self.key.sign(core_module.release_message(envelope["payload"]), scheme, hashes.SHA256())
            envelope["signature"] = base64.b64encode(signature).decode()
            self.rewrite(envelope, prefix)
            self.assert_blocked()

    def test_signed_invalid_identity_schema_size_or_version_is_rejected(self):
        valid = self.signed()
        for field, value in (("id", "other_mod"), ("filename", "../foreign.rpa"),
                             ("owner", "foreign"), ("schema", 2), ("schema", True),
                             ("archive_size", True), ("archive_size", 0),
                             ("version", "{b}fake"), ("version", "1.0.0\n"),
                             ("version", None), ("archive_sha256", "bad")):
            with self.subTest(field=field, value=value):
                self.path.write_bytes(valid)
                prefix, envelope = self.envelope()
                envelope["payload"][field] = value
                self.sign_envelope(envelope)
                self.rewrite(envelope, prefix)
                self.assert_blocked()

    def test_duplicate_json_keys_and_unbounded_lengths_are_rejected(self):
        self.signed()
        prefix, envelope = self.envelope()
        data = json.dumps(envelope, separators=(",", ":")).encode().replace(
            b'"schema":1', b'"schema":1,"schema":1')
        self.path.write_bytes(prefix + data + struct.pack(">I", len(data)) + core_module.RELEASE_MAGIC)
        self.assert_blocked()
        self.path.write_bytes(prefix + b"{}" + struct.pack(">I", 0xffffffff) + core_module.RELEASE_MAGIC)
        self.assert_blocked()

    def test_no_pickle_index_is_executed_during_recognition(self):
        self.signed()
        with mock.patch("pickle.loads", side_effect=AssertionError("must not unpickle an archive")):
            self.assertTrue(self.core.scan()[0]["can_toggle"])

    def test_other_components_do_not_gain_automatic_trust(self):
        self.signed()
        catalog = [dict(self.catalog[0], id="visual_quality")]
        self.assertFalse(ManagerCore(self.game, catalog).scan()[0]["can_toggle"])

    def optional_core(self, component):
        path = self.game / core_module.RELEASE_COMPONENTS[component]
        pack({"fixture.rpyc": b"old optional mod"}, path)
        catalog = [dict(id=component, filename=path.name, version="1.0.0",
                        sha256=hashlib.sha256(path.read_bytes()).hexdigest())]
        return path, ManagerCore(self.game, catalog)

    def optional_signed(self, path, component, version):
        pack({"fixture.rpyc": b"updated optional mod"}, path)
        signer.sign_archive(path, version, self.key_path, self.KEY_ID, component=component)
        return path.read_bytes()

    def test_optional_updates_active_disabled_and_repeated_with_same_manager(self):
        for component in ("visual_quality", "startup_fast"):
            with self.subTest(component=component):
                path, core = self.optional_core(component)
                self.assertTrue(core.scan()[0]["can_toggle"])
                for version in ("99.0.0-test", "100.0.0-test"):
                    raw = self.optional_signed(path, component, version)
                    row = core.scan()[0]
                    self.assertEqual((row["version"], row["recognition"], row["can_toggle"]),
                                     (version, "signed-release", True))
                    core.stage({component: False})
                    self.assertEqual(core.apply_pending()["outcome"], "applied")
                    disabled = path.with_name(path.name + ".disabled")
                    self.assertEqual(disabled.read_bytes(), raw)
                    self.optional_signed(disabled, component, "101.0.0-test")
                    row = core.scan()[0]
                    self.assertEqual((row["version"], row["enabled"], row["can_toggle"]),
                                     ("101.0.0-test", False, True))
                    core.stage({component: True})
                    core.apply_pending()
                self.assertEqual(core.catalog[0]["version"], "1.0.0")
                core._control_path("result").unlink()

    def test_optional_updates_reject_cross_component_substitution_even_if_catalog_hash_matches(self):
        for component in ("visual_quality", "startup_fast"):
            path, core = self.optional_core(component)
            other = "startup_fast" if component == "visual_quality" else "visual_quality"
            raw = self.optional_signed(path, other, "99.0.0-test")
            core.catalog[0]["sha256"] = hashlib.sha256(raw).hexdigest()
            self.assertFalse(core.scan()[0]["can_toggle"])
            with self.assertRaises(ManagerError):
                core.stage({component: False})

    def test_optional_updates_keep_integrity_conflict_and_byte_pinned_plan_checks(self):
        for component in ("visual_quality", "startup_fast"):
            path, core = self.optional_core(component)
            raw = self.optional_signed(path, component, "99.0.0-test")
            core.stage({component: False})
            self.optional_signed(path, component, "100.0.0-test")
            with self.assertRaises(ManagerError):
                core.apply_pending()
            core.cancel()
            path.write_bytes(raw[:40] + bytes([raw[40] ^ 1]) + raw[41:])
            self.assertFalse(core.scan()[0]["can_toggle"])
            path.write_bytes(raw)
            disabled = path.with_name(path.name + ".disabled")
            disabled.write_bytes(raw)
            self.assertEqual(core.scan()[0]["state"], "conflict")
            disabled.unlink()
            pack({"fixture.rpyc": b"unsigned replacement"}, path)
            self.assertFalse(core.scan()[0]["can_toggle"])

    def test_optional_refresh_checks_same_size_and_timestamp(self):
        for component in ("visual_quality", "startup_fast"):
            path, core = self.optional_core(component)
            first = self.optional_signed(path, component, "99.0.0-test")
            self.assertEqual(core.scan()[0]["version"], "99.0.0-test")
            info = path.stat()
            second = self.optional_signed(path, component, "98.0.0-test")
            self.assertEqual(len(first), len(second))
            os.utime(path, ns=(info.st_atime_ns, info.st_mtime_ns))
            self.assertEqual(core.scan()[0]["version"], "98.0.0-test")

    def test_three_signed_components_share_one_transaction(self):
        self.signed()
        catalogs = list(self.catalog)
        for component in ("visual_quality", "startup_fast"):
            path, core = self.optional_core(component)
            catalogs.extend(core.catalog)
            self.optional_signed(path, component, "99.0.0-test")
        core = ManagerCore(self.game, catalogs)
        for enabled in (False, True):
            core.stage({item["id"]: enabled for item in catalogs})
            self.assertEqual(core.apply_pending()["outcome"], "applied")
            self.assertTrue(all(row["can_toggle"] and row["enabled"] == enabled for row in core.scan()))

    def test_signer_rejects_unmanaged_components_before_modifying_archive(self):
        before = self.path.read_bytes()
        for component in ("wiki", "mod_manager", "unknown"):
            with self.assertRaises(ValueError):
                signer.sign_archive(self.path, "1.0.0", self.key_path, self.KEY_ID, component=component)
            self.assertEqual(self.path.read_bytes(), before)

    def test_duplicate_enabled_and_disabled_copies_are_not_merged_implicitly(self):
        self.signed()
        disabled = self.path.with_name(self.FILENAME + ".disabled")
        self.signed("3.0.0-own", path=disabled)
        before = (self.path.read_bytes(), disabled.read_bytes())
        row = self.core.scan()[0]
        self.assertEqual(row["state"], "conflict")
        self.assertFalse(row["can_toggle"])
        self.assertEqual((self.path.read_bytes(), disabled.read_bytes()), before)

    def test_update_after_staging_cannot_change_the_planned_bytes(self):
        self.signed("2.00.0-own", b"version two")
        self.core.stage({"localization_ru": False})
        pending_path = self.core._control_path("pending")
        pending = pending_path.read_bytes()
        replacement = self.signed("3.00.0-own", b"version three")
        with self.assertRaises(ManagerError):
            self.core.apply_pending()
        self.assertEqual(pending_path.read_bytes(), pending)
        self.assertEqual(self.path.read_bytes(), replacement)
        self.assertFalse(self.core._control_path("journal").exists())
        self.core.cancel()
        self.assertEqual(self.core.scan()[0]["version"], "3.00.0-own")

    def test_completed_receipt_survives_automatic_update(self):
        self.signed()
        self.core.stage({"localization_ru": False})
        self.core.apply_pending()
        receipt_path = self.core._control_path("result")
        before = receipt_path.read_bytes()
        disabled = self.path.with_name(self.FILENAME + ".disabled")
        self.signed("9.00.0-own", path=disabled)
        self.assertTrue(self.core.scan()[0]["can_toggle"])
        self.assertEqual(receipt_path.read_bytes(), before)
        self.assertIsNotNone(self.core.last_result())
        self.core.stage({"localization_ru": True})
        self.assertEqual(self.core.apply_pending()["outcome"], "applied")

    def test_mixed_transaction_rolls_back_the_signed_update_on_later_failure(self):
        self.signed()
        other = self.game / "zz_other_mod.rpa"
        pack({"fixture": b"other"}, other)
        catalog = self.catalog + [dict(id="other_mod", filename=other.name, version="1.0.0",
                                      sha256=hashlib.sha256(other.read_bytes()).hexdigest())]
        core = ManagerCore(self.game, catalog)
        core.stage({"localization_ru": False, "other_mod": False})
        original = self.path.read_bytes()
        rename = core._rename
        def locked(source, target):
            if source == other:
                raise PermissionError("fixture locked")
            return rename(source, target)
        with mock.patch.object(core, "_rename", side_effect=locked):
            with self.assertRaises(ManagerError) as error:
                core.apply_pending()
        self.assertEqual(error.exception.code, "rolled_back")
        self.assertEqual(self.path.read_bytes(), original)
        self.assertIsNone(core._read_document("journal"))
        self.assertTrue(all(row["enabled"] for row in core.scan()))

    def test_signed_updates_do_not_bypass_an_interrupted_journal(self):
        self.signed()
        pending = self.core.stage({"localization_ru": False})
        journal = dict(pending, kind="journal", phase="applying", completed=[])
        self.core._control_path("journal").write_text(json.dumps(journal), encoding="utf-8")
        self.signed("8.0.0-own")
        row = ManagerCore(self.game, self.catalog).scan()[0]
        self.assertEqual(row["version"], "8.0.0-own")
        self.assertFalse(row["can_toggle"])
        with self.assertRaises(ManagerError):
            self.core.apply_pending()

    def test_refresh_detects_replacement_with_preserved_size_and_timestamp(self):
        first = self.signed("2.00.0-own", b"same length 1")
        self.assertEqual(self.core.scan()[0]["version"], "2.00.0-own")
        old_stat = self.path.stat()
        second = self.signed("3.00.0-own", b"same length 2")
        self.assertEqual(len(first), len(second))
        os.utime(self.path, ns=(old_stat.st_atime_ns, old_stat.st_mtime_ns))
        self.assertEqual(self.core.scan()[0]["version"], "3.00.0-own")

    def test_forged_pending_cannot_rename_unsigned_or_unrelated_archives(self):
        self.signed()
        pending = self.core.stage({"localization_ru": False})
        pack({"translation.rpyc": b"unsigned foreign file"}, self.path)
        pending["actions"][0]["sha256"] = hashlib.sha256(self.path.read_bytes()).hexdigest()
        self.core._control_path("pending").write_text(json.dumps(pending), encoding="utf-8")
        with self.assertRaises(ManagerError):
            self.core.apply_pending()
        self.assertTrue(self.path.exists())

    def test_signature_is_verified_by_independent_cryptography_implementation(self):
        self.signed()
        _, envelope = self.envelope()
        self.key.public_key().verify(base64.b64decode(envelope["signature"]),
            core_module.release_message(envelope["payload"]),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=32), hashes.SHA256())
        self.assertTrue(self.core.scan()[0]["can_toggle"])

    def test_signer_rejects_a_different_key_and_double_signing(self):
        self.signed()
        before = self.path.read_bytes()
        with self.assertRaises(ValueError):
            signer.sign_archive(self.path, "3.0.0-own", self.key_path, self.KEY_ID)
        self.assertEqual(self.path.read_bytes(), before)
        with self.assertRaises(ValueError):
            signer.sign_archive(self.path, "3.0.0-own", self.key_path, signer.RELEASE_KEY_ID)

    def test_missing_publisher_key_requires_explicit_local_unsigned_build(self):
        with mock.patch.object(signer, "DEFAULT_SIGNING_KEY", self.game / "missing.pem"):
            with self.assertRaises(FileNotFoundError):
                release_signing_key()
            self.assertIsNone(release_signing_key(unsigned=True))
            self.assertEqual(release_signing_key(self.key_path), self.key_path)
            with self.assertRaises(ValueError):
                release_signing_key(self.key_path, unsigned=True)


if __name__ == "__main__":
    unittest.main()
