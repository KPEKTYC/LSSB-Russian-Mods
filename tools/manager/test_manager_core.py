"""Behavioural transaction tests; fixtures are isolated temporary archives."""
import hashlib
import json
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock

from manager_core import ManagerCore, ManagerError


class ManagerCoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.game = Path(self.temp.name) / "game"
        self.game.mkdir()
        self.catalog = []
        for index in range(2):
            data = b"RPA-3.0 0000000000000022 12345678\n" + (b"fixture" + bytes([index])) * 10
            filename = "zz_test_" + str(index) + ".rpa"
            (self.game / filename).write_bytes(data)
            self.catalog.append(dict(id="mod_" + str(index), name="Мод " + str(index),
                                     filename=filename, version="1.0.0",
                                     sha256=hashlib.sha256(data).hexdigest()))
        self.core = ManagerCore(self.game, self.catalog)

    def path(self, index=0, disabled=False):
        return self.game / (self.catalog[index]["filename"] + (".disabled" if disabled else ""))

    def write_control(self, kind, value):
        self.core.data_dir.mkdir(exist_ok=True)
        path = self.core._control_path(kind)
        path.write_text(json.dumps(value), encoding="utf-8")
        return path

    def test_scan_and_stage_do_not_change_archives(self):
        before = {p.name: p.read_bytes() for p in self.game.iterdir()}
        self.assertEqual([r["state"] for r in self.core.scan()], ["enabled", "enabled"])
        pending = self.core.stage({"mod_0": False})
        self.assertEqual(pending, self.core.pending())
        self.assertEqual(pending["actions"][0]["destination"], self.path(disabled=True).name)
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.game.iterdir() if p.is_file()})

    def test_disable_then_enable_and_report(self):
        self.core.stage({"mod_0": False, "mod_1": False})
        result = self.core.apply_pending()
        self.assertEqual(result["outcome"], "applied")
        self.assertIsNone(self.core.pending())
        self.assertFalse(self.core._control_path("journal").exists())
        self.assertEqual([r["state"] for r in self.core.scan()], ["disabled", "disabled"])
        self.core.stage({"mod_0": True})
        self.assertEqual(self.core.apply_pending()["outcome"], "applied")
        self.assertTrue(self.path().exists())
        self.assertFalse(self.path(disabled=True).exists())
        report = self.core.last_result()
        self.assertNotIn(str(self.game), json.dumps(report))
        self.assertEqual(report["actions"][0]["source"], self.path(disabled=True).name)

    def test_completed_receipt_survives_archive_update_and_next_transaction(self):
        self.core.stage({"mod_0": False})
        old_result = self.core.apply_pending()
        receipt_path = self.core._control_path("result")
        receipt_bytes = receipt_path.read_bytes()
        updated_bytes = self.path(disabled=True).read_bytes() + b"updated payload"
        self.path(disabled=True).write_bytes(updated_bytes)
        catalog = [dict(item) for item in self.catalog]
        catalog[0].update(version="2.0.0", sha256=hashlib.sha256(updated_bytes).hexdigest())
        updated = ManagerCore(self.game, catalog)
        self.assertTrue(all(row["can_toggle"] for row in updated.scan()))
        self.assertEqual(updated.last_result(), old_result)
        self.assertEqual(receipt_path.read_bytes(), receipt_bytes)
        updated.stage({"mod_0": True})
        self.assertEqual(updated.apply_pending()["outcome"], "applied")
        self.assertEqual(self.path().read_bytes(), updated_bytes)
        self.assertEqual(updated.last_result()["actions"][0]["sha256"], catalog[0]["sha256"])

    def test_update_keeps_pending_and_journal_digest_checks_strict(self):
        pending = self.core.stage({"mod_0": False})
        catalog = [dict(item) for item in self.catalog]
        catalog[0]["sha256"] = "a" * 64
        updated = ManagerCore(self.game, catalog)
        before = self.path().read_bytes()
        with self.assertRaises(ManagerError):
            updated.pending()
        with self.assertRaises(ManagerError):
            updated.apply_pending()
        self.assertEqual(self.path().read_bytes(), before)
        journal = dict(pending, kind="journal", phase="applying", completed=[])
        self.write_control("journal", journal)
        with self.assertRaises(ManagerError):
            updated._read_document("journal")
        self.assertEqual(self.path().read_bytes(), before)

    def test_historical_receipt_still_rejects_foreign_paths_ids_and_bad_hashes(self):
        self.core.stage({"mod_0": False})
        result = self.core.apply_pending()
        for field, value in (("sha256", "not-a-hash"), ("sha256", None),
                             ("id", "foreign"), ("source", "../outside.rpa"),
                             ("destination", "other.rpa")):
            with self.subTest(field=field, value=value):
                changed = dict(result, actions=[dict(result["actions"][0], **{field: value})])
                self.write_control("result", changed)
                with self.assertRaises(ManagerError):
                    self.core.last_result()

    def test_unchanged_selection_cancels_pending(self):
        self.core.stage({"mod_0": False})
        self.assertIsNone(self.core.stage({"mod_0": True}))
        self.assertIsNone(self.core.pending())
        self.assertFalse(self.core.cancel())

    def test_duplicate_and_versioned_backups(self):
        self.path(disabled=True).write_bytes(self.path().read_bytes())
        self.assertEqual(self.core.scan()[0]["state"], "conflict")
        with self.assertRaises(ManagerError):
            self.core.stage({"mod_0": False})
        self.path(disabled=True).unlink()
        backup = self.game / (self.path().name + ".abcdef.disabled")
        backup.write_bytes(b"backup")
        self.core.stage({"mod_0": False})
        self.core.apply_pending()
        self.assertEqual(backup.read_bytes(), b"backup")

    def test_modified_hash_and_bad_header_not_toggleable(self):
        self.path().write_bytes(self.path().read_bytes() + b"changed")
        self.assertEqual(self.core.scan()[0]["state"], "changed")
        with self.assertRaises(ManagerError):
            self.core.stage({"mod_0": False})
        invalid = b"invalid archive data" * 4
        self.path().write_bytes(invalid)
        self.catalog[0]["sha256"] = hashlib.sha256(invalid).hexdigest()
        another = ManagerCore(self.game, self.catalog)
        self.assertEqual(another.scan()[0]["state"], "changed")

    def test_fresh_apply_hash_catches_preserved_timestamp(self):
        self.core.stage({"mod_0": False})
        old_stat = self.path().stat()
        old = self.path().read_bytes()
        self.path().write_bytes(old[:-1] + b"X")
        os.utime(self.path(), ns=(old_stat.st_atime_ns, old_stat.st_mtime_ns))
        with self.assertRaises(ManagerError) as result:
            self.core.apply_pending()
        self.assertEqual(result.exception.code, "changed")
        self.assertFalse(self.path(disabled=True).exists())
        self.assertEqual(self.path().read_bytes(), old[:-1] + b"X")

    def test_entire_plan_preflight_prevents_partial_change(self):
        self.core.stage({"mod_0": False, "mod_1": False})
        self.path(1, True).write_bytes(b"unknown destination")
        with self.assertRaises(ManagerError):
            self.core.apply_pending()
        self.assertTrue(self.path().exists())
        self.assertFalse(self.path(disabled=True).exists())
        self.assertEqual(self.path(1, True).read_bytes(), b"unknown destination")
        self.assertFalse(self.core._control_path("journal").exists())

    def test_mid_operation_failure_rolls_back(self):
        self.core.stage({"mod_0": False, "mod_1": False})
        rename = self.core._rename
        def fail_second_archive(source, target):
            if source == self.path(1):
                raise PermissionError("fixture locked")
            return rename(source, target)
        with mock.patch.object(self.core, "_rename", side_effect=fail_second_archive):
            with self.assertRaises(ManagerError) as result:
                self.core.apply_pending()
        self.assertEqual(result.exception.code, "rolled_back")
        self.assertEqual([r["state"] for r in self.core.scan()], ["enabled", "enabled"])
        self.assertIsNotNone(self.core.pending())
        self.assertIsNone(self.core._read_document("journal"))
        self.assertEqual(self.core.last_result()["outcome"], "rolled_back")

    def test_failed_rollback_preserves_modified_archive_and_journal(self):
        self.core.stage({"mod_0": False, "mod_1": False})
        rename = self.core._rename
        def fail_and_change_first(source, target):
            if source == self.path(1):
                self.path(0, True).write_bytes(b"external change")
                raise PermissionError("fixture locked")
            return rename(source, target)
        with mock.patch.object(self.core, "_rename", side_effect=fail_and_change_first):
            with self.assertRaises(ManagerError) as result:
                self.core.apply_pending()
        self.assertEqual(result.exception.code, "recovery_required")
        self.assertEqual(self.path(0, True).read_bytes(), b"external change")
        self.assertTrue(self.path(1).exists())
        self.assertEqual(self.core.last_result()["outcome"], "recovery_required")
        self.assertTrue(all(not r["can_toggle"] for r in self.core.scan()))
        with self.assertRaises(ManagerError):
            self.core.cancel()

    def test_interrupted_journal_never_auto_resumes(self):
        pending = self.core.stage({"mod_0": False, "mod_1": False})
        journal = dict(pending, kind="journal", phase="applying", completed=[])
        self.write_control("journal", journal)
        self.path().rename(self.path(disabled=True))
        new_core = ManagerCore(self.game, self.catalog)
        self.assertTrue(all(not r["can_toggle"] for r in new_core.scan()))
        self.assertIn("прервано", new_core.status_error)
        with self.assertRaises(ManagerError):
            new_core.apply_pending()
        self.assertTrue(self.path(disabled=True).exists())
        self.assertTrue(self.path(1).exists())

    def test_corrupt_foreign_control_files_are_preserved(self):
        path = self.write_control("pending", {"owner": "somebody-else"})
        before = path.read_bytes()
        for action in (self.core.pending, self.core.cancel, self.core.apply_pending,
                       lambda: self.core.stage({"mod_0": False})):
            with self.assertRaises(ManagerError):
                action()
            self.assertEqual(path.read_bytes(), before)
        self.assertTrue(all(not r["can_toggle"] for r in self.core.scan()))

    def test_traversal_and_wrong_digest_in_pending_rejected(self):
        pending = self.core.stage({"mod_0": False})
        for field, value in (("source", "../outside.rpa"), ("destination", "C:/outside.rpa"),
                             ("sha256", "0" * 64), ("enabled", 0)):
            changed = json.loads(json.dumps(pending))
            changed["actions"][0][field] = value
            path = self.write_control("pending", changed)
            before = path.read_bytes()
            with self.assertRaises(ManagerError):
                self.core.apply_pending()
            self.assertEqual(path.read_bytes(), before)
        self.assertTrue(self.path().exists())

    def test_catalog_traversal_and_case_duplicate_rejected(self):
        for filename in ("../unsafe.rpa", "x/unsafe.rpa", "C:unsafe.rpa", "x\\unsafe.rpa"):
            with self.assertRaises(ManagerError):
                ManagerCore(self.game, [dict(self.catalog[0], filename=filename)])
        with self.assertRaises(ManagerError):
            ManagerCore(self.game, [self.catalog[0], dict(self.catalog[1],
                        filename=self.catalog[0]["filename"].upper().replace(".RPA", ".rpa"))])

    def test_json_duplicate_keys_rejected(self):
        path = self.core.data_dir
        path.mkdir()
        self.core._control_path("pending").write_text('{"owner":"x","owner":"y"}', encoding="utf-8")
        with self.assertRaises(ManagerError):
            self.core.pending()

    def test_foreign_result_blocks_apply_before_changes(self):
        self.core.stage({"mod_0": False})
        result_path = self.write_control("result", {"owner": "foreign"})
        old = result_path.read_bytes()
        with self.assertRaises(ManagerError):
            self.core.apply_pending()
        self.assertEqual(result_path.read_bytes(), old)
        self.assertTrue(self.path().exists())
        self.assertFalse(self.core._control_path("journal").exists())

    def test_symlink_file_or_parent_is_rejected(self):
        outside = Path(self.temp.name) / "outside.rpa"
        outside.write_bytes(self.path().read_bytes())
        self.path().unlink()
        try:
            self.path().symlink_to(outside)
        except OSError:
            self.skipTest("Windows symlink creation requires permission")
        self.assertEqual(self.core.scan()[0]["state"], "conflict")
        self.assertFalse(self.core.scan()[0]["can_toggle"])
        alias = Path(self.temp.name) / "alias"
        alias.symlink_to(self.game, target_is_directory=True)
        with self.assertRaises(ManagerError):
            ManagerCore(alias, self.catalog)

    def test_unknown_directory_at_archive_path_is_conflict(self):
        self.path().unlink()
        self.path().mkdir()
        row = self.core.scan()[0]
        self.assertEqual(row["state"], "conflict")
        self.assertFalse(row["can_toggle"])

    def test_windows_reparse_attribute_is_rejected(self):
        real_lstat = Path.lstat
        target = self.path()
        def lstat(path, *args, **kwargs):
            info = real_lstat(path, *args, **kwargs)
            if path == target:
                return SimpleNamespace(st_mode=info.st_mode, st_file_attributes=0x400)
            return info
        with mock.patch.object(Path, "lstat", lstat):
            row = self.core.scan()[0]
            self.assertEqual(row["state"], "conflict")
            self.assertFalse(row["can_toggle"])

    def test_data_directory_reparse_attribute_is_rejected(self):
        self.core.data_dir.mkdir()
        real_lstat = Path.lstat
        target = self.core.data_dir
        def lstat(path, *args, **kwargs):
            info = real_lstat(path, *args, **kwargs)
            if path == target:
                return SimpleNamespace(st_mode=info.st_mode, st_file_attributes=0x400)
            return info
        with mock.patch.object(Path, "lstat", lstat):
            with self.assertRaises(ManagerError):
                self.core.stage({"mod_0": False})
        self.assertTrue(self.path().exists())

    def test_destination_created_during_apply_is_never_overwritten(self):
        self.core.stage({"mod_0": False})
        rename = self.core._rename
        def intruder(source, target):
            if source == self.path():
                target.write_bytes(b"another program created this")
            return rename(source, target)
        with mock.patch.object(self.core, "_rename", side_effect=intruder):
            with self.assertRaises(ManagerError) as result:
                self.core.apply_pending()
        self.assertEqual(result.exception.code, "recovery_required")
        self.assertTrue(self.path().exists())
        self.assertEqual(self.path(disabled=True).read_bytes(), b"another program created this")

    def test_pending_created_during_atomic_save_is_preserved(self):
        rename = self.core._rename
        pending_path = self.core._control_path("pending")
        def intruder(source, target):
            if target == pending_path:
                target.write_bytes(b"unknown state file")
            return rename(source, target)
        with mock.patch.object(self.core, "_rename", side_effect=intruder):
            with self.assertRaises(ManagerError):
                self.core.stage({"mod_0": False})
        self.assertEqual(pending_path.read_bytes(), b"unknown state file")
        self.assertTrue(self.path().exists())

    def test_competing_journal_is_not_replaced(self):
        pending = self.core.stage({"mod_0": False})
        competitor = dict(pending, kind="journal", phase="applying", completed=[],
                          transaction_id="a" * 32)
        write_document = self.core._write_document
        def competitor_starts(value, **kwargs):
            if value["kind"] == "journal":
                self.write_control("journal", competitor)
            return write_document(value, **kwargs)
        with mock.patch.object(self.core, "_write_document", side_effect=competitor_starts):
            with self.assertRaises(ManagerError):
                self.core.apply_pending()
        self.assertEqual(self.core._read_document("journal"), competitor)
        self.assertTrue(self.path().exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
