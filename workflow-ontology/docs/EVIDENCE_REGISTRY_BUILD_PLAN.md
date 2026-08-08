# Evidence Registry Build Plan

**Version:** draft v0.2.0  
**Status:** implementation plan  
**Owner:** HRP Transfer Lab  
**Applies to:** `workflow-ontology/evidence/`

## 1. Purpose

Build a versioned, claims-safe evidence table before implementing the IQMindware.com Cognitive Route Builder.

The evidence system must support:

```text
user goal or workflow demand
→ cognitive function
→ current product route
→ measurement plan
→ evidence status
→ approved public claim
→ required caveat
```

It must also support the planned full stack:

```text
Attention Control
→ Relational Memory
→ Binding Memory
→ Path Prediction
→ Reasoning
```

crossed with:

```text
Signal
Evidence
Predictive Calibration
Commit
```

Predictive Calibration remains a cross-cutting derived profile. It is not a fourth public game.

## 2. Located evidence assets

The repository contains:

```text
evidence/evidence-sources.json
evidence/evidence-claims.json
evidence/measurement-registry.json
evidence/training-fit-mappings.json
evidence/vertical-stack-mode-matrix.candidate.json
evidence/vertical-stack-sources.candidate.json
docs/EVIDENCE_GRADING.md
```

The first four files form the current canonical evidence layer. The vertical-stack files are candidate review assets and must not enter production automatically.

Two human-readable source documents supplied for this build are tracked in `evidence/reviews/SOURCE_DOCUMENTS.md`:

```text
IQM_Training_Fit_Evidence_Registry_v0.2.md
IQM_Stack_Evidence_v0.1_DISCOVERY.md
```

Active research reviews include:

```text
evidence/reviews/GT_ATTENTION_ZONE_EVIDENCE_REVIEW_v0.1.md
evidence/reviews/FULL_VERTICAL_STACK_MODE_EVIDENCE_REVIEW_v0.1.md
```

## 3. Import hierarchy

### Tier A — reviewed seed

`IQM_Training_Fit_Evidence_Registry_v0.2.md`

Use for:

- G Track measurement claims;
- MFT-M and Attention Coach claims;
- claims boundaries;
- initial clinical-adjacent wording;
- source bibliography.

### Tier B — discovery backlog

`IQM_Stack_Evidence_v0.1_DISCOVERY.md`

Use for:

- candidate functions;
- candidate populations and niches;
- possible future partner routes;
- literature-search priorities.

Do not directly import its `High`, `Moderate` or commercial-priority labels. Some rows refer to evidence for a broad intervention category rather than the exact IQ Mindware protocol.

### Tier C — full-stack candidate review

Use the full vertical-stack review and candidate matrix to:

- define the 20 capacity-by-mode cells;
- separate construct evidence from exact-protocol evidence;
- identify current, development and research-only routes;
- distinguish formal reasoning, belief calibration and domain-semantic applications;
- build a prepublication watchlist;
- prioritise validation studies.

Candidate files must be translated into atomic source, claim, protocol and mapping records before approval.

## 4. First production scope

Complete current live products before future or clinical-adjacent modules.

### G Track

- SART engagement and response control;
- Stroop;
- Flanker;
- combined attention profile;
- provisional Zone context;
- complex-span-style working memory;
- visual working-memory binding;
- OMIB Matrix Reasoning;
- baseline/follow-up interpretation.

### Attention Coach

- classic masked MFT-M Signal Control;
- selected attention-task transfer;
- verbal-learning acquisition signal;
- everyday-focus boundary;
- relative-frame and optic-flow extensions as principled, unvalidated extensions.

### WM Coach

- Relational Memory Signal;
- Binding Memory Signal;
- wrong-lag and partial-match/swap lure targets;
- general working-memory transfer;
- explicit conflicting evidence and far-transfer boundary.

## 5. Full-stack research scope

The next evidence programme covers:

| Capacity | Signal | Evidence | Predictive Calibration | Commit |
|---|---|---|---|---|
| **Attention Control** | Current commercial anchor | In development | Derived profile | In development |
| **Relational Memory** | Current commercial anchor | In development | Derived profile | In development |
| **Binding Memory** | Current commercial anchor | In development | Derived profile | In development |
| **Path Prediction** | In development | In development | Derived profile | In development |
| **Reasoning** | In development | In development | Derived belief-calibration profile | In development |

Reasoning must retain three wrappers:

```text
symbolic
nonsense-semantic
domain-semantic verbal
```

and three distinct application classes:

```text
formal reasoning and validity
professional belief calibration
non-clinical evidence-sensitive reframing
```

Health-related interpretation-bias or reappraisal protocols remain partner/research-only.

## 6. Evidence dimensions

Every mapping should retain:

```text
construct_basis_level
measurement_source_level
exact_implementation_level
training_benefit_level
cross_layer_or_workflow_transfer_level
governance_eligibility
product_availability
publication_status
review_status
```

## 7. Evidence-level interpretation

```text
strong
multiple direct studies, a strong synthesis, a validated item bank,
or a mature computational/experimental literature

moderate
one directly relevant study or several close studies

plausible_but_not_established
defensible mechanism or adjacent evidence without a direct test

insufficient
current evidence does not support the claim

not_eligible
diagnostic, treatment, selection or guaranteed-effect claim outside intended use
```

## 8. Key regrading decisions

### Working-memory evidence

The broad stack document describes working-memory updating as `High`.

For product claims, this must be decomposed. The 2024 Rodas review reports small overall improvement on working-memory outcomes, much larger apparent effects when assessment tasks resemble training, and no supported fluid-intelligence improvement. Controlled evidence also includes findings against broad updating and binding transfer.

The website-ready judgement is therefore:

```text
working-memory mechanism fit:
strong

general untrained WM benefit:
moderate / small

exact WM Coach benefit:
not yet independently established

fluid-intelligence transfer:
not established
```

### Attention evidence

```text
MFT-M mechanism fit:
strong

direct MFT-M training evidence:
moderate / emerging

selected attention-task and verbal-learning transfer:
initial controlled evidence

sustained everyday focus:
plausible, not established
```

### Path Prediction evidence

```text
successor-representation and transition-learning basis:
strong

exact IQ Mindware path task:
not established

training benefit and workflow transfer:
not established
```

### Explicit reasoning evidence

```text
formal reasoning, relational integration and belief-bias basis:
strong

argument-mapping and structured-instruction evidence:
moderate / heterogeneous

exact graph-to-language Reasoning Coach protocol:
not established

professional judgement transfer:
not established
```

### Belief calibration evidence

```text
metacognitive and confidence-measurement basis:
strong

adaptive metacognitive-training signal:
moderate

exact Reasoning Coach belief-calibration profile:
not established
```

### Reframing evidence

```text
stress-reappraisal and reappraisal-category evidence:
moderate / heterogeneous

non-clinical evidence-sensitive reframing route:
pilot-ready hypothesis

clinical or treatment use:
partner/research only
```

### Clinical-adjacent evidence

Evidence for a broad category such as ADHD cognitive training, anxiety-related working-memory training, reappraisal or cognitive remediation does not become evidence for the exact IQ Mindware app.

Clinical-adjacent records must keep separate:

```text
category evidence
→ function relevance
→ exact product evidence
→ governance route
```

## 9. Phased build

### Phase 1A — current-product evidence

Deliver:

```text
evidence-sources.json
evidence-claims.json
measurement-registry.json
training-fit-mappings.json
```

### Phase 1B — full-stack candidate evidence

Deliver:

```text
FULL_VERTICAL_STACK_MODE_EVIDENCE_REVIEW_v0.1.md
vertical-stack-mode-matrix.candidate.json
vertical-stack-sources.candidate.json
```

Then translate approved candidate material into:

```text
atomic sources
atomic claims
protocol records
mode-specific mappings
application records
prepublication watchlist
```

### Phase 2 — workflow evidence

Add:

```text
workflow-demand claims
function-mapping claims
person-versus-system alternatives
workflow outcomes
pilot-ready route status
```

### Phase 3 — governed application evidence

Create separate governed registries for:

```text
health and care pathways
interpretation-bias research
reappraisal or health-psychology protocols
clinical-adjacent populations
```

Do not mix category-level clinical evidence into ordinary self-service product claims.

### Phase 4 — results registry

Add app and pilot results by immutable protocol and model version:

```text
trained-task outcome
separate cognitive outcome
cross-layer outcome
workflow outcome
delayed outcome
null or adverse finding
limitations
```

### Phase 5 — website export

Build a release bundle containing only approved records:

```text
evidence-sources.json
evidence-claims.json
measurement-registry.json
training-fit-mappings.json
approved full-stack mappings
release-manifest.json
checksums
```

## 10. Review gates

A record cannot become `approved` until reviewers have checked:

1. construct clarity;
2. source accuracy;
3. publication status;
4. directness to the exact product;
5. alternative explanations;
6. claims wording;
7. caveat sufficiency;
8. product availability;
9. governance;
10. outcome measurability;
11. conflicting or null evidence;
12. cross-layer and workflow-transfer status.

## 11. Immediate work queue

1. Review the ten G Track measurement records.
2. Review the fifteen initial training-fit mappings.
3. Review the 20 candidate capacity-by-mode cells.
4. Verify source metadata and effect-size wording.
5. Convert candidate full-stack sources into the canonical source schema.
6. Create atomic claims for Path Prediction, explicit reasoning, belief calibration and reframing.
7. Add exact WM Coach implementation metadata.
8. Add relative-frame and optic-flow Attention Coach records.
9. Define protocol records for Evidence and Commit modes.
10. Add a formal prepublication-watchlist schema and review cadence.
11. Build product-availability and public-copy overlays outside the canonical science records.
12. Build workflow mappings only after the current-product evidence base is stable.
13. Move approved records into the first tagged evidence release.
