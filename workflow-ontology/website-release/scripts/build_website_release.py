#!/usr/bin/env python3
"""Build a deterministic IQ Mindware website import bundle."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RELEASE = ROOT / "website-release"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True, help="Bundle version, e.g. 0.1.0-rc2")
    parser.add_argument("--output", default=None, help="Optional output directory")
    parser.add_argument(
        "--source-commit",
        default=os.environ.get("GITHUB_SHA", "UNSPECIFIED"),
        help="Immutable source commit for the bundle manifest",
    )
    args = parser.parse_args()

    subprocess.run(
        ["python", str(RELEASE / "scripts" / "validate_website_release.py")],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        ["python", str(RELEASE / "scripts" / "run_website_route_cases.py")],
        cwd=ROOT,
        check=True,
    )

    source_manifest = json.loads((RELEASE / "manifest.json").read_text(encoding="utf-8"))
    files = source_manifest["included_files"]

    output = (
        Path(args.output)
        if args.output
        else ROOT / "dist" / f"website-v{args.version}"
    )
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    sums: list[str] = []
    file_hashes: dict[str, str] = {}
    for relative in files:
        source = RELEASE / relative
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        file_hashes[relative] = digest
        sums.append(f"{digest}  {relative}")

    (output / "SHA256SUMS").write_text("\n".join(sums) + "\n", encoding="utf-8")

    built_manifest = {
        **source_manifest,
        "bundle_version": args.version,
        "source_commit": args.source_commit,
        "built_at": datetime.now(timezone.utc).isoformat(),
        "validation_status": "passed",
        "sha256sums_file": "SHA256SUMS",
        "file_hashes": file_hashes,
    }
    (output / "release-manifest.json").write_text(
        json.dumps(built_manifest, indent=2) + "\n",
        encoding="utf-8",
    )

    lock_template = json.loads(
        (RELEASE / "ontology-lock.template.json").read_text(encoding="utf-8")
    )
    lock_template["commercial_release"] = source_manifest["release_id"]
    lock_template["source_commits"]["commercial"] = args.source_commit
    lock_template["file_hashes"] = file_hashes
    (output / "ontology-lock.generated.json").write_text(
        json.dumps(lock_template, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Built website bundle: {output}")
    print("The generated lock remains unapproved until all review roles sign off.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
