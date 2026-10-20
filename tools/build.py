"""Build our four RPA archives using the user's installed Ren'Py runtime.

Reads the game runtime only. Does not install, launch gameplay, or alter saves.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import pickle
import shutil
import subprocess
import zlib

ROOT = Path(__file__).resolve().parent.parent


def copy_license_documents(destination):
    """Keep licensing scope and attribution beside packaged components."""
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    for name in ("LICENSE", "LICENSE_SCOPE.md", "NOTICE"):
        shutil.copy2(ROOT / name, destination / name)
    shutil.copytree(ROOT / "LICENSES", destination / "LICENSES")

def digest(data):
    return hashlib.sha256(data).hexdigest()

def pack(files, target):
    data = bytearray(b" " * 34)
    index = {}
    key = 0x4C535343
    for name, blob in sorted(files.items()):
        index[name] = [(len(data) ^ key, len(blob) ^ key)]
        data.extend(blob)
    offset = len(data)
    data.extend(zlib.compress(pickle.dumps(index, protocol=2), 9))
    data[:34] = f"RPA-3.0 {offset:016x} {key:08x}\n".encode()
    target.write_bytes(data)

def manager_source(catalog, version):
    template = (ROOT / "tools/manager/runtime.rpy.in").read_text(encoding="utf-8")
    core = (ROOT / "tools/manager/manager_core.py").read_text(encoding="utf-8")
    return template.replace("@CORE_SOURCE@", repr(core)).replace("@CATALOG@", repr(catalog)).replace("@VERSION@", version)


def release_signing_key(explicit=None, unsigned=False):
    if unsigned:
        if explicit:
            raise ValueError("Choose signed or unsigned mods.")
        return None
    from release_metadata import DEFAULT_SIGNING_KEY
    path = Path(explicit) if explicit else DEFAULT_SIGNING_KEY
    if not path.is_file():
        raise FileNotFoundError("Release signing key is missing. For a local build use --unsigned-mods and its matching manager.")
    return path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game-root", required=True, type=Path)
    parser.add_argument("--output", type=Path, default=ROOT / "build/own-mods")
    parser.add_argument("--signing-key", type=Path,
                        help="Private RSA release key outside the repository (official mod updates).")
    parser.add_argument("--unsigned-mods", "--unsigned-localization", dest="unsigned_mods", action="store_true",
                        help="Local build without an automatic-update signature; its matching manager still works.")
    args = parser.parse_args()
    assert not (args.signing_key and args.unsigned_mods), "Choose signed or unsigned mods."
    signing_key = release_signing_key(args.signing_key, args.unsigned_mods)
    game_root = args.game_root.resolve()
    output = args.output.resolve()
    assert not output.exists(), "Choose a fresh output directory."
    assert not output.is_relative_to(game_root), "Build outside the installed game."
    runtime = game_root / "lib/py3-windows-x86_64/python.exe"
    entry = game_root / "LoSeSb.py"
    assert runtime.is_file() and entry.is_file(), "A Windows LSSB installation with its Ren'Py runtime is required."
    specs = json.loads((ROOT / "components.json").read_text(encoding="utf-8"))
    destination = output / "dist/game"
    destination.mkdir(parents=True)
    catalog = []
    manifests = {}
    for component, spec in specs.items():
        project = output / component
        sources = ROOT / "mods" / component / "game"
        shutil.copytree(sources, project / "game")
        if component == "lssb_mod_manager":
            (project / "game/zz_lssb_mod_manager.rpy").write_text(manager_source(catalog, spec["version"]), encoding="utf-8")
        environment = dict(os.environ, SDL_VIDEODRIVER="dummy", SDL_AUDIODRIVER="dummy",
                           PYTHONIOENCODING="utf-8", RENPY_MULTIPERSISTENT=str(project / "multipersistent"))
        with (project / "compile.log").open("wb") as log:
            subprocess.run([str(runtime), str(entry), str(project), "compile", "--savedir", str(project / "saves")],
                           env=environment, stdout=log, stderr=subprocess.STDOUT, check=True,
                           creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        files = {}
        for source in sorted(sources.rglob("*")):
            if not source.is_file():
                continue
            relative = source.relative_to(sources).as_posix()
            built = project / "game" / relative
            if source.suffix == ".rpy":
                built = built.with_suffix(".rpyc")
                relative += "c"
            assert built.is_file(), relative
            assert "daerty" not in relative.lower(), relative
            files[relative] = built.read_bytes()
        archive = destination / spec["archive"]
        pack(files, archive)
        release_metadata = None
        if component != "lssb_mod_manager" and not args.unsigned_mods:
            from release_metadata import sign_archive
            release_metadata = sign_archive(archive, spec["version"], signing_key, component=spec["id"])
            print("Mod release signed for automatic recognition by existing managers.", flush=True)
        elif component != "lssb_mod_manager":
            print("Local unsigned mod: use the matching manager from this build.", flush=True)
        archive_hash = digest(archive.read_bytes())
        manifests[component] = dict(version=spec["version"], archive=spec["archive"], sha256=archive_hash,
                                    files={n: digest(b) for n, b in files.items()},
                                    validation_status="compiled; gameplay validation required")
        if release_metadata:
            manifests[component]["release_metadata"] = release_metadata
        if component != "lssb_mod_manager":
            catalog.append(dict(id=spec["id"], name=spec["name"], description=spec["description"],
                                version=spec["version"], filename=spec["archive"], sha256=archive_hash))
        print(component, archive_hash, flush=True)
    (output / "dist/manifest.json").write_text(json.dumps(manifests, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    copy_license_documents(output / "dist")
    print("Compiled all four mods. No files installed.")

if __name__ == "__main__":
    main()
