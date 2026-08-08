# IQ Mindware Website Release Candidate

**Release:** `iqm-website-slice-v0.1.0-rc2`  
**Status:** implementation-ready preview contract; not yet approved for production import  
**Owner:** HRP Transfer Lab / IQ Mindware  
**Date:** 8 August 2026

## Purpose

This directory packages the narrow first website slice for the IQMindware.com workflow pivot.

It converts the wider research ontology into a bounded commercial and implementation contract based on the products that are complete and available for sale now.

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

Coming-soon modules may be displayed in the roadmap and named as the closest target function. They must not appear as live route steps or be sold as currently available.

## Runtime contracts

```text
product-availability.json
    Owner-confirmed availability and fallback rules.

evidence-slice.json
    Eight compact evidence cards for the live measurement and training components.

route-builder-config.json
    Three-question deterministic homepage questionnaire and matching policy.

route-templates.json
    Six curated route configurations using live products only.

route-copy.json
    Candidate headings, workflow explanations, module labels, evidence boundaries and CTAs.
```

## Validation and implementation files

```text
schemas/
    JSON Schemas for evidence cards, builder configuration and rendered route results.

tests/website-route-cases.json
    Availability, deterministic matching, governance and claims-boundary cases.

ontology-lock.template.json
    Fail-closed lock template for the eventual website import.

scripts/validate_website_release.py
    Cross-reference, product-status, evidence and matching-contract validation.

scripts/run_website_route_cases.py
    Executes the release-candidate route and boundary cases.

scripts/render_route_result.py
    Builds a normalised route-result payload for preview implementation.

scripts/build_website_release.py
    Validates, hashes and packages the import bundle.

reference/route-builder.reference.ts
    Dependency-free TypeScript reference for Codex.

examples/report-review-route.example.json
    Compact example of the route payload presented to the UI.

IMPLEMENTATION_HANDOFF.md
    Codex-facing integration, privacy, accessibility and acceptance contract.

REVIEW_CHECKLIST.md
    Human scientific, claims, governance and production-import sign-off gates.
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
4. Preserve four evidence dimensions:
   scientific basis, exact implementation, training benefit and workflow transfer.
5. Pair cognitive training with workflow-support recommendations.
6. Use G Track for baseline and separate follow-up where appropriate.
7. State the current applied-evidence boundary.
8. Route health-related or high-stakes uses to partner/research governance.
9. Never use Zone Check or cognitive scores for selection, diagnosis or punitive ranking.
10. Run the first questionnaire client-side and show value before contact capture.
11. Exclude free-text or LLM interpretation from the first production slice.
12. Fail closed when versions, IDs, manifests or checksums do not match.
```

## Deterministic homepage flow

```text
Who are you configuring this for?
→
What are you trying to accomplish?
→
What tends to happen when this becomes difficult?
→
highest eligible curated route
→
normalised route result
```

The required primary need determines eligibility. Audience and friction answers refine the route score but cannot replace the primary workflow match.

## Route-result structure

```text
heading
status labels
workflow explanation
available route
coming-soon targets
evidence cards
workflow supports
outcomes
evidence boundary
CTA
version metadata
```

## Validation commands

```bash
python workflow-ontology/scripts/validate_registry.py

python workflow-ontology/website-release/scripts/validate_website_release.py

python workflow-ontology/website-release/scripts/run_website_route_cases.py

python workflow-ontology/website-release/scripts/render_route_result.py \
  --route-id report_review_and_verification_v1
```

Build a candidate import bundle:

```bash
python workflow-ontology/website-release/scripts/build_website_release.py \
  --version 0.1.0-rc2 \
  --source-commit "$GITHUB_SHA"
```

## Production path

```text
human scientific review
→ claims and copy review
→ route and governance review
→ validator and route-case pass
→ immutable canonical evidence release
→ rc2 commercial bundle
→ website-repository import
→ completed local lock file and checksums
→ accessible preview testing
→ production launch
```

The production website must not read these branch files dynamically. After approval, it should import a pinned release into the IQ Mindware website repository and retain the exact versions and hashes in its lock file.
