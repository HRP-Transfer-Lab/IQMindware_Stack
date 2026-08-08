#!/usr/bin/env python3
"""Build a deterministic IQ Mindware website import bundle."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RELEASE = ROOT / "website-release"
FILES = [
    "product-availability.json",
    "route-templates.json",
    "route-copy.json",
    "tests/website-route-cases.json",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True, help="Bundle version, e.g. 0.1.0-rc1")
    parser.add_argument("--output", default=None, help="Optional output directory")
    args = parser.parse_args()

    subprocess.run(
        ["python", str(RELEASE / "scripts" / "validate_website_release.py")],
        cwd=ROOT,
        check=True,
    )

    output = (
        Path(args.output)
        if args.output
        else ROOT / "dist" / f"website-v{args.version}"
    )
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    sums: list[str] = []
    for relative in FILES:
        source = RELEASE / relative
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        sums.append(f"{digest}  {relative}")

    (output / "SHA256SUMS").write_text("\n".join(sums) + "\n", encoding="utf-8")

    source_manifest = json.loads((RELEASE / "manifest.json").read_text(encoding="utf-8"))
    built_manifest = {
        **source_manifest,
        "bundle_version": args.version,
        "built_at": datetime.now(timezone.utc).isoformat(),
        "validation_status": "passed",
        "sha256sums_file": "SHA256SUMS",
    }
    (output / "release-manifest.json").write_text(
        json.dumps(built_manifest, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Built website bundle: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
