#!/usr/bin/env python3
"""Validate the Cognitive Workflow Ontology without external dependencies."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_LOCI = {"person", "task_interface", "team_process", "organisation_system"}
ALLOWED_REVIEW = {"draft", "expert_reviewed", "approved", "deprecated", "retired"}


def load(relative: str) -> dict[str, Any]:
    path = ROOT / relative
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise AssertionError(f"Missing required file: {relative}") from exc
    except json.JSONDecodeError as exc:
        raise AssertionError(f"Invalid JSON in {relative}: {exc}") from exc


def records(relative: str) -> list[dict[str, Any]]:
    data = load(relative)
    value = data.get("records")
    if not isinstance(value, list):
        raise AssertionError(f"{relative} must contain a records array")
    return value


def ids(items: list[dict[str, Any]], key: str, label: str) -> set[str]:
    values: list[str] = []
    for item in items:
        value = item.get(key)
        if not isinstance(value, str) or not value:
            raise AssertionError(f"{label} record missing {key}: {item}")
        values.append(value)
    duplicates = {value for value in values if values.count(value) > 1}
    if duplicates:
        raise AssertionError(f"Duplicate {label} IDs: {sorted(duplicates)}")
    return set(values)


def main() -> int:
    errors: list[str] = []

    niches = records("ontology/niches.json")
    workflows = records("ontology/workflow-archetypes.json")
    demands = records("ontology/demand-dimensions.json")
    frictions = records("ontology/friction-signatures.json")
    loci = records("ontology/intervention-loci.json")
    outcomes = records("ontology/outcome-measures.json")
    supports = records("mappings/workflow-supports.json")
    governance = records("mappings/governance-profiles.json")
    sources = records("evidence/evidence-sources.json")
    claims = records("evidence/evidence-claims.json")
    stages = records("ontology/workflow-stages.json")

    try:
        niche_ids = ids(niches, "niche_id", "niche")
        workflow_ids = ids(workflows, "workflow_id", "workflow")
        demand_ids = ids(demands, "demand_id", "demand")
        friction_ids = ids(frictions, "friction_id", "friction")
        locus_ids = ids(loci, "locus_id", "intervention locus")
        outcome_ids = ids(outcomes, "outcome_id", "outcome")
        support_ids = ids(supports, "workflow_support_id", "workflow support")
        governance_ids = ids(governance, "governance_profile_id", "governance profile")
        source_ids = ids(sources, "source_id", "evidence source")
        ids(claims, "claim_id", "evidence claim")
        ids(stages, "workflow_stage_id", "workflow stage")
    except AssertionError as exc:
        errors.append(str(exc))
        niche_ids = workflow_ids = demand_ids = friction_ids = locus_ids = set()
        outcome_ids = support_ids = governance_ids = source_ids = set()

    if locus_ids and locus_ids != ALLOWED_LOCI:
        errors.append(f"Intervention-locus registry must equal {sorted(ALLOWED_LOCI)}; got {sorted(locus_ids)}")

    function_data = load("mappings/demand-function-mappings.json")
    function_ids = {
        item.get("function_id") for item in function_data.get("functions", [])
        if isinstance(item.get("function_id"), str)
    }

    for stage in stages:
        stage_id = stage.get("workflow_stage_id", "<unknown>")

        if stage.get("workflow_id") not in workflow_ids:
            errors.append(f"{stage_id}: missing workflow reference {stage.get('workflow_id')}")

        for niche_id in stage.get("niche_ids", []):
            if niche_id not in niche_ids:
                errors.append(f"{stage_id}: missing niche reference {niche_id}")

        for demand_id, value in stage.get("demand_profile", {}).items():
            if demand_id not in demand_ids:
                errors.append(f"{stage_id}: missing demand reference {demand_id}")
            if not isinstance(value, int) or not 0 <= value <= 4:
                errors.append(f"{stage_id}: demand {demand_id} must be integer 0-4")

        for friction_id in stage.get("likely_frictions", []):
            if friction_id not in friction_ids:
                errors.append(f"{stage_id}: missing friction reference {friction_id}")

        for mapping in stage.get("function_mappings", []):
            function_id = mapping.get("function_id")
            if function_id not in function_ids:
                errors.append(f"{stage_id}: missing function reference {function_id}")
            for source_id in mapping.get("source_ids", []):
                if source_id not in source_ids:
                    errors.append(f"{stage_id}: missing evidence source {source_id}")

        for locus in stage.get("intervention_loci", []):
            if locus not in ALLOWED_LOCI:
                errors.append(f"{stage_id}: invalid intervention locus {locus}")

        for support_id in stage.get("workflow_support_ids", []):
            if support_id not in support_ids:
                errors.append(f"{stage_id}: missing workflow support {support_id}")

        for outcome_id in stage.get("outcome_ids", []):
            if outcome_id not in outcome_ids:
                errors.append(f"{stage_id}: missing outcome {outcome_id}")

        governance_id = stage.get("governance_profile_id")
        if governance_id not in governance_ids:
            errors.append(f"{stage_id}: missing governance profile {governance_id}")

        status = stage.get("review_status")
        if status not in ALLOWED_REVIEW:
            errors.append(f"{stage_id}: invalid review status {status}")

        if "health_service_pathway" in stage.get("niche_ids", []):
            if governance_id != "health_partner_research_v1":
                errors.append(f"{stage_id}: health record must use partner/research governance")
            if not stage.get("claims_boundary"):
                errors.append(f"{stage_id}: health record requires a claims boundary")

    for claim in claims:
        claim_id = claim.get("claim_id", "<unknown>")
        for source_id in claim.get("source_ids", []):
            if source_id not in source_ids:
                errors.append(f"{claim_id}: missing evidence source {source_id}")
        if claim.get("review_status") == "approved":
            if not claim.get("approved_public_wording") or not claim.get("required_caveat"):
                errors.append(f"{claim_id}: approved claim requires wording and caveat")

    if errors:
        print("Cognitive Workflow Ontology validation FAILED:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Cognitive Workflow Ontology validation PASSED")
    print(f"Validated {len(stages)} workflow stages, {len(demands)} demands and {len(frictions)} frictions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
