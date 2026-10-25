"""Signed-prefix and whole-file hashes remain exact at read boundaries."""
import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest import mock
import manager_core
from manager_core import ManagerCore

class HashBoundaryTests(unittest.TestCase):
    def test_signed_prefix_and_trailer_boundaries(self):
        chunk=1024*1024
        for length in [34,35,34+chunk-1,34+chunk,35+chunk,34+2*chunk+97]:
            with self.subTest(length=length),tempfile.TemporaryDirectory() as tmp:
                p=Path(tmp)/'test.rpa'
                raw=b'RPA-3.0 0000000000000022 12345678\n'+b'a'*(length-34)+b'trailer'
                p.write_bytes(raw)
                release=dict(archive_size=length,archive_sha256=hashlib.sha256(raw[:length]).hexdigest())
                core=ManagerCore(tmp,[])
                with mock.patch.object(manager_core,'read_release_footer',return_value=release):
                    found=core._fingerprint(p,fresh=True)
                    self.assertEqual(found['digest'],hashlib.sha256(raw).hexdigest())
                    self.assertEqual(found['release'],release)
                    self.assertFalse(found['release_error'])
                    p.write_bytes(raw[:-1]+b'X')
                    footer_change=core._fingerprint(p,fresh=True)
                    self.assertEqual(footer_change['release'],release)
                    self.assertNotEqual(footer_change['digest'],found['digest'])
                    if length>34:
                        p.write_bytes(raw[:34]+b'X'+raw[35:])
                        changed=core._fingerprint(p,fresh=True)
                        self.assertTrue(changed['release_error'])
                        self.assertIsNone(changed['release'])
