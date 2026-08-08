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

## Candidate full-stack files

```text
vertical-stack-mode-matrix.candidate.json
    Candidate 5-capacity × 4-control-mode evidence matrix.

vertical-stack-sources.candidate.json
    Candidate peer-reviewed and prepublication sources for the full stack.

live-signal-reasoning-overrides.candidate.json
    Promotion-oriented overrides for live Signal modes and the explicit-reasoning measurement model.

live-signal-reasoning-source-additions.candidate.json
    Source additions for the live-Signal and explicit-reasoning audit.

explicit-reasoning-intervention-families.candidate.json
    Separates formal relational reasoning, professional belief calibration,
    non-clinical reframing, clinical cognitive restructuring and reappraisal.

explicit-reasoning-cbt-sources.candidate.json
    Candidate peer-reviewed and prepublication sources for explicit restructuring,
    Socratic questioning, behavioural experiments, CBT components and reappraisal.
```

Candidate files are not production registries. They support expert review, schema development and later promotion into atomic source, claim, protocol and mapping records.

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

### Full vertical stack and control modes

[`reviews/FULL_VERTICAL_STACK_MODE_EVIDENCE_REVIEW_v0.1.md`](reviews/FULL_VERTICAL_STACK_MODE_EVIDENCE_REVIEW_v0.1.md)

This review crosses:

```text
Attention Control
Relational Memory
Binding Memory
Path Prediction
Reasoning
```

with:

```text
Signal
Evidence
Predictive Calibration
Commit
```

It extends the review through explicit symbolic, nonsense-semantic and domain-semantic verbal reasoning, including belief calibration and a separately governed evidence-sensitive reframing application.

Machine-readable companions:

- [`vertical-stack-mode-matrix.candidate.json`](vertical-stack-mode-matrix.candidate.json)
- [`vertical-stack-sources.candidate.json`](vertical-stack-sources.candidate.json)

### Live Signal and explicit-reasoning measurement audit

[`reviews/LIVE_SIGNAL_AND_REASONING_MEASUREMENT_REVIEW_v0.1.md`](reviews/LIVE_SIGNAL_AND_REASONING_MEASUREMENT_REVIEW_v0.1.md)

This review audits the three commercially available Signal implementations and specifies a multi-parameter explicit-reasoning measurement model.

Machine-readable companions:

- [`live-signal-reasoning-overrides.candidate.json`](live-signal-reasoning-overrides.candidate.json)
- [`live-signal-reasoning-source-additions.candidate.json`](live-signal-reasoning-source-additions.candidate.json)

### Explicit reasoning, cognitive restructuring and reappraisal

[`reviews/EXPLICIT_REASONING_COGNITIVE_RESTRUCTURING_REVIEW_v0.1.md`](reviews/EXPLICIT_REASONING_COGNITIVE_RESTRUCTURING_REVIEW_v0.1.md)

This review corrects the interpretation of the Reasoning layer. It separates:

```text
formal / relational reasoning
professional belief calibration
non-clinical evidence-sensitive reframing
cognitive restructuring in CBT-type interventions
cognitive reappraisal
behavioural-experiment belief updating
LLM-assisted delivery research
```

Machine-readable companions:

- [`explicit-reasoning-intervention-families.candidate.json`](explicit-reasoning-intervention-families.candidate.json)
- [`explicit-reasoning-cbt-sources.candidate.json`](explicit-reasoning-cbt-sources.candidate.json)

The governing distinction is:

> **Cognitive restructuring is an applied explicit-reasoning intervention family, not merely a SMART-style wrapper and not a generic Reasoning-capacity score.**

Clinical cognitive-restructuring evidence remains category- and condition-specific. It cannot be used as direct evidence for the generic IQ Mindware Reasoning app.

The full-stack reviews preserve four boundaries:

1. the five capacities have defensible construct families, but their exact implementations are not equally validated;
2. Predictive Calibration is a cross-cutting derived profile, not a fourth gameplay task;
3. formal relational reasoning, professional belief calibration, cognitive restructuring and reappraisal are related but distinct protocol families;
4. non-clinical reframing and health-governed clinical applications require separate claims, outcomes and governance.

No review document approves public claims or promotes canonical records automatically. Reviews support named human expert assessment and the next machine-readable revision.

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

## Full-stack development scope

The research registry now covers the intended architecture beyond the first production release:

```text
Attention Control
Structured Working Memory
├─ Relational Memory
└─ Binding Memory
Predictive Inference
├─ Path Prediction
└─ Explicit Reasoning
```

across the four APC functions:

```text
Signal
Evidence
Predictive Calibration
Commit
```

The candidate matrix is intended to guide research prioritisation and honest website status labels. It must not cause the website to imply that roadmap modules are already available or validated.

The explicit Reasoning family has two broad development branches:

```text
REASONING CORE
formal structure, argument evidence, belief calibration and conclusion timing

APPLIED REASONING
non-clinical evidence-sensitive reframing and separately governed clinical protocols
```

The generic Reasoning score must not be presented as a measure of clinical cognitive-restructuring skill.

## Prepublication policy

arXiv, PsyArXiv and bioRxiv sources may be retained as `prepublication_watchlist` records when they contribute useful models, open analyses, unusually dense data or direct challenges to measurement assumptions.

A preprint must not, by itself:

```text
upgrade a public claim to strong
validate an exact product implementation
justify a clinical or consequential route
override stronger peer-reviewed contrary evidence
```

Dialogue datasets, synthetic therapy sessions and LLM-generated Socratic conversations are design evidence only. They do not establish therapeutic efficacy, safety or clinician equivalence.

## Production policy

Only records with `review_status: approved` may enter a tagged production release. Draft and candidate records may support internal review and website-preview development only.

The production website must import a pinned release rather than reading the latest branch dynamically.

Every published route should retain:

```text
ontology_version
evidence_registry_version
route_engine_version
product_availability_version
copy_version
```
