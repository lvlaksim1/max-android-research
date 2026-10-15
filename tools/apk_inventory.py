#!/usr/bin/env python3
"""Verify and inventory a MAX APK; optionally extract all entries locally.

The program does not write back to the APK or contact any remote service.
"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile

EXPECTED_SHA256 = "e809176d6bf6ff69247274433ec170a5db8a5687a02a04299a78a2ae978119fc"

def digest_file(path):
    h = hashlib.sha256()
    with path.open("rb") as source:
        for part in iter(lambda: source.read(1024 * 1024), b""):
            h.update(part)
    return h.hexdigest()

def safe_relative(name):
    norm = PurePosixPath(name)
    if norm.is_absolute() or not norm.parts or ".." in norm.parts or "\\" in name:
        raise ValueError(f"Unsafe ZIP path: {name!r}")
    return Path(*norm.parts)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("apk", type=Path)
    p.add_argument("--index", type=Path, default=Path("work/files.json"))
    p.add_argument("--extract", type=Path, help="Optional local output folder (ignored by Git)")
    p.add_argument("--allow-other-hash", action="store_true",
                   help="Allow another APK (but never silently mistake it for the reference)")
    args = p.parse_args()
    sha = digest_file(args.apk)
    if sha != EXPECTED_SHA256 and not args.allow_other_hash:
        raise SystemExit(f"APK SHA-256 differs: {sha}; expected: {EXPECTED_SHA256}")
    listing = []
    with zipfile.ZipFile(args.apk) as archive:
        bad = archive.testzip()
        if bad:
            raise SystemExit(f"ZIP integrity error: {bad}")
        for item in archive.infolist():
            rel = safe_relative(item.filename)
            if item.is_dir():
                continue
            record = {"path": item.filename, "uncompressed_bytes": item.file_size,
                      "compressed_bytes": item.compress_size,
                      "crc32": f"{item.CRC:08x}"}
            listing.append(record)
            if args.extract:
                target = args.extract / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(item) as source, target.open("wb") as output:
                    while True:
                        chunk = source.read(1024 * 1024)
                        if not chunk: break
                        output.write(chunk)
    result = {"apk_sha256": sha, "reference_match": sha == EXPECTED_SHA256,
              "entry_count": len(listing), "files": listing}
    args.index.parent.mkdir(parents=True, exist_ok=True)
    args.index.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                          encoding="utf-8")
    print(f"SHA-256: {sha}; files: {len(listing)}; index: {args.index}")
    if args.extract: print(f"Extracted locally: {args.extract}")

if __name__ == "__main__":
    main()
