#!/usr/bin/env python3
"""Build a deterministic release bundle after registry validation."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FILES = [
    "ontology/niches.json",
    "ontology/workflow-archetypes.json",
    "ontology/workflow-stages.json",
    "ontology/demand-dimensions.json",
    "ontology/friction-signatures.json",
    "ontology/intervention-loci.json",
    "ontology/outcome-measures.json",
    "mappings/demand-function-mappings.json",
    "mappings/governance-profiles.json",
    "mappings/workflow-supports.json",
    "evidence/evidence-sources.json",
    "evidence/evidence-claims.json",
    "evidence/measurement-registry.json",
    "evidence/training-fit-mappings.json",
]


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "UNKNOWN"


def count_records(relative: str) -> int:
    data: dict[str, Any] = json.loads((ROOT / relative).read_text(encoding="utf-8"))
    records = data.get("records")
    if isinstance(records, list):
        return len(records)
    if relative.endswith("demand-function-mappings.json"):
        return len(data.get("mappings", []))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True, help="Release version, e.g. 0.1.0")
    parser.add_argument("--output", default=None, help="Optional output directory")
    args = parser.parse_args()

    subprocess.run(
        ["python", str(ROOT / "scripts" / "validate_registry.py")],
        cwd=ROOT,
        check=True,
    )

    output = Path(args.output) if args.output else ROOT / "dist" / f"v{args.version}"
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    sums: list[str] = []
    for relative in DEFAULT_FILES:
        source = ROOT / relative
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        sums.append(f"{digest}  {relative}")

    (output / "SHA256SUMS").write_text("\n".join(sums) + "\n", encoding="utf-8")

    manifest = {
        "ontology_version": args.version,
        "source_commit": git_commit(),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "included_files": DEFAULT_FILES,
        "record_counts": {Path(path).stem: count_records(path) for path in DEFAULT_FILES},
        "validation_status": "passed",
        "evidence_review_cutoff": datetime.now(timezone.utc).date().isoformat(),
        "approved_by": [],
        "known_limitations": [
            "Approval fields must be completed before production import.",
            "Relevance weights are ontology annotations, not effect estimates.",
            "Training-fit mappings must not be published until their review_status is approved."
        ],
        "sha256sums_file": "SHA256SUMS"
    }
    (output / "release-manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )

    print(f"Built release bundle: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
