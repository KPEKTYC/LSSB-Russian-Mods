"""Sign a first-party mod RPA without changing its Ren'Py index or contents.

The manager verifies a bounded footer using its embedded public key. Private
keys stay outside the repository and are needed only for official releases.
"""
import base64
import hashlib
import json
from pathlib import Path
import struct

from manager.manager_core import (
    RELEASE_KEY_ID, RELEASE_KEYS, RELEASE_MAGIC, RELEASE_MAX_JSON, RELEASE_COMPONENTS,
    read_release_footer, release_message,
)

DEFAULT_SIGNING_KEY = Path.home() / ".lssb-mods/signing/localization-release.pem"


def sign_archive(archive, version, key_path, key_id=RELEASE_KEY_ID, component="localization_ru"):
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding, rsa

    archive = Path(archive)
    if component not in RELEASE_COMPONENTS:
        raise ValueError("Only the three managed first-party components can be signed.")
    key = serialization.load_pem_private_key(Path(key_path).read_bytes(), password=None)
    if not isinstance(key, rsa.RSAPrivateKey):
        raise ValueError("Release signing requires an RSA key.")
    public = key.public_key().public_numbers()
    if RELEASE_KEYS.get(key_id) != (public.n, public.e):
        raise ValueError("Signing key does not match the manager's public verification key.")
    with archive.open("rb") as stream:
        if read_release_footer(stream, archive.stat().st_size) is not None:
            raise ValueError("Archive already has a release footer.")
        stream.seek(0)
        if not stream.read(34).startswith(b"RPA-3.0 "):
            raise ValueError("Expected an RPA-3.0 archive.")
        stream.seek(0)
        digest = hashlib.file_digest(stream, "sha256").hexdigest()
    payload = dict(schema=1 if component == "localization_ru" else 2,
                   owner="lssb-russian-mods", id=component,
                   filename=RELEASE_COMPONENTS[component], version=version,
                   archive_size=archive.stat().st_size, archive_sha256=digest)
    signature = key.sign(release_message(payload), padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()), salt_length=32), hashes.SHA256())
    envelope = dict(key_id=key_id, payload=payload, signature=base64.b64encode(signature).decode("ascii"))
    encoded = json.dumps(envelope, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")
    if len(encoded) > RELEASE_MAX_JSON:
        raise ValueError("Release metadata is too large.")
    footer = encoded + struct.pack(">I", len(encoded)) + RELEASE_MAGIC
    with archive.open("ab") as stream:
        stream.write(footer)
    with archive.open("rb") as stream:
        if read_release_footer(stream, archive.stat().st_size) != payload:
            raise ValueError("Release metadata readback failed.")
    return dict(key_id=key_id, payload=payload, algorithm="RSA-PSS-SHA256-salt32")
