#!/usr/bin/env python3
"""Verify public-repository patch metadata and forbid game images."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "STATUS.json"
FORBIDDEN = {".gba", ".sav", ".srm", ".state", ".ss0", ".ss1"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    status = json.loads(STATUS.read_text(encoding="utf-8"))
    patch = ROOT / status["patch"]["path"]
    errors: list[str] = []
    if not patch.is_file():
        errors.append(f"missing patch: {patch.relative_to(ROOT)}")
    else:
        if patch.stat().st_size != status["patch"]["size"]:
            errors.append("patch size mismatch")
        if sha256_file(patch) != status["patch"]["sha256"]:
            errors.append("patch SHA-256 mismatch")
    forbidden = [path.relative_to(ROOT) for path in ROOT.rglob("*") if path.is_file() and path.suffix.lower() in FORBIDDEN]
    if forbidden:
        errors.append("forbidden game/save files: " + ", ".join(map(str, forbidden)))
    if errors:
        raise SystemExit("FAIL\n" + "\n".join(f"- {error}" for error in errors))
    print("PASS: patch metadata matches and no ROM/save files are tracked")


if __name__ == "__main__":
    main()
