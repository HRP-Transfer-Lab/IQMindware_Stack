#!/usr/bin/env python3
"""Execute the static website-release route and boundary cases."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
RELEASE = ROOT / "website-release"


def load(relative: str) -> dict[str, Any]:
    return json.loads((RELEASE / relative).read_text(encoding="utf-8"))


def main() -> int:
    availability = load("product-availability.json")
    routes_data = load("route-templates.json")
    copy = load("route-copy.json")
    tests = load("tests/website-route-cases.json")

    routes = {route["route_id"]: route for route in routes_data["routes"]}

    live_components: set[str] = set()
    future_components: dict[str, dict[str, Any]] = {}

    for product in availability["products"]:
        for component in product.get("available_components", []):
            live_components.add(component["component_id"])
        for component in product.get("coming_soon_components", []):
            future_components[component["component_id"]] = component

    for family in availability.get("coming_soon_product_families", []):
        for module in family.get("modules", []):
            future_components[module] = {
                "component_id": module,
                "status": "coming_soon",
            }

    errors: list[str] = []

    for case in tests["cases"]:
        case_id = case["case_id"]

        if case_id == "live_route_contains_only_available_modules":
            route = routes[case["route_id"]]
            expected = case["assertions"]["available_protocol_route_must_only_use"]
            actual = route["available_protocol_route"]
            if actual != expected:
                errors.append(f"{case_id}: route steps differ; expected {expected}, got {actual}")
            forbidden = set(case["assertions"]["must_not_include_available_steps"])
            used_forbidden = forbidden & set(actual)
            if used_forbidden:
                errors.append(f"{case_id}: future modules used as live steps: {sorted(used_forbidden)}")

        elif case_id == "evidence_goal_uses_partial_fit_fallback":
            expected = case["expected"]
            module = future_components.get(expected["target_module"])
            if not module:
                errors.append(f"{case_id}: target future module is not registered")
                continue
            if module.get("status") != expected["target_status"]:
                errors.append(f"{case_id}: target status mismatch")
            if module.get("nearest_available_foundation") != expected["nearest_available_foundation"]:
                errors.append(f"{case_id}: nearest available foundation mismatch")
            if expected["nearest_available_foundation"] not in live_components:
                errors.append(f"{case_id}: fallback is not a live component")

        elif case_id == "reasoning_goal_is_not_sold_as_live":
            expected = case["expected"]
            for module_id in expected["target_modules"]:
                if module_id not in future_components:
                    errors.append(f"{case_id}: reasoning module not registered as coming soon: {module_id}")
                if module_id in live_components:
                    errors.append(f"{case_id}: reasoning module incorrectly registered as live: {module_id}")
            full_copy = json.dumps(copy)
            for forbidden_claim in expected["must_not_claim"]:
                if forbidden_claim in full_copy:
                    errors.append(f"{case_id}: forbidden claim appears in route copy: {forbidden_claim}")

        elif case_id == "matrix_goal_is_measurement_first":
            route = routes["objective_cognitive_progress_tracking_v1"]
            for required in case["expected"]["must_include"]:
                if required not in route["available_protocol_route"]:
                    errors.append(f"{case_id}: missing required measurement step {required}")
            full_copy = json.dumps(copy).lower()
            for forbidden_claim in case["expected"]["must_not_claim"]:
                if forbidden_claim.lower() in full_copy:
                    errors.append(f"{case_id}: forbidden matrix claim appears in route copy")

        elif case_id == "zone_check_not_consequential":
            g_track = next(
                product for product in availability["products"]
                if product["product_id"] == "g_track"
            )
            zone = next(
                component for component in g_track["available_components"]
                if component["component_id"] == "gtrack_zone_check"
            )
            boundary = zone.get("boundary", "").lower()
            if "not a diagnosis" not in boundary:
                errors.append(f"{case_id}: Zone Check diagnostic boundary is missing")
            rules = " ".join(availability.get("routing_rules", [])).lower()
            if "consequential" not in rules:
                errors.append(f"{case_id}: consequential-use prohibition is missing")

        elif case_id == "health_goal_routes_to_partner_research":
            self_service_health_routes = [
                route["route_id"]
                for route in routes.values()
                if "health_service_pathway" in route.get("niche_ids", [])
            ]
            if self_service_health_routes:
                errors.append(
                    f"{case_id}: health routes present in self-service catalogue: "
                    f"{self_service_health_routes}"
                )
            if case["expected"]["governance_profile_id"] != "health_partner_research_v1":
                errors.append(f"{case_id}: expected governance fixture is incorrect")

        else:
            errors.append(f"Unknown website route test case: {case_id}")

    if errors:
        print("IQ Mindware website route cases FAILED:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("IQ Mindware website route cases PASSED")
    print(f"Executed {len(tests['cases'])} release-candidate cases.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
