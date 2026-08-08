#!/usr/bin/env python3
"""Validate the Cognitive Workflow Ontology without external dependencies."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_LOCI = {"person", "task_interface", "team_process", "organisation_system"}
ALLOWED_REVIEW = {"draft", "expert_reviewed", "approved", "deprecated", "retired"}
ALLOWED_EVIDENCE = {
    "strong",
    "moderate",
    "plausible",
    "plausible_but_not_established",
    "insufficient",
    "not_established",
    "not_applicable",
    "not_eligible",
}


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
    duplicates = {value for value, count in Counter(values).items() if count > 1}
    if duplicates:
        raise AssertionError(f"Duplicate {label} IDs: {sorted(duplicates)}")
    return set(values)


def require_nonempty_text(item: dict[str, Any], fields: list[str], label: str, errors: list[str]) -> None:
    for field in fields:
        value = item.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{label}: missing non-empty {field}")


def validate_references(
    values: Any,
    allowed: set[str],
    label: str,
    reference_label: str,
    errors: list[str],
) -> None:
    if values is None:
        return
    if not isinstance(values, list):
        errors.append(f"{label}: {reference_label} must be an array")
        return
    for value in values:
        if value not in allowed:
            errors.append(f"{label}: missing {reference_label} reference {value}")


def validate_evidence_level(value: Any, label: str, field: str, errors: list[str]) -> None:
    if value not in ALLOWED_EVIDENCE:
        errors.append(f"{label}: invalid {field} {value}")


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
    measurements = records("evidence/measurement-registry.json")
    training_mappings = records("evidence/training-fit-mappings.json")
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
        claim_ids = ids(claims, "claim_id", "evidence claim")
        measurement_ids = ids(measurements, "measurement_id", "measurement")
        ids(training_mappings, "mapping_id", "training-fit mapping")
        ids(stages, "workflow_stage_id", "workflow stage")
    except AssertionError as exc:
        errors.append(str(exc))
        niche_ids = workflow_ids = demand_ids = friction_ids = locus_ids = set()
        outcome_ids = support_ids = governance_ids = source_ids = claim_ids = set()
        measurement_ids = set()

    if locus_ids and locus_ids != ALLOWED_LOCI:
        errors.append(f"Intervention-locus registry must equal {sorted(ALLOWED_LOCI)}; got {sorted(locus_ids)}")

    function_data = load("mappings/demand-function-mappings.json")
    function_ids = {
        item.get("function_id")
        for item in function_data.get("functions", [])
        if isinstance(item.get("function_id"), str)
    }

    for source in sources:
        source_id = source.get("source_id", "<unknown>")
        require_nonempty_text(
            source,
            ["citation", "doi_or_url", "study_type", "population", "review_status", "last_reviewed"],
            source_id,
            errors,
        )
        if source.get("review_status") not in ALLOWED_REVIEW:
            errors.append(f"{source_id}: invalid review status {source.get('review_status')}")
        for field in ("constructs", "outcomes", "limitations"):
            if not isinstance(source.get(field), list):
                errors.append(f"{source_id}: {field} must be an array")

    for claim in claims:
        claim_id = claim.get("claim_id", "<unknown>")
        require_nonempty_text(
            claim,
            ["claim", "claim_type", "approved_public_wording", "required_caveat", "review_status", "last_reviewed"],
            claim_id,
            errors,
        )
        validate_evidence_level(claim.get("evidence_level"), claim_id, "evidence_level", errors)
        validate_references(claim.get("source_ids", []), source_ids, claim_id, "evidence source", errors)
        if claim.get("review_status") not in ALLOWED_REVIEW:
            errors.append(f"{claim_id}: invalid review status {claim.get('review_status')}")
        if claim.get("review_status") == "approved":
            if not claim.get("approved_public_wording") or not claim.get("required_caveat"):
                errors.append(f"{claim_id}: approved claim requires wording and caveat")

    for measurement in measurements:
        measurement_id = measurement.get("measurement_id", "<unknown>")
        require_nonempty_text(
            measurement,
            [
                "product_id",
                "component_id",
                "public_name",
                "construct",
                "approved_public_wording",
                "required_caveat",
                "governance_boundary",
                "review_status",
                "last_reviewed",
            ],
            measurement_id,
            errors,
        )
        validate_evidence_level(
            measurement.get("measurement_source_level"), measurement_id, "measurement_source_level", errors
        )
        validate_evidence_level(
            measurement.get("exact_implementation_level"), measurement_id, "exact_implementation_level", errors
        )
        validate_references(measurement.get("claim_ids", []), claim_ids, measurement_id, "claim", errors)
        validate_references(measurement.get("source_ids", []), source_ids, measurement_id, "evidence source", errors)
        if measurement.get("review_status") not in ALLOWED_REVIEW:
            errors.append(f"{measurement_id}: invalid review status {measurement.get('review_status')}")
        if not isinstance(measurement.get("validation_needs"), list):
            errors.append(f"{measurement_id}: validation_needs must be an array")
        if not isinstance(measurement.get("evidence_status_tags"), list):
            errors.append(f"{measurement_id}: evidence_status_tags must be an array")

    for mapping in training_mappings:
        mapping_id = mapping.get("mapping_id", "<unknown>")
        require_nonempty_text(
            mapping,
            [
                "user_goal_id",
                "user_goal",
                "training_target_id",
                "approved_claim",
                "required_caveat",
                "availability",
                "commercial_status",
                "governance_profile_id",
                "review_status",
                "last_reviewed",
            ],
            mapping_id,
            errors,
        )
        validate_evidence_level(mapping.get("mechanism_fit_level"), mapping_id, "mechanism_fit_level", errors)
        validate_evidence_level(mapping.get("training_benefit_level"), mapping_id, "training_benefit_level", errors)
        validate_evidence_level(mapping.get("workflow_transfer_level"), mapping_id, "workflow_transfer_level", errors)
        validate_references(mapping.get("claim_ids", []), claim_ids, mapping_id, "claim", errors)
        validate_references(mapping.get("source_ids", []), source_ids, mapping_id, "evidence source", errors)
        validate_references(
            mapping.get("gtrack_primary_measures", []), measurement_ids, mapping_id, "primary measurement", errors
        )
        validate_references(
            mapping.get("gtrack_secondary_measures", []), measurement_ids, mapping_id, "secondary measurement", errors
        )
        if mapping.get("governance_profile_id") not in governance_ids:
            errors.append(f"{mapping_id}: missing governance profile {mapping.get('governance_profile_id')}")
        if mapping.get("review_status") not in ALLOWED_REVIEW:
            errors.append(f"{mapping_id}: invalid review status {mapping.get('review_status')}")
        if not isinstance(mapping.get("product_route"), list) or not mapping.get("product_route"):
            errors.append(f"{mapping_id}: product_route must be a non-empty array")

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

    if errors:
        print("Cognitive Workflow Ontology validation FAILED:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Cognitive Workflow Ontology validation PASSED")
    print(
        f"Validated {len(stages)} workflow stages, {len(demands)} demands, {len(frictions)} frictions, "
        f"{len(sources)} sources, {len(claims)} claims, {len(measurements)} measures and "
        f"{len(training_mappings)} training-fit mappings."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
