#!/usr/bin/env python3
"""Render a normalised route-result payload for preview and implementation tests."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
RELEASE = ROOT / "website-release"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--route-id", required=True)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    routes_data = load(RELEASE / "route-templates.json")
    route_copy = load(RELEASE / "route-copy.json")
    evidence_data = load(RELEASE / "evidence-slice.json")
    availability = load(RELEASE / "product-availability.json")
    supports_data = load(ROOT / "mappings" / "workflow-supports.json")
    outcomes_data = load(ROOT / "ontology" / "outcome-measures.json")
    manifest = load(RELEASE / "manifest.json")

    routes = {record["route_id"]: record for record in routes_data["routes"]}
    if args.route_id not in routes:
        raise SystemExit(f"Unknown route: {args.route_id}")
    route = routes[args.route_id]

    evidence = {record["evidence_card_id"]: record for record in evidence_data["records"]}
    supports = {record["workflow_support_id"]: record for record in supports_data["records"]}
    outcomes = {record["outcome_id"]: record for record in outcomes_data["records"]}

    future: dict[str, dict[str, Any]] = {}
    for product in availability["products"]:
        for component in product.get("coming_soon_components", []):
            future[component["component_id"]] = component
    for family in availability.get("coming_soon_product_families", []):
        for component_id in family.get("modules", []):
            future[component_id] = {
                "component_id": component_id,
                "status": "coming_soon",
            }

    payload = {
        "route_id": route["route_id"],
        "heading": route_copy["headings"][route["heading_key"]],
        "status_labels": [
            route_copy["status_copy"][status] for status in route["route_status"]
        ],
        "workflow_explanation": route_copy["workflow_explanations"][
            route["workflow_explanation_key"]
        ],
        "available_protocol_route": [
            {
                "step_id": step,
                "label": route_copy["module_labels"][step],
                "availability": "available_now",
            }
            for step in route["available_protocol_route"]
        ],
        "coming_soon_targets": [
            {
                "component_id": component_id,
                "label": route_copy["coming_soon_labels"].get(
                    component_id, component_id
                ),
                "availability": future[component_id]["status"],
                "nearest_available_foundation": future[component_id].get(
                    "nearest_available_foundation"
                ),
                "explanation": route_copy["coming_soon_explanations"].get(
                    component_id
                ),
            }
            for component_id in route["target_functions_in_development"]
        ],
        "evidence_cards": [
            evidence[card_id] for card_id in route["evidence_card_ids"]
        ],
        "workflow_supports": [
            {
                "workflow_support_id": support_id,
                "label": supports[support_id]["label"],
                "description": supports[support_id]["description"],
                "locus": supports[support_id]["locus"],
            }
            for support_id in route["workflow_support_ids"]
        ],
        "outcomes": [
            {
                "outcome_id": outcome_id,
                "label": outcomes[outcome_id]["label"],
                "level": outcomes[outcome_id]["level"],
                "interpretation": outcomes[outcome_id]["interpretation"],
            }
            for outcome_id in route["outcome_ids"]
        ],
        "evidence_boundary": route_copy["evidence_boundaries"][
            route["evidence_boundary_key"]
        ],
        "primary_cta": route_copy["cta_copy"][route["primary_cta"]],
        "versions": {
            "ontology": manifest["ontology_version"],
            "evidence": manifest["website_evidence_slice_version"],
            "availability": manifest["product_availability_version"],
            "route_config": manifest["route_builder_config_version"],
            "copy": manifest["copy_version"],
        },
    }

    output = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
