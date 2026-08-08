# Workflow Ontology Evidence Registry

**Status:** draft evidence infrastructure  
**Branch:** `feat/workflow-ontology-v0.1`

This directory is the canonical evidence layer for the Cognitive Workflow Ontology and the IQ Mindware website route builder.

## Canonical files

```text
evidence-sources.json
    Bibliographic and internal evidence-source registry.

evidence-claims.json
    Atomic, reviewable claims with approved public wording and caveats.

measurement-registry.json
    Evidence status of G Track measures and longitudinal interpretations.

training-fit-mappings.json
    Goal-to-product mappings for the deterministic website route builder.

reviews/
    Provenance and research reviews supporting registry decisions.
```

## Governing rule

The evidence chain must remain decomposed:

```text
workflow-demand support
→ cognitive-function mapping
→ measurement/source validity
→ exact implementation validity
→ training-benefit evidence
→ workflow-transfer evidence
```

These dimensions must not be collapsed into one `science-backed` score.

## Source-document policy

The human-readable **IQ Mindware Training-Fit Evidence Registry v0.2** is the reviewed seed for current-product claims.

The broader **IQM Stack Evidence** table is retained as a discovery and prioritisation backlog. Its evidence-strength labels must not be imported automatically. Each claim must be checked against the source, separated from product-specific evidence, and regraded under [`../docs/EVIDENCE_GRADING.md`](../docs/EVIDENCE_GRADING.md).

## Active evidence reviews

### G Track Attention and Zone

[`reviews/GT_ATTENTION_ZONE_EVIDENCE_REVIEW_v0.1.md`](reviews/GT_ATTENTION_ZONE_EVIDENCE_REVIEW_v0.1.md)

This review covers:

```text
SART engagement consistency
SART response-control stability
Stroop conflict control
Flanker selective attention / response competition
combined Attention profile
four exploratory behavioural response profiles
provisional Zone estimate
```

It includes peer-reviewed evidence, an explicitly labelled arXiv/bioRxiv watchlist, revised grading recommendations, scoring requirements and a proposed prospective validation study.

The review does **not** approve public claims or promote the canonical records. Its purpose is to support expert review and the next machine-readable revision.

## Product scope for the first evidence release

```text
G Track
├─ SART, Stroop and Flanker attention measures
├─ provisional Zone context
├─ complex-span-style working memory
├─ visual working-memory binding
└─ OMIB Matrix Reasoning Benchmark

Attention Coach
└─ Signal Control / masked Majority Function training

WM Coach
├─ Relational Memory Signal
└─ Binding Memory Signal
```

Evidence, Commit, Predictive Calibration, Path Prediction and explicit Reasoning are not to be presented as currently validated commercial modules unless a separate approved beta or research record exists.

## Production policy

Only records with `review_status: approved` may enter a tagged production release. Draft records may support internal review and website-preview development only.

The production website must import a pinned release rather than reading the latest branch dynamically.

Every published route should retain:

```text
ontology_version
evidence_registry_version
route_engine_version
product_availability_version
copy_version
```
