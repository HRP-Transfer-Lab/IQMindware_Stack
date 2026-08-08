# IQ Mindware Website Release Candidate

**Release:** `iqm-website-slice-v0.1.0-rc1`  
**Status:** release candidate; not yet approved for production import  
**Owner:** HRP Transfer Lab / IQ Mindware  
**Date:** 8 August 2026

## Purpose

This directory packages the narrow first website slice for the IQMindware.com workflow pivot.

It converts the wider research ontology into a deliberately bounded commercial release candidate based on the products that are actually complete and available for sale now.

## Commercially available now

```text
G Track
├─ attention battery
├─ Zone Check
├─ working-memory measures
├─ OMIB Matrix Reasoning Benchmark
└─ baseline / follow-up comparison

Attention Coach
└─ Signal Control

WM Coach
├─ Relational Memory — Signal
└─ Binding Memory — Signal
```

## Coming soon

```text
Evidence modes
Predictive Calibration profiles
Commit / Decision Timing modes
Path Prediction
Explicit Reasoning
Applied reasoning and restructuring routes
```

Coming-soon modules may be displayed in the roadmap and may be named as the closest target function. They must not appear as live route steps or be sold as currently available.

## Files

```text
product-availability.json
    Owner-confirmed commercial availability and fallback rules.

route-templates.json
    Six curated route configurations using live products only.

route-copy.json
    Candidate headings, status labels, module labels and evidence boundaries.

tests/website-route-cases.json
    Expected availability, fallback, governance and claims-boundary cases.

manifest.json
    Release-candidate scope, versions, production gates and limitations.

REVIEW_CHECKLIST.md
    Human scientific, claims, governance and website-import sign-off gates.

scripts/validate_website_release.py
    Dependency-free cross-reference and availability validator.

scripts/run_website_route_cases.py
    Executes the static availability, fallback and governance cases.

scripts/build_website_release.py
    Builds a deterministic import bundle after validation.
```

## Curated first routes

1. Individual focus under competing information.
2. Professional multi-source synthesis.
3. Report review and verification.
4. Complex-task re-entry after interruption.
5. Higher-education source synthesis.
6. Objective cognitive progress tracking.

These routes are evidence-informed configurations. They are not claims that the current apps already improve the corresponding workflow outcomes.

## Governing rules

```text
1. Return a route, not a binary evidence verdict.
2. Show only live modules in the available route.
3. Show future modules separately as coming soon.
4. Pair cognitive training with workflow-support recommendations.
5. Use G Track for baseline and separate follow-up where appropriate.
6. State the current applied-evidence boundary.
7. Route health-related or high-stakes uses to partner/research governance.
8. Never use Zone Check or cognitive scores for selection, diagnosis or punitive ranking.
```

## Validation commands

```bash
python workflow-ontology/scripts/validate_registry.py
python workflow-ontology/website-release/scripts/validate_website_release.py
python workflow-ontology/website-release/scripts/run_website_route_cases.py
```

## Production path

```text
human scientific review
→ claims and copy review
→ route and governance review
→ validator pass
→ immutable evidence release
→ website-repository import
→ local lock file and checksums
→ preview testing
→ production launch
```

The production website must not read these branch files dynamically. After approval, it should import a pinned release into the IQ Mindware website repository and retain the source versions in its lock file.
