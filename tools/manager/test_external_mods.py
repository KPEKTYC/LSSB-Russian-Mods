"""Third-party opt-in discovery and update lifecycle without publisher keys."""
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from build import pack
from register_mod import manifest
from manager_core import ManagerCore, ManagerError


class ExternalModTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.game = Path(self.temp.name)
        self.path = self.game / "zz_mod_weather.rpa"
        self.meta = self.path.with_suffix(".lssb-mod.json")
        self.core = ManagerCore(self.game, [])
        self.update("1.0.0")

    def update(self, version, disabled=False):
        path = self.path.with_name(self.path.name + ".disabled") if disabled else self.path
        pack({"fixture": version.encode()}, path)
        data = dict(schema=1, id="weather", filename=self.path.name, name="Weather",
                    description="An author's mod", version=version,
                    sha256=hashlib.sha256(path.read_bytes()).hexdigest())
        self.meta.write_text(json.dumps(data), encoding="utf-8")
        return data

    def test_discovery_updates_and_disabled_state_with_same_controller(self):
        with mock.patch("pickle.loads", side_effect=AssertionError("no code execution")):
            for version in ("1.0.0", "99.0.0"):
                self.update(version)
                row = self.core.scan()[0]
                self.assertEqual((row["version"], row["recognition"]), (version, "author-manifest"))
                self.core.stage({"external_weather": False})
                self.core.apply_pending()
                self.update("100.0.0", disabled=True)
                row = self.core.scan()[0]
                self.assertEqual((row["enabled"], row["can_toggle"], row["version"]), (False, True, "100.0.0"))
                self.core.stage({"external_weather": True})
                self.core.apply_pending()

    def test_archive_only_update_requires_matching_metadata(self):
        self.core.scan()
        pack({"fixture": b"changed"}, self.path)
        self.assertFalse(self.core.scan()[0]["can_toggle"])
        self.update("2.0.0")
        self.assertTrue(self.core.scan()[0]["can_toggle"])

    def test_valid_update_after_staging_cannot_change_planned_bytes(self):
        self.core.stage({"external_weather": False})
        self.update("2.0.0")
        with self.assertRaises(ManagerError):
            self.core.apply_pending()
        self.assertTrue(self.path.exists())
        self.core.cancel()
        self.assertEqual(self.core.scan()[0]["version"], "2.0.0")

    def test_conflict_keeps_both_copies(self):
        self.update("2.0.0", disabled=True)
        self.assertEqual(self.core.scan()[0]["state"], "conflict")
        self.assertTrue(self.path.exists())

    def test_bad_identity_path_markup_and_types_are_blocked(self):
        original = self.meta.read_text()
        for field, value in (("filename", "scripts.rpa"), ("filename", "../foreign.rpa"),
                             ("filename", "zzzzzz_lssb_localization_ru.rpa"),
                             ("id", "../weather"), ("id", []), ("schema", True),
                             ("name", "{a=evil}click{/a}"), ("description", "a\nb"),
                             ("version", "not a version"), ("sha256", "0")):
            with self.subTest(field=field):
                data = json.loads(original)
                data[field] = value
                self.meta.write_text(json.dumps(data))
                self.assertEqual(self.core.scan(), [])
                self.assertIsNotNone(self.core.status_error)
        self.meta.write_text(original)
        self.assertTrue(self.core.scan()[0]["can_toggle"])

    def test_duplicate_json_and_excessive_size_are_blocked(self):
        self.meta.write_text(self.meta.read_text().replace('"schema": 1', '"schema": 1,"schema": 1'))
        self.assertEqual(self.core.scan(), [])
        self.assertIsNotNone(self.core.status_error)
        self.meta.write_text(" " * 8193)
        self.assertEqual(self.core.scan(), [])
        self.assertIsNotNone(self.core.status_error)

    def test_metadata_filename_is_bound_to_identity(self):
        self.meta.rename(self.game / "foreign.lssb-mod.json")
        self.assertEqual(self.core.scan(), [])
        self.assertIsNotNone(self.core.status_error)

    def test_historical_receipt_does_not_require_removed_external_mod(self):
        self.core.stage({"external_weather": False})
        self.core.apply_pending()
        receipt = self.core.last_result()
        self.meta.unlink()
        restarted = ManagerCore(self.game, [])
        self.assertEqual(restarted.scan(), [])
        self.assertIsNone(restarted.status_error)
        self.assertEqual(restarted.last_result(), receipt)

    def test_generator_matches_discovery_format_without_signing_key(self):
        data = manifest(self.path, "weather", "Weather", "1.2.3", "Custom weather")
        self.meta.write_text(json.dumps(data))
        self.assertEqual(self.core.scan()[0]["version"], "1.2.3")
        with self.assertRaises(ValueError):
            manifest(self.path, "other", "Weather", "1.2.3", "Custom weather")

    def test_manifest_cannot_take_over_builtin_catalogue_entry(self):
        builtin = dict(id="external_weather", filename="zz_builtin.rpa", version="1.0.0", sha256="0" * 64)
        with self.assertRaises(ManagerError):
            ManagerCore(self.game, [builtin])


if __name__ == "__main__":
    unittest.main()
