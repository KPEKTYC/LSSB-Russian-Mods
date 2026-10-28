"""A combined build must not silently replace shared scripts or omit visuals."""
from pathlib import Path
import importlib.util
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("lssb_build", Path(__file__).parents[1] / "build.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class CombinedBuildTests(unittest.TestCase):
    def make(self, root, component, name, data):
        target = root / "mods" / component / "game" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    def test_shared_identical_script_is_included_once_with_both_payloads(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.make(root, "text", "guard.rpy", b"same guard")
            self.make(root, "visual", "guard.rpy", b"same guard")
            self.make(root, "text", "translation.rpy", b"translation")
            self.make(root, "visual", "images/hd.png", b"image")
            result = build.collect_sources("text", {"sources": ["text", "visual"]}, root)
            self.assertEqual(set(result), {"guard.rpy", "translation.rpy", "images/hd.png"})

    def test_conflicting_shared_script_rejects_build(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.make(root, "text", "guard.rpy", b"first guard")
            self.make(root, "visual", "guard.rpy", b"different guard")
            with self.assertRaisesRegex(ValueError, "Conflicting combined-mod source"):
                build.collect_sources("text", {"sources": ["text", "visual"]}, root)

    def test_missing_visual_tree_rejects_build(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.make(root, "text", "translation.rpy", b"translation")
            with self.assertRaises(FileNotFoundError):
                build.collect_sources("text", {"sources": ["text", "visual"]}, root)
