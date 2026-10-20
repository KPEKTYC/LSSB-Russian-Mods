"""Verify the saved snapshot, exclusion policy, and manager catalogue."""
import ast
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

def main():
    expected = json.loads((ROOT / "provenance/snapshot.json").read_text(encoding="utf-8"))
    for relative, sha256 in expected["files"].items():
        path = ROOT / relative
        assert path.is_file(), relative
        assert hashlib.sha256(path.read_bytes()).hexdigest() == sha256, relative
    actual = {p.relative_to(ROOT).as_posix() for folder in ("mods", "work-in-progress", "tools/manager")
              for p in (ROOT / folder).rglob("*") if p.is_file() and "__pycache__" not in p.parts}
    assert actual == set(expected["files"]), ("unrecorded or missing files", actual ^ set(expected["files"]))
    for relative in actual:
        assert "daerty" not in relative.lower(), relative
        path = ROOT / relative
        assert path.suffix.lower() not in {".rpa", ".rpyc", ".save", ".log"}, relative
        if path.suffix in {".rpy", ".py"} or path.name.endswith(".rpy.in"):
            text = path.read_text(encoding="utf-8")
            assert not re.search(r"daerty|Đã dời", text, re.I), relative
            assert not re.search(r"(?:ghp_|github_pat_|sk-proj-)[A-Za-z0-9_]{16,}", text), relative
    manager = (ROOT / "mods/lssb_mod_manager/game/zz_lssb_mod_manager.rpy").read_text(encoding="utf-8")
    # Source construction must retain exactly the three first-party entries.
    for name in ("localization_ru", "visual_quality", "startup_fast"):
        assert "'id': '" + name + "'" in manager, name
    assert manager.count("'filename':") == 3
    for path in (ROOT / "tools").rglob("*.py"):
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    print(f"PASS: {len(actual)} snapshot files; four own mods; no wiki payloads or wiki translation code.")

if __name__ == "__main__":
    main()
