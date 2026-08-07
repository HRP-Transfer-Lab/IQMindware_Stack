# Evidence Grading

## Why several evidence judgements are needed

A workflow route may be highly relevant to a user’s goal while having limited direct training evidence. The registry therefore keeps separate judgements for:

1. **Workflow-demand support** — evidence that the workflow genuinely places the stated demand on users.
2. **Function mapping** — evidence that the demand or friction implicates the proposed cognitive function.
3. **Measurement/source validity** — evidence supporting the task, item bank or paradigm.
4. **Exact implementation validity** — evidence for the specific digital implementation and scoring model.
5. **Training-benefit evidence** — evidence that training changes a separate outcome.
6. **Workflow-transfer evidence** — evidence that change reaches the functional or organisational outcome.

These must not be collapsed into one “science-backed” score.

## Public evidence levels

| Level | Definition |
|---|---|
| **Strong** | Multiple direct studies, a high-quality synthesis, or a validated item bank supports substantially the same construct or mapping. |
| **Moderate** | At least one directly relevant study, or several reasonably close studies, support the mapping. |
| **Plausible but not established** | No direct test of the exact mapping; a defensible mechanism, adjacent evidence or original protocol rationale exists. |
| **Insufficient** | The current evidence does not support a recommendation or public benefit statement. |
| **Not an eligible claim** | The proposed interpretation would imply diagnosis, treatment, high-stakes selection or a guaranteed effect outside intended use. |

## Evidence-status tags

Machine-readable records may use:

```text
published_anchor
adapted_published_model
principled_extension
internal_calibration
pilot_supported
controlled_validation
deployment_validation
conflicting_evidence
implementation_unvalidated
not_clinical_support
```

## Evidence-source requirements

Each source record should include:

```text
source_id
citation
doi_or_url
study_type
population
constructs
outcomes
limitations
review_status
last_reviewed
```

Each claim or mapping must point to one or more `source_id` values or explicitly state that it is a theory-led, expert-derived or pilot-derived hypothesis.

## Workflow evidence sources

Workflow-demand records may draw on:

- peer-reviewed occupational, educational, health or human-factors research;
- formal workflow or service documentation;
- task analysis and process mapping;
- interviews or workshops with workflow participants;
- observational or administrative data;
- pilot data.

The source type and confidence must be retained.

## Claims rule

A public statement must never be stronger than the weakest essential link in its chain.

Example:

```text
Strong workflow-demand evidence
+ strong function fit
+ moderate training evidence
+ no workflow-transfer study
=
moderate cognitive-training rationale,
workflow benefit not established
```

## Review procedure

Before approval, a mapping should be reviewed for:

1. construct clarity;
2. workflow specificity;
3. alternative explanations;
4. person-versus-system attribution;
5. product availability;
6. claims wording;
7. governance implications;
8. measurable outcomes.

Only approved mappings may enter a tagged production release.
