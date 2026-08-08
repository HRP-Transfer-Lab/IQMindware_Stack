# Evidence Registry Build Plan

**Version:** draft v0.1.0  
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

## 2. Located evidence assets

The repository contains:

```text
evidence/evidence-sources.json
evidence/evidence-claims.json
evidence/measurement-registry.json
evidence/training-fit-mappings.json
docs/EVIDENCE_GRADING.md
```

The first two files were the original canonical evidence assets. The measurement and training-fit registries add the website-ready layer while preserving atomic source and claim records.

Two human-readable source documents supplied for this build are tracked in `evidence/reviews/SOURCE_DOCUMENTS.md`:

```text
IQM_Training_Fit_Evidence_Registry_v0.2.md
IQM_Stack_Evidence_v0.1_DISCOVERY.md
```

The source documents should be imported in full only after their naming, references and evidence labels have been reviewed. Their current role is evidence-review provenance rather than production runtime data.

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

## 5. Evidence dimensions

Every mapping should retain:

```text
mechanism_fit_level
measurement_source_level
exact_implementation_level
training_benefit_level
workflow_transfer_level
governance_eligibility
product_availability
review_status
```

## 6. Evidence-level interpretation

```text
strong
multiple direct studies, a strong synthesis, or a validated item bank

moderate
one directly relevant study or several close studies

plausible_but_not_established
defensible mechanism or adjacent evidence without a direct test

insufficient
current evidence does not support the claim

not_eligible
diagnostic, treatment, selection or guaranteed-effect claim outside intended use
```

## 7. Key regrading decisions

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

### Clinical-adjacent evidence

Evidence for a broad category such as ADHD cognitive training, anxiety-related working-memory training or cognitive remediation does not become evidence for the exact IQ Mindware app.

Clinical-adjacent records must keep separate:

```text
category evidence
→ function relevance
→ exact product evidence
→ governance route
```

## 8. Phased build

### Phase 1 — current-product evidence

Deliver:

```text
evidence-sources.json
evidence-claims.json
measurement-registry.json
training-fit-mappings.json
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

### Phase 3 — clinical-adjacent evidence

Create a separate governed registry. Do not mix clinical-adjacent category evidence into ordinary self-service product claims.

### Phase 4 — results registry

Add app and pilot results by immutable protocol and model version:

```text
trained-task outcome
separate cognitive outcome
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
release-manifest.json
checksums
```

## 9. Review gates

A record cannot become `approved` until reviewers have checked:

1. construct clarity;
2. source accuracy;
3. directness to the exact product;
4. alternative explanations;
5. claims wording;
6. caveat sufficiency;
7. product availability;
8. governance;
9. outcome measurability;
10. conflicts or null evidence.

## 10. Immediate work queue

1. Review the ten G Track measurement records.
2. Review the fifteen initial training-fit mappings.
3. Verify source metadata and effect-size wording.
4. Add exact WM Coach implementation metadata.
5. Add relative-frame and optic-flow Attention Coach records.
6. Add product-availability and public-copy overlays outside the canonical science records.
7. Build workflow mappings only after the current-product evidence base is stable.
8. Move approved records into the first tagged evidence release.
