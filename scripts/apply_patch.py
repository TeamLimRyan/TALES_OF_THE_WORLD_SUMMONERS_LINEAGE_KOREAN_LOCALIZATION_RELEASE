#!/usr/bin/env python3
"""Apply the supported xdelta patch and verify every file hash."""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATCH = ROOT / "Tales_of_the_World_Summoners_Lineage_KO.xdelta"
SOURCE_SIZE = 8_388_608
SOURCE_SHA256 = "b41c293fc0ed6111b7a37d960d9cd0c685e5d521a4739e0e2eaa7ff6186cfdd3"
PATCH_SIZE = 237_005
PATCH_SHA256 = "550aa8ac8f176171ec524825f9fe6c2a19f0a3237ae78c7edc0a62f57157ba11"
TARGET_SIZE = 8_937_092
TARGET_SHA256 = "43c315b28b54c944aa862c838d54c464c4c66bdaa1214ce739113ba6b8860be4"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def require_file(path: Path, size: int, digest: str, label: str) -> None:
    if not path.is_file():
        raise SystemExit(f"{label} 파일이 없습니다: {path}")
    actual_size = path.stat().st_size
    actual_digest = sha256_file(path)
    if actual_size != size or actual_digest != digest:
        raise SystemExit(
            f"{label} 검증 실패\n"
            f"  경로: {path}\n"
            f"  크기: {actual_size} (예상 {size})\n"
            f"  SHA-256: {actual_digest}\n"
            f"  예상값: {digest}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="서머너즈 리니지 한국어 xdelta 적용기")
    parser.add_argument("source", type=Path, help="지원 대상 일본판 원본 ROM")
    parser.add_argument("output", type=Path, nargs="?", default=Path("summoners_lineage_ko.gba"))
    parser.add_argument("--xdelta", default="xdelta3", help="xdelta3 실행 파일 또는 경로")
    parser.add_argument("--force", action="store_true", help="기존 출력 파일 덮어쓰기")
    args = parser.parse_args()

    source = args.source.resolve()
    output = args.output.resolve()
    xdelta = shutil.which(args.xdelta) or (str(Path(args.xdelta).resolve()) if Path(args.xdelta).is_file() else None)
    if xdelta is None:
        raise SystemExit("xdelta3를 찾을 수 없습니다. PATH에 추가하거나 --xdelta로 경로를 지정하십시오.")
    if output.exists() and not args.force:
        raise SystemExit(f"출력 파일이 이미 있습니다: {output}\n덮어쓰려면 --force를 사용하십시오.")

    require_file(source, SOURCE_SIZE, SOURCE_SHA256, "원본 ROM")
    require_file(PATCH, PATCH_SIZE, PATCH_SHA256, "xdelta 패치")
    output.parent.mkdir(parents=True, exist_ok=True)

    temp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(prefix=output.name + ".", suffix=".tmp", dir=output.parent, delete=False) as handle:
            temp_path = Path(handle.name)
        subprocess.run(
            [xdelta, "-f", "-d", "-s", str(source), str(PATCH), str(temp_path)],
            check=True,
        )
        require_file(temp_path, TARGET_SIZE, TARGET_SHA256, "패치 결과")
        os.replace(temp_path, output)
        temp_path = None
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"xdelta3 적용 실패: 종료 코드 {exc.returncode}") from exc
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)

    print(f"PASS: {output}")
    print(f"SIZE: {TARGET_SIZE}")
    print(f"SHA-256: {TARGET_SHA256}")


if __name__ == "__main__":
    main()
