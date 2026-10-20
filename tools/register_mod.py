"""Create the companion metadata used by the in-game manager for an author's mod.

The filename namespace opts in to management without claiming publisher trust.
Re-run for each update, then distribute the RPA and JSON together.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re


def manifest(archive, mod_id, name, version, description):
    archive = Path(archive)
    if not re.fullmatch(r"[a-z0-9_]{1,48}", mod_id) or archive.name != "zz_mod_" + mod_id + ".rpa":
        raise ValueError("Use zz_mod_<id>.rpa; id must contain 1-48 lowercase letters, digits or underscores.")
    if not re.fullmatch(r"[0-9]{1,5}\.[0-9]{1,5}\.[0-9]{1,5}(?:-[A-Za-z0-9][A-Za-z0-9.-]{0,31})?", version):
        raise ValueError("Version must use major.minor.patch, optionally with a release suffix.")
    for text, limit in ((name, 64), (description, 160)):
        if not 0 < len(text) <= limit or any(ord(c) < 32 or c in "{}[]" for c in text):
            raise ValueError("Use short plain display text without markup or control characters.")
    with archive.open("rb") as stream:
        if not re.fullmatch(br"RPA-3\.0 [0-9a-fA-F]{16} [0-9a-fA-F]{8}\n", stream.read(34)):
            raise ValueError("Expected an RPA-3.0 archive.")
        stream.seek(0)
        digest = hashlib.file_digest(stream, "sha256").hexdigest()
    return dict(schema=1, id=mod_id, filename=archive.name, name=name,
                description=description, version=version, sha256=digest)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--id", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--description", required=True)
    args = parser.parse_args()
    data = manifest(args.archive, args.id, args.name, args.version, args.description)
    path = args.archive.with_suffix(".lssb-mod.json")
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    temporary.replace(path)
    print(path)


if __name__ == "__main__":
    main()
