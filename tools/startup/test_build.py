"""Keep interpreter caches out of source copies and published RPAs."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import pickle
import sys
import tempfile
import unittest
from unittest.mock import patch
import zlib

SPEC = importlib.util.spec_from_file_location('build_under_test', Path(__file__).resolve().parents[1] / 'build.py')
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class BuildTests(unittest.TestCase):
    def test_python_caches_are_not_copied_or_packed(self):
        with tempfile.TemporaryDirectory(prefix='lssb-build-test-') as folder:
            root = Path(folder).resolve()
            self.assertTrue(root.is_relative_to(Path(tempfile.gettempdir()).resolve()))
            sources = root / 'mods/lssb_startup_fix/game'
            (sources / '__pycache__').mkdir(parents=True)
            (sources / '__pycache__/removed_module.cpython-312.pyc').write_bytes(b'stale')
            (sources / 'stale.pyc').write_bytes(b'stale')
            (sources / 'stale.pyo').write_bytes(b'stale')
            (sources / 'helper.py').write_text('value = 1\n')
            (sources / 'startup.rpy').write_text('init python:\n    value = 1\n')
            (root / 'components.json').write_text(json.dumps({'lssb_startup_fix':dict(version='1.2.0-own',archive='startup.rpa',id='startup_fast',name='Startup',description='test')}))
            for name in ('LICENSE', 'LICENSE_SCOPE.md', 'NOTICE'):
                (root / name).write_text('test')
            (root / 'LICENSES').mkdir()
            game = root / 'fake-game'
            (game / 'lib/py3-windows-x86_64').mkdir(parents=True)
            (game / 'lib/py3-windows-x86_64/python.exe').write_bytes(b'not executed')
            (game / 'LoSeSb.py').write_text('not executed')
            output = root / 'output'

            def compile_stub(args, **kwargs):
                project = Path(args[2])
                self.assertFalse((project / 'game/__pycache__').exists())
                self.assertFalse(list((project / 'game').rglob('*.pyc')))
                self.assertFalse(list((project / 'game').rglob('*.pyo')))
                (project / 'game/startup.rpyc').write_bytes(b'compiled test payload')

            argv = ['build.py', '--game-root', str(game), '--output', str(output), '--component', 'lssb_startup_fix', '--unsigned-mods']
            with patch.object(builder, 'ROOT', root), patch.object(sys, 'argv', argv), patch.object(builder.subprocess, 'run', side_effect=compile_stub), contextlib.redirect_stdout(io.StringIO()):
                builder.main()
            archive = (output / 'dist/game/startup.rpa').read_bytes()
            offset = int(archive[:34].split()[1], 16)
            index = pickle.loads(zlib.decompress(archive[offset:]))
            self.assertEqual(set(index), {'startup.rpyc', 'helper.py'})
            manifest = json.loads((output / 'dist/manifest.json').read_text())
            self.assertEqual(set(manifest['lssb_startup_fix']['files']), set(index))


if __name__ == '__main__':
    unittest.main()
