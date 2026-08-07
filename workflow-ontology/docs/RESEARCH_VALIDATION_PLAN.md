# Workflow Ontology Research and Validation Plan

**Version:** draft v0.1.0  
**Status:** canonical programme plan  
**Owner:** HRP Transfer Lab  
**Applies to:** `workflow-ontology/`  
**Scientific anchor:** Adaptive Predictive Control Intervention Framework  

---

## 1. Purpose

This document defines the staged research programme required to turn the Cognitive Workflow Ontology from a theoretically structured routing system into an evidence-backed basis for website recommendations, organisational pilots and later workflow integration.

The ontology currently represents the chain:

```text
niche
→ workflow
→ workflow stage
→ cognitive demand
→ observed friction
→ intervention locus
→ cognitive function
→ protocol route
→ outcome plan
→ governance profile
```

The central research problem is that each arrow in this chain is a separate empirical claim. A workflow may be accurately described even when the cognitive mapping is uncertain. A cognitive function may be relevant even when the current app has not been validated for that function. A protocol may improve an app-native score without improving the intended workflow outcome.

The ontology must therefore avoid one undifferentiated evidence label. It must preserve separate confidence judgements for:

1. the workflow representation;
2. the cognitive demands attributed to the workflow stage;
3. the mapping from demands and frictions to cognitive functions;
4. the fit and validity of the implemented protocol;
5. change in separate workflow outcomes;
6. implementation readiness in the target niche.

The governing principle is:

> **Do not treat a plausible workflow-to-app route as an established intervention effect. Validate the chain in stages, preserve uncertainty and abstain when the evidence is insufficient.**

---

## 2. Why this is the first research programme

The website route builder can be technically deterministic and still be scientifically weak if it simply translates a user complaint into whichever app is currently available.

The first research programme should therefore establish whether the ontology:

- represents real workflows accurately;
- identifies the correct critical stages;
- captures the cognitive demands that matter at those stages;
- distinguishes person-level limitations from avoidable task, interface, team or organisational problems;
- maps demands and friction signatures to defensible APC functions;
- selects appropriate outcomes and governance routes;
- recognises when the relevant protocol is unavailable or unvalidated;
- abstains instead of over-recommending.

The first research question is not yet:

> Does Attention Coach improve AI-output verification?

It is:

> **Have we represented the workflow accurately, identified the right cognitive demands, selected defensible intervention loci and created a route that practitioners, users and cognitive experts recognise as relevant and claims-safe?**

---

## 3. Validation objects

The programme validates six related but distinct objects.

| Code family | Validation object | Core question |
|---|---|---|
| **W** | Workflow representation | Is this an accurate account of the real workflow and critical stage? |
| **D** | Cognitive-demand mapping | Does the stage genuinely impose the stated cognitive demands? |
| **F** | Cognitive-function mapping | Are those demands and frictions meaningfully related to the proposed APC functions and capacities? |
| **P** | Protocol fit | Does the current IQ Mindware task validly exercise the relevant function? |
| **O** | Workflow outcome evidence | Does the route improve a separate functional or workflow outcome? |
| **I** | Implementation readiness | Can the route be used acceptably, feasibly, safely and sustainably in the niche? |

These codes should be stored independently. They must not be averaged into one opaque evidence percentage.

---

# 4. Confidence model

## 4.1 W — Workflow representation

| Level | Label | Definition |
|---:|---|---|
| **W0** | Draft hypothesis | Workflow stage inferred from general knowledge or theory only. |
| **W1** | Documented | Supported by an authoritative workflow source or several credible descriptions. |
| **W2** | Practitioner-confirmed | Confirmed through structured expert review, interviews or walkthroughs. |
| **W3** | Field-observed | Supported by direct observation, task traces, artefacts or think-aloud performance. |
| **W4** | Replicated | Observed across more than one organisation, course, service or comparable setting. |

## 4.2 D — Cognitive-demand mapping

| Level | Label | Definition |
|---:|---|---|
| **D0** | Theoretical | Derived from APC, cognitive theory or analyst judgement only. |
| **D1** | Literature-grounded | Relevant human-factors, cognitive or domain literature supports the demand. |
| **D2** | Expert content-validated | Domain and cognitive experts judge the demand relevant and sufficiently comprehensive. |
| **D3** | Behaviourally supported | Demand ratings predict relevant errors, workload, latency or task performance. |
| **D4** | Experimentally supported | Manipulating the demand produces the predicted behavioural effect. |

## 4.3 F — Cognitive-function mapping

| Level | Label | Definition |
|---:|---|---|
| **F0** | Plausible | Conceptual APC mapping with no direct validation. |
| **F1** | Convergent rationale | Related cognitive and human-factors evidence supports the proposed function. |
| **F2** | Expert-reviewed | Domain, cognitive and human-factors experts endorse the mapping and alternatives have been considered. |
| **F3** | Prospectively predictive | Function-specific measures predict the relevant workflow outcome in a held-out or prospective sample. |
| **F4** | Externally replicated | The predictive mapping holds in a new sample, workflow or organisation. |

## 4.4 P — Protocol fit

| Level | Label | Definition |
|---:|---|---|
| **P0** | No implemented protocol | The function is identified but no relevant live app mode exists. |
| **P1** | Construct-aligned | The current task plausibly exercises the target function. |
| **P2** | Exact implementation characterised | Reliability, data quality and construct validity of the implemented app have been studied. |
| **P3** | Separate cognitive transfer supported | Training changes an untrained function-relevant measure. |
| **P4** | Functional transfer supported | Training contributes to improvement on the intended workflow task. |

## 4.5 O — Workflow outcome evidence

| Level | Label | Definition |
|---:|---|---|
| **O0** | Untested | Outcome identified but not studied. |
| **O1** | Feasibility evidence | The route and outcome can be delivered and measured. |
| **O2** | Pilot-supported | Pre/post or repeated-measures evidence suggests improvement. |
| **O3** | Controlled evidence | An active-control, factorial or randomised comparison supports a functional effect. |
| **O4** | Replicated deployment evidence | The effect replicates, persists after delay and survives routine implementation. |

## 4.6 I — Implementation readiness

| Level | Label | Definition |
|---:|---|---|
| **I0** | Governance unresolved | Intended use, data roles, access or decision rights are not sufficiently specified. |
| **I1** | Governance-defined | Intended use, data relationships, access, claims and escalation boundaries are specified. |
| **I2** | Acceptable and feasible | Relevant stakeholders judge the route acceptable, appropriate and feasible. |
| **I3** | Implementable | Adoption, fidelity, burden, cost and integration requirements have been evaluated. |
| **I4** | Sustainable | Maintenance, equity and routine integration have been demonstrated. |

## 4.7 Interpretation rule

A route can have different confidence levels across the six dimensions.

Example:

```text
AI-output verification

W2  Practitioner-confirmed workflow
D1  Literature-grounded cognitive demands
F1  Convergent cognitive-function rationale
P1  Current apps are construct-aligned foundations
O0  Workflow improvement not yet tested
I1  Governance route defined
```

This should not be compressed to “moderate evidence”.

---

# 5. Public evidence translation

The website should translate the internal evidence profile into plain-language status labels.

| Internal evidence state | Suggested public wording |
|---|---|
| W0/D0/F0 | **Research hypothesis** |
| W1 and relevant literature | **Source-grounded** |
| W2/D2/F2 | **Expert-reviewed** |
| F3 or D3 | **Field-supported mapping** |
| O2 | **Pilot-supported** |
| O3 | **Controlled evidence** |
| O4/I4 | **Deployment-validated** |

A public route should show at least four distinct statements:

```text
Workflow basis
Cognitive-function mapping
Current protocol fit
Workflow outcome evidence
```

Example:

> This route is based on a documented workflow and an expert-reviewed cognitive mapping. The current apps target relevant foundational functions, but improvement in the intended workflow outcome has not yet been established.

---

# 6. Research phases

## Phase 0 — Technical and conceptual validation

### Purpose

Confirm that the ontology is internally coherent and can answer the questions required by the website and research programme.

### Required work

1. Define competency questions.
2. Validate identifiers, references, ranges and governance constraints.
3. Add the six-part evidence profile to workflow-stage records.
4. Define abstention rules.
5. Test whether the ontology distinguishes person-level training from task, interface, team and system redesign.
6. Test whether unavailable modules are reported as unavailable rather than silently replaced.
7. Review all draft records for category errors and broken mappings.

### Initial competency questions

```text
Given a workflow stage, can the ontology return:
- its niche and workflow family;
- its demand profile;
- likely friction signatures;
- all plausible intervention loci;
- relevant APC capacities and functions;
- current and future protocol coverage;
- suitable cognitive, functional and workflow outcomes;
- the correct governance profile;
- the evidence and confidence profile;
- a clear abstention when evidence is insufficient?
```

### Outputs

- competency-question registry;
- evidence-profile schema;
- abstention rules;
- ontology-integrity tests;
- corrected v0.1 draft records.

### Gate to Phase 1

All current records pass structural validation, every mapping has provenance or an explicit `no_direct_source` status, and no health-related record can resolve to an ungoverned consumer treatment route.

---

## Phase 1 — Workflow evidence review

### Purpose

Establish what the workflow is, where the important stages occur, what information must be maintained and what outcomes matter.

### Evidence sources

- standard operating procedures;
- workflow manuals and process maps;
- educational assessment instructions;
- research-method guidance;
- role and competency descriptions;
- interface and artefact examples;
- quality-assurance and error reports;
- human-factors and ergonomics studies;
- observational and process studies;
- relevant implementation and service documents.

### Review unit

Use the smallest coherent unit that supports a workflow claim, normally a passage, task segment or documented stage.

### Required extraction fields

```text
workflow claim
workflow stage
actor
input
required output
decision or action
constraints
known failure modes
reported outcomes
source type
source population
directness
limitations
reviewer
```

### Output

A workflow evidence table for each target workflow, separating direct workflow evidence from theoretical cognitive interpretation.

### Gate to Phase 2

Each selected workflow has a documented stage model, a bounded evidence corpus and an explicit list of unresolved tacit-work questions.

---

## Phase 2 — Cognitive task analysis

### Purpose

Elicit the tacit knowledge, cues, judgements, options and re-entry requirements that documents do not capture.

### Candidate methods

- workflow walkthroughs;
- direct or screen-based observation;
- think-aloud task performance;
- artefact elicitation;
- critical-incident interviews;
- Critical Decision Method interviews;
- comparison of experienced and developing performers;
- stimulated recall using task traces or recordings.

### Initial sampling target

For each workflow, begin with approximately:

```text
6–10 experienced performers
6–10 typical or developing performers
several observed or simulated task episodes
```

This is a pragmatic starting target, not a powered efficacy sample. Continue or stop based on information power, recurrence of the workflow model and whether substantively new demands or frictions continue to emerge.

### Core questions

```text
What information must be noticed?
What must remain active?
What relations and dependencies matter?
What belongs with what?
What changes over time?
What future path must be anticipated?
What evidence is sufficient?
What produces premature closure?
What produces excessive checking?
What is caused by the person?
What is caused by the interface, process or system?
What outcome would count as a genuine improvement?
```

### Outputs

- revised workflow-stage maps;
- observed demand and friction signatures;
- intervention-locus hypotheses;
- critical-event and decision-point inventory;
- candidate functional and workflow outcomes.

### Gate to Phase 3

The workflow model is recognisable to performers, captures the critical stages and has an explicit account of alternative person and system explanations.

---

## Phase 3 — Expert content validation

### Purpose

Assess relevance, comprehensiveness, comprehensibility, specificity and claims safety of the proposed ontology mappings.

### Panel composition

The panel should include, where appropriate:

- practitioners from the target niche;
- cognitive psychologists or neuroscientists;
- human-factors specialists;
- implementation researchers;
- end-user representatives;
- governance, safeguarding or clinical expertise for consequential routes.

### Rating domains

Experts rate each workflow stage, demand, friction and mapping for:

```text
relevance
comprehensiveness
comprehensibility
specificity
alternative explanations
intervention locus
outcome suitability
governance fit
claims safety
```

### Quantitative summaries

Possible summaries include:

- item-level content-validity index;
- scale-level average content-validity index;
- Aiken’s V;
- chance-corrected agreement;
- inter-rater agreement for categorical mappings;
- qualitative consensus and dissent logs.

Provisional review gates such as an item-level CVI around `.78` and a scale-level average around `.90` may be used as prompts for review, not as proof that a mapping is empirically true.

### Required alternative-explanation test

For every person-level cognitive mapping, experts must consider whether the friction may be better explained by:

- interface design;
- excessive workload or interruption;
- missing information;
- unclear authority;
- poor domain knowledge;
- inappropriate incentives;
- team coordination;
- organisational policy;
- emotional or health context;
- measurement artefact.

### Outputs

- expert rating dataset;
- consensus log;
- revised coding manual;
- evidence-profile updates;
- ontology v0.2 candidate.

### Gate to Phase 4

The workflow and demand model passes the agreed content-validity review, dissent is recorded, and unsupported cognitive mappings remain labelled as hypotheses.

---

## Phase 4 — Behavioural and predictive validation

### Purpose

Test whether the mapped demands and cognitive functions predict relevant workflow behaviour.

### Example: AI-output verification

Manipulate or measure:

- source density;
- contradiction frequency;
- interruptions;
- time pressure;
- plausibility of unsupported claims;
- number of context switches;
- decision reversibility.

Measure:

- unsupported claims detected;
- source-attribution errors;
- false alarms;
- review time;
- interruption re-entry time;
- confidence and calibration;
- premature release;
- excessive checking.

### Candidate preregistered predictions

```text
G Track attention measures predict signal-loss and distractor errors.

G Track binding performance predicts source–claim swap errors.

Relational Memory performance predicts loss of dependencies and task structure.

Evidence and Commit measures, once available, predict stale-model persistence,
premature release and excessive review.
```

### Design requirements

- prespecified primary outcomes;
- held-out or prospective validation sample;
- no tuning and testing on the same cases;
- explicit competing explanations;
- timing and data-quality controls;
- separate modelling of person and workflow variables;
- uncertainty and abstention reporting.

### Output

Evidence for or against the chain:

```text
workflow demand
→ cognitive function
→ measurable workflow performance
```

### Gate to Phase 5

At least one mapped cognitive function predicts a relevant held-out workflow outcome above appropriate baselines, or the mapping is revised or rejected.

---

## Phase 5 — Intervention validation

### Purpose

Test whether a configured route causes improvement in separate cognitive and workflow outcomes.

### Preferred comparative design

Where feasible, compare:

| Condition | Purpose |
|---|---|
| Measurement or active control | Estimate change without the targeted intervention. |
| Workflow redesign only | Test task, interface or process support. |
| Cognitive training only | Test the person-level protocol route. |
| Combined route | Test training plus workflow support. |

### Outcome hierarchy

```text
app learning
→ separate cognitive measure
→ simulated functional task
→ real workflow outcome
→ delayed persistence
→ implementation outcome
```

### Important distinction

A positive app-learning result is not evidence of workflow transfer. A positive cognitive-measure result is not automatically evidence of organisational value.

### Gate to Phase 6

A route shows an interpretable benefit on a prespecified separate outcome, with acceptable burden and no serious claims or governance concern.

---

## Phase 6 — Deployment validation

### Purpose

Determine whether the route remains useful, governable and sustainable in routine delivery.

### Implementation outcomes

Assess separately:

- acceptability;
- appropriateness;
- feasibility;
- adoption;
- fidelity;
- participant burden;
- practitioner or manager burden;
- cost;
- equity and accessibility;
- privacy and trust;
- penetration;
- maintenance;
- unintended effects.

### Deployment evidence

A deployment-validated route should show:

```text
acceptable implementation
+ stable protocol delivery
+ interpretable outcome evidence
+ appropriate governance
+ delayed persistence or maintenance
+ no unsupported consequential use
```

---

# 7. First study

## Proposed title

**Development and Content Validation of a Cognitive Workflow Demand Ontology for AI-Assisted Knowledge Work and Higher Education**

## Initial workflow stages

1. Verify an AI-generated report before release.
2. Recover a complex task after interruption.
3. Integrate sources into an evidence-based assignment.
4. Screen studies against eligibility criteria.

These cases provide useful variation across niches while allowing repeated demands such as attention selection, relation maintenance, source binding, vigilance and re-entry to be compared.

## Aims

### Aim 1

Establish whether the workflow stages, demand dimensions and friction signatures are relevant and sufficiently comprehensive.

### Aim 2

Assess agreement on mappings from demands and frictions to APC capacities and functions.

### Aim 3

Assess agreement on person-, task/interface-, team/process- and organisation/system-level intervention loci.

### Aim 4

Test whether the ontology produces sensible, availability-aware and claims-safe routes for held-out workflow cases.

## Study sequence

```text
bounded evidence review
→ cognitive task analysis
→ draft coding manual
→ independent double-coding
→ multidisciplinary expert panel
→ content-validity and agreement analysis
→ held-out route cases
→ revised ontology v0.2
```

## Principal outputs

- validated workflow coding manual;
- revised ontology and evidence profiles;
- paper or preprint;
- public methods export;
- expert-reviewed expected-route cases;
- production-ready website ontology release;
- explicit register of mappings that remain hypotheses.

The operational study scaffold is stored under:

```text
workflow-ontology/studies/001-content-validation/
```

---

# 8. Repository changes required during the programme

## 8.1 Evidence profile field

Each workflow-stage record should gain a structured profile such as:

```json
{
  "evidence_profile": {
    "workflow": "W1",
    "demand": "D0",
    "function_mapping": "F0",
    "protocol_fit": "P1",
    "workflow_outcome": "O0",
    "implementation": "I1"
  }
}
```

## 8.2 Review metadata

Each mapping should retain:

```text
review_status
reviewed_by
review_date
review_method
source_ids
alternative_explanations
consensus_status
dissent_note
next_required_evidence
```

## 8.3 Planned study tree

```text
workflow-ontology/
├── studies/
│   ├── 001-content-validation/
│   ├── 002-behavioural-validation/
│   └── 003-intervention-pilot/
├── reviews/
├── preregistrations/
└── docs/
    ├── RESEARCH_VALIDATION_PLAN.md
    ├── CODING_MANUAL.md
    ├── CONTENT_VALIDITY_PROTOCOL.md
    └── CONFIDENCE_MODEL.md
```

The current document is the canonical programme-level plan. Study-specific protocols should not silently modify it; material changes require a versioned update and changelog entry.

---

# 9. Website use during validation

The route builder may be used before intervention trials are complete, provided the wording follows the evidence profile.

## Before expert validation

> **Research hypothesis:** This route is based on a theoretical mapping between the workflow demand and the cognitive function.

## After evidence review

> **Source-grounded:** The workflow demand is documented in relevant research or practice materials.

## After content validation

> **Expert-reviewed:** Domain and cognitive experts judged this mapping relevant and sufficiently complete.

## After behavioural validation

> **Field-supported:** The mapped cognitive measures predicted relevant workflow performance.

## After a pilot

> **Pilot-supported:** Initial evidence suggests that the route may improve selected outcomes.

## After controlled and replicated evaluation

> **Controlled evidence** or **Deployment-validated**.

The website should always display separately:

```text
workflow evidence
cognitive-function evidence
protocol evidence
workflow-outcome evidence
```

---

# 10. Abstention and revision rules

The ontology should abstain or return a research-only route when:

- the workflow stage is insufficiently specified;
- evidence supports several competing cognitive mappings with no basis for selection;
- a system-level problem is likely to dominate person-level variation;
- the relevant protocol does not exist;
- the route would imply diagnosis or treatment without an approved pathway;
- the proposed outcome cannot be measured defensibly;
- the data would be used for selection, discipline or covert ranking;
- timing, adherence or data quality is inadequate;
- the mapping fails behavioural or external validation.

A failed hypothesis should produce:

```text
retain the source record
→ mark the mapping unsupported or retired
→ document the failed prediction
→ update the ontology version
→ preserve the historical website release
```

---

# 11. Immediate work order

## Priority 1 — Phase 0

- add evidence profiles to the schema;
- create competency questions;
- repair current category and reference errors;
- add abstention tests;
- validate health-governance boundaries;
- confirm that all records distinguish function relevance from product availability.

## Priority 2 — First study protocol

- freeze the four initial workflow cases;
- create the bounded review strategy;
- draft the coding manual;
- draft practitioner and cognitive-expert interview guides;
- define expert rating forms;
- preregister aims, exclusions and analysis rules.

## Priority 3 — Website release preparation

- permit only `source-grounded` or `expert-reviewed` mappings to appear as normal recommendations;
- label theoretical mappings explicitly;
- show unavailable target functions as in development;
- display both cognitive-support and workflow-support routes;
- retain the ontology and evidence versions with every recommendation.

---

# 12. Methodological anchors

The programme should draw on the following method families as appropriate:

- ontology competency questions, consistency and task-based evaluation;
- cognitive task analysis and cognitive work analysis;
- Critical Decision Method and critical-incident interviewing;
- content-validity methods focused on relevance, comprehensiveness and comprehensibility;
- transparent Delphi or consensus-reporting guidance;
- psychometric and behavioural predictive validation;
- held-out and prospective model testing;
- complex-intervention development and evaluation;
- implementation outcomes including acceptability, appropriateness, feasibility, fidelity, cost and sustainability;
- preregistration, versioned protocols and reproducible reporting.

The choice of a named instrument or threshold must be justified in each study protocol. Methodological thresholds are review aids, not substitutes for substantive evidence.

---

# 13. Definition of programme success

The research programme succeeds when:

1. real users and practitioners recognise the workflow models;
2. experts judge the demand and function mappings relevant and sufficiently complete;
3. the ontology distinguishes cognitive-support opportunities from workflow-design problems;
4. function-specific measures predict at least some held-out workflow outcomes;
5. unsupported mappings are rejected or revised rather than protected;
6. intervention studies separate app learning, cognitive change and workflow change;
7. deployment studies show acceptable, governable and sustainable use;
8. website evidence labels accurately represent the maturity of each claim;
9. every released route remains reproducible from versioned ontology, evidence, availability and copy records;
10. null, mixed and unfavourable findings are retained in the public research history.

The intended endpoint is not a marketing taxonomy. It is a progressively validated workflow–demand–intervention knowledge system that can support defensible website routing, bounded organisational pilots and later workflow integration.
