"""Unifying the archives must preserve old receipts and reject active duplicates."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from manager_core import ManagerCore, ManagerError, RELEASE_COMPONENTS


class CombinedMigrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = b'RPA-3.0 0000000000000022 4c535343\n' + b'unified fixture'
        self.active = self.root / RELEASE_COMPONENTS['localization_ru']
        self.active.write_bytes(self.data)
        self.legacy = self.root / RELEASE_COMPONENTS['visual_quality']
        self.item = dict(id='localization_ru', filename=self.active.name, name='Unified', version='1.89.0',
            sha256=hashlib.sha256(self.data).hexdigest(), incompatible_files=[self.legacy.name])

    def core(self):
        return ManagerCore(self.root, [self.item])

    def test_active_legacy_archive_blocks_toggle_without_changing_either_file(self):
        self.legacy.write_bytes(b'old visual archive')
        row = self.core().scan()[0]
        self.assertEqual(row['state'], 'conflict')
        self.assertFalse(row['can_toggle'])
        with self.assertRaises(ManagerError):self.core().stage({'localization_ru':False})
        self.assertEqual(self.active.read_bytes(), self.data)
        self.assertEqual(self.legacy.read_bytes(), b'old visual archive')

    def test_disabled_legacy_archive_does_not_block_unified_toggle(self):
        self.legacy.with_suffix('.rpa.disabled').write_bytes(b'old disabled archive')
        core = self.core()
        core.stage({'localization_ru':False})
        self.assertEqual(core.apply_pending()['outcome'], 'applied')
        self.assertEqual(self.active.with_suffix('.rpa.disabled').read_bytes(), self.data)

    def test_legacy_archive_added_after_staging_is_rechecked_before_rename(self):
        core = self.core()
        core.stage({'localization_ru':False})
        self.legacy.write_bytes(b'late duplicate')
        with self.assertRaises(ManagerError):core.apply_pending()
        self.assertEqual(self.active.read_bytes(), self.data)
        self.assertFalse(self.active.with_suffix('.rpa.disabled').exists())

    def test_invalid_conflict_path_is_rejected(self):
        for value in (['../other.rpa'], ['/other.rpa'], [self.active.name], 'other.rpa'):
            with self.subTest(value=value), self.assertRaises(ManagerError):
                ManagerCore(self.root, [dict(self.item, incompatible_files=value)])

    def old_visual_transaction(self):
        self.legacy.write_bytes(self.data)
        old = ManagerCore(self.root, [dict(self.item, incompatible_files=[]),
            dict(id='visual_quality', filename=self.legacy.name, name='Visual', version='1.7.0', sha256=hashlib.sha256(self.data).hexdigest())])
        old.stage({'visual_quality':False})
        return old

    def test_completed_receipt_for_retired_component_remains_readable(self):
        old = self.old_visual_transaction()
        receipt = old.apply_pending()
        core = self.core()
        self.assertEqual(core.last_result(), receipt)
        core.stage({'localization_ru':False})
        self.assertEqual(core.apply_pending()['outcome'], 'applied')

    def test_pending_plan_for_retired_component_is_still_rejected(self):
        self.old_visual_transaction()
        with self.assertRaises(ManagerError):self.core().pending()
        self.assertTrue(self.legacy.exists())

    def test_retired_receipt_cannot_reference_another_file(self):
        old = self.old_visual_transaction()
        receipt = old.apply_pending()
        receipt['actions'][0]['source'] = self.active.name
        old._control_path('result').write_text(json.dumps(receipt),encoding='utf-8')
        with self.assertRaises(ManagerError):self.core().last_result()
