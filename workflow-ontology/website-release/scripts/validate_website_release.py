#!/usr/bin/env python3
"""Validate the narrow IQ Mindware website release candidate."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
RELEASE = ROOT / "website-release"


def load(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise AssertionError(f"Missing required file: {path.relative_to(ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise AssertionError(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def ids(records: list[dict[str, Any]], key: str, label: str) -> set[str]:
    values: list[str] = []
    for record in records:
        value = record.get(key)
        if not isinstance(value, str) or not value:
            raise AssertionError(f"{label} record missing {key}: {record}")
        values.append(value)
    duplicates = sorted({value for value in values if values.count(value) > 1})
    if duplicates:
        raise AssertionError(f"Duplicate {label} IDs: {duplicates}")
    return set(values)


def main() -> int:
    errors: list[str] = []

    availability = load(RELEASE / "product-availability.json")
    evidence_slice = load(RELEASE / "evidence-slice.json")
    builder = load(RELEASE / "route-builder-config.json")
    routes = load(RELEASE / "route-templates.json")
    copy = load(RELEASE / "route-copy.json")
    tests = load(RELEASE / "tests" / "website-route-cases.json")
    manifest = load(RELEASE / "manifest.json")
    lock_template = load(RELEASE / "ontology-lock.template.json")

    measurements = load(ROOT / "evidence" / "measurement-registry.json")
    claims = load(ROOT / "evidence" / "evidence-claims.json")
    supports = load(ROOT / "mappings" / "workflow-supports.json")
    outcomes = load(ROOT / "ontology" / "outcome-measures.json")
    governance = load(ROOT / "mappings" / "governance-profiles.json")
    workflows = load(ROOT / "ontology" / "workflow-archetypes.json")
    stages = load(ROOT / "ontology" / "workflow-stages.json")
    niches = load(ROOT / "ontology" / "niches.json")
    frictions = load(ROOT / "ontology" / "friction-signatures.json")

    try:
        measurement_ids = ids(measurements["records"], "measurement_id", "measurement")
        claim_ids = ids(claims["records"], "claim_id", "claim")
        support_ids = ids(supports["records"], "workflow_support_id", "workflow support")
        outcome_ids = ids(outcomes["records"], "outcome_id", "outcome")
        governance_ids = ids(governance["records"], "governance_profile_id", "governance profile")
        workflow_ids = ids(workflows["records"], "workflow_id", "workflow")
        stage_ids = ids(stages["records"], "workflow_stage_id", "workflow stage")
        niche_ids = ids(niches["records"], "niche_id", "niche")
        friction_ids = ids(frictions["records"], "friction_id", "friction")
        route_ids = ids(routes["routes"], "route_id", "website route")
        evidence_card_ids = ids(evidence_slice["records"], "evidence_card_id", "evidence card")
    except (AssertionError, KeyError) as exc:
        errors.append(str(exc))
        measurement_ids = claim_ids = support_ids = outcome_ids = governance_ids = set()
        workflow_ids = stage_ids = niche_ids = friction_ids = route_ids = evidence_card_ids = set()

    expected_products = {"g_track", "attention_coach", "wm_coach"}
    products = availability.get("products", [])
    product_ids = {item.get("product_id") for item in products}
    if product_ids != expected_products:
        errors.append(
            "Available product registry must contain exactly "
            f"{sorted(expected_products)}; got {sorted(product_ids)}"
        )

    available_components: set[str] = set()
    coming_soon_components: set[str] = set()

    for product in products:
        product_id = product.get("product_id", "<unknown>")
        if product.get("product_status") != "available_now":
            errors.append(f"{product_id}: product_status must be available_now")
        if product.get("sales_status") != "available_for_sale_now":
            errors.append(f"{product_id}: sales_status must be available_for_sale_now")

        for component in product.get("available_components", []):
            component_id = component.get("component_id")
            if not component_id:
                errors.append(f"{product_id}: available component missing component_id")
                continue
            if component.get("status") != "available_now":
                errors.append(f"{component_id}: available component must have status available_now")
            available_components.add(component_id)
            for measurement_id in component.get("measurement_ids", []):
                if measurement_id not in measurement_ids:
                    errors.append(f"{component_id}: missing measurement reference {measurement_id}")

        for component in product.get("coming_soon_components", []):
            component_id = component.get("component_id")
            if not component_id:
                errors.append(f"{product_id}: coming-soon component missing component_id")
                continue
            if component.get("status") != "coming_soon":
                errors.append(f"{component_id}: future component must have status coming_soon")
            coming_soon_components.add(component_id)

    for family in availability.get("coming_soon_product_families", []):
        if family.get("status") != "coming_soon":
            errors.append(f"{family.get('product_id')}: future product family must be coming_soon")
        coming_soon_components.update(family.get("modules", []))

    overlap = available_components & coming_soon_components
    if overlap:
        errors.append(f"Components cannot be both available and coming soon: {sorted(overlap)}")

    required_available = {
        "gtrack_attention_battery",
        "gtrack_zone_check",
        "gtrack_working_memory",
        "gtrack_matrix_reasoning",
        "gtrack_longitudinal_comparison",
        "attention_signal",
        "wm_relational_signal",
        "wm_binding_signal",
    }
    missing_available = required_available - available_components
    if missing_available:
        errors.append(f"Missing owner-confirmed live components: {sorted(missing_available)}")

    allowed_evidence_levels = set(evidence_slice.get("display_policy", {}).get("allowed_public_levels", []))
    for card in evidence_slice.get("records", []):
        card_id = card.get("evidence_card_id", "<unknown>")
        if card.get("review_status") != "release_candidate":
            errors.append(f"{card_id}: evidence card review_status must be release_candidate")
        for component_id in card.get("component_ids", []):
            if component_id not in available_components:
                errors.append(f"{card_id}: evidence card references non-live component {component_id}")
        for measurement_id in card.get("measurement_ids", []):
            if measurement_id not in measurement_ids:
                errors.append(f"{card_id}: missing measurement reference {measurement_id}")
        for claim_id in card.get("claim_ids", []):
            if claim_id not in claim_ids:
                errors.append(f"{card_id}: missing claim reference {claim_id}")
        profile = card.get("evidence_profile", {})
        expected_dimensions = {"scientific_basis", "exact_implementation", "training_benefit", "workflow_transfer"}
        if set(profile) != expected_dimensions:
            errors.append(
                f"{card_id}: evidence profile must contain exactly {sorted(expected_dimensions)}"
            )
        for dimension, value in profile.items():
            if value.get("level") not in allowed_evidence_levels:
                errors.append(
                    f"{card_id}: invalid public level {value.get('level')} in {dimension}"
                )
            if not value.get("label") or not value.get("summary"):
                errors.append(f"{card_id}: incomplete evidence dimension {dimension}")

    module_labels = copy.get("module_labels", {})
    heading_keys = set(copy.get("headings", {}))
    explanation_keys = set(copy.get("workflow_explanations", {}))
    boundary_keys = set(copy.get("evidence_boundaries", {}))
    status_keys = set(copy.get("status_copy", {}))

    live_route_tokens = {
        "gtrack_attention_baseline",
        "gtrack_full_baseline",
        "gtrack_full_followup",
        "gtrack_attention_followup",
        "attention_signal",
        "wm_relational_signal",
        "wm_binding_signal",
        "matched_live_training_optional",
        "delayed_recheck",
    }

    for route in routes.get("routes", []):
        route_id = route.get("route_id", "<unknown>")

        if route.get("heading_key") not in heading_keys:
            errors.append(f"{route_id}: missing heading key {route.get('heading_key')}")
        if route.get("workflow_explanation_key") not in explanation_keys:
            errors.append(
                f"{route_id}: missing workflow explanation key "
                f"{route.get('workflow_explanation_key')}"
            )
        if route.get("evidence_boundary_key") not in boundary_keys:
            errors.append(
                f"{route_id}: missing evidence boundary key "
                f"{route.get('evidence_boundary_key')}"
            )
        for status in route.get("route_status", []):
            if status not in status_keys:
                errors.append(f"{route_id}: missing public status copy for {status}")

        for step in route.get("available_protocol_route", []):
            if step not in live_route_tokens:
                errors.append(f"{route_id}: unavailable or unknown live route step {step}")
            if step not in module_labels:
                errors.append(f"{route_id}: missing public label for route step {step}")
            if step in coming_soon_components:
                errors.append(f"{route_id}: coming-soon component used as live route step {step}")

        for target in route.get("target_functions_in_development", []):
            if target in route.get("available_protocol_route", []):
                errors.append(f"{route_id}: future target also appears as a live route step {target}")
            if target not in coming_soon_components:
                errors.append(f"{route_id}: target function is not registered as coming soon: {target}")

        for card_id in route.get("evidence_card_ids", []):
            if card_id not in evidence_card_ids:
                errors.append(f"{route_id}: missing evidence card {card_id}")
        if not route.get("evidence_card_ids"):
            errors.append(f"{route_id}: no evidence cards assigned")

        for niche_id in route.get("niche_ids", []):
            if niche_id not in niche_ids:
                errors.append(f"{route_id}: missing niche reference {niche_id}")

        workflow_id = route.get("workflow_archetype_id")
        if workflow_id and workflow_id not in workflow_ids:
            errors.append(f"{route_id}: missing workflow archetype {workflow_id}")

        for stage_id in route.get("workflow_stage_ids", []):
            if stage_id not in stage_ids:
                errors.append(f"{route_id}: missing workflow stage {stage_id}")

        for support_id in route.get("workflow_support_ids", []):
            if support_id not in support_ids:
                errors.append(f"{route_id}: missing workflow support {support_id}")

        for outcome_id in route.get("outcome_ids", []):
            if outcome_id not in outcome_ids:
                errors.append(f"{route_id}: missing outcome {outcome_id}")

        if route.get("governance_profile_id") not in governance_ids:
            errors.append(
                f"{route_id}: missing governance profile {route.get('governance_profile_id')}"
            )

    question_options: dict[str, set[str]] = {}
    for question in builder.get("questions", []):
        qid = question.get("question_id")
        if not qid:
            errors.append("Route-builder question missing question_id")
            continue
        if qid in question_options:
            errors.append(f"Duplicate route-builder question: {qid}")
            continue
        option_values = [option.get("option_id") for option in question.get("options", [])]
        if any(not value for value in option_values):
            errors.append(f"{qid}: option missing option_id")
        if len(option_values) != len(set(option_values)):
            errors.append(f"{qid}: duplicate option IDs")
        question_options[qid] = set(option_values)

    friction_options = question_options.get("observed_friction", set())
    unknown_frictions = friction_options - friction_ids
    if unknown_frictions:
        errors.append(f"Route builder contains unknown frictions: {sorted(unknown_frictions)}")

    rule_route_ids: set[str] = set()
    for rule in builder.get("route_rules", []):
        route_id = rule.get("route_id")
        if route_id not in route_ids:
            errors.append(f"Route-builder rule references missing route {route_id}")
            continue
        rule_route_ids.add(route_id)
        required = rule.get("required_answers", {})
        for question_id, options in required.items():
            if question_id not in question_options:
                errors.append(f"{route_id}: unknown required question {question_id}")
                continue
            for option in options:
                if option not in question_options[question_id]:
                    errors.append(f"{route_id}: unknown required option {question_id}={option}")
        for question_id, weights in rule.get("score_weights", {}).items():
            if question_id not in question_options:
                errors.append(f"{route_id}: unknown weighted question {question_id}")
                continue
            for option_id in weights:
                if option_id not in question_options[question_id]:
                    errors.append(f"{route_id}: unknown weighted option {question_id}={option_id}")

    if rule_route_ids != route_ids:
        errors.append(
            "Route-builder rules must cover every curated route exactly once; "
            f"missing={sorted(route_ids - rule_route_ids)}, "
            f"extra={sorted(rule_route_ids - route_ids)}"
        )

    required_question_ids = set(builder.get("selection_policy", {}).get("required_question_ids", []))
    if not required_question_ids <= set(question_options):
        errors.append(
            f"Unknown required question IDs: {sorted(required_question_ids - set(question_options))}"
        )

    for case in tests.get("cases", []):
        if "route_id" in case and case["route_id"] not in route_ids:
            errors.append(f"{case.get('case_id')}: missing route reference {case['route_id']}")

    included_files = set(manifest.get("included_files", []))
    expected_files = {
        "product-availability.json",
        "evidence-slice.json",
        "route-builder-config.json",
        "route-templates.json",
        "route-copy.json",
        "tests/website-route-cases.json",
        "schemas/website-evidence-slice.schema.json",
        "schemas/route-builder-config.schema.json",
        "schemas/rendered-route.schema.json",
        "ontology-lock.template.json",
    }
    if included_files != expected_files:
        errors.append(
            "Manifest included_files mismatch: "
            f"expected {sorted(expected_files)}, got {sorted(included_files)}"
        )

    if manifest.get("scope", {}).get("curated_route_count") != len(routes.get("routes", [])):
        errors.append("Manifest curated_route_count does not match route registry")
    if manifest.get("scope", {}).get("evidence_card_count") != len(evidence_slice.get("records", [])):
        errors.append("Manifest evidence_card_count does not match evidence slice")
    if manifest.get("scope", {}).get("route_question_count") != len(builder.get("questions", [])):
        errors.append("Manifest route_question_count does not match builder config")
    if lock_template.get("approved_for_production") is not False:
        errors.append("Lock template must default to approved_for_production=false")
    if lock_template.get("fail_closed") is not True:
        errors.append("Lock template must default to fail_closed=true")

    if errors:
        print("IQ Mindware website release validation FAILED:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("IQ Mindware website release validation PASSED")
    print(f"Validated {len(routes['routes'])} curated routes.")
    print(f"Validated {len(evidence_slice['records'])} website evidence cards.")
    print(f"Validated {len(builder['questions'])} route-builder questions.")
    print(f"Confirmed {len(available_components)} live components.")
    print(f"Registered {len(coming_soon_components)} coming-soon modules.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
