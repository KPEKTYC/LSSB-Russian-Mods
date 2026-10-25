"""Background validation must never block the UI or weaken fresh archive checks."""
import threading
import unittest
from manager_core import ScanJob

class FakeCore:
    status_error = ''
    plan = None
    result = None
    def __init__(self, game_dir, catalog):
        self.game_dir = game_dir
        self.catalog = catalog
    def scan(self):
        return [dict(id='visual_quality', enabled=True, can_toggle=True)]
    def pending(self):
        return self.plan
    def last_result(self):
        return self.result

class ScanJobTests(unittest.TestCase):
    def completed(self, factory):
        job = ScanJob('.', [], factory=factory)
        job._thread.join(3)
        self.assertFalse(job._thread.is_alive())
        result = job.poll()
        self.assertIsNotNone(result)
        self.assertIsNone(job.poll())
        return result

    def test_slow_scan_does_not_block_caller(self):
        entered = threading.Event()
        release = threading.Event()
        class Slow(FakeCore):
            def scan(self):
                entered.set()
                if not release.wait(3):
                    raise RuntimeError('test timeout')
                return super().scan()
        job = ScanJob('.', [], factory=Slow)
        try:
            self.assertTrue(entered.wait(2))
            self.assertIsNone(job.poll())
            self.assertTrue(job._thread.daemon)
        finally:
            release.set()
            job._thread.join(3)
        self.assertEqual(job.poll()['choices'], {'visual_quality': True})

    def test_fresh_controller_for_each_job(self):
        a = self.completed(FakeCore)
        b = self.completed(FakeCore)
        self.assertIsNot(a['controller'], b['controller'])

    def test_pending_choice_preserved(self):
        class Pending(FakeCore):
            plan = {'actions': [dict(id='visual_quality', enabled=False)]}
        result = self.completed(Pending)
        self.assertFalse(result['choices']['visual_quality'])
        self.assertTrue(result['notice'])

    def test_failure_publishes_no_stale_controller_or_rows(self):
        class Broken(FakeCore):
            def scan(self):
                raise OSError('archive changed during verification')
        result = self.completed(Broken)
        self.assertIsNone(result['controller'])
        self.assertFalse(result['rows'])
        self.assertFalse(result['choices'])
        self.assertIn('archive changed', result['issue'])

    def test_recovery_error_prevents_pending_read(self):
        class Recovery(FakeCore):
            status_error = 'recovery required'
            def pending(self):
                raise AssertionError('must not inspect pending after recovery error')
        result = self.completed(Recovery)
        self.assertEqual(result['issue'], 'recovery required')
        self.assertIsNotNone(result['controller'])

    def test_worker_does_not_modify_input_catalog(self):
        catalog = [dict(id='original')]
        class Mutates(FakeCore):
            def scan(self):
                self.catalog[0]['id'] = 'worker'
                return super().scan()
        job = ScanJob('.', catalog, factory=Mutates)
        job._thread.join(3)
        self.assertIsNotNone(job.poll())
        self.assertEqual(catalog, [dict(id='original')])

if __name__ == '__main__':
    unittest.main()
