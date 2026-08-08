# Cognitive Workflow Ontology

**Version:** draft v0.1.0  
**Status:** research and website-routing ground truth  
**Owner:** HRP Transfer Lab  

This directory defines a versioned ontology linking real organisational, educational and health-pathway workflows to cognitive demands, observed friction signatures, intervention loci, IQ Mindware functions, evidence status and outcome plans.

The core mapping is:

```text
niche
→ workflow
→ workflow stage
→ demand profile
→ observed friction
→ intervention locus
→ cognitive function
→ protocol route
→ outcome plan
→ governance profile
```

The ontology is designed to support:

- the IQMindware.com deterministic Cognitive Route Builder;
- organisational and education pilot design;
- research and validation studies;
- later programme dashboards and workflow integrations;
- versioned public methods and claims-safe reporting.

## Scientific architecture

The cognitive-function layer follows the Adaptive Predictive Control architecture:

```text
Attention Control
Structured Working Memory
├─ Relational Memory
└─ Binding Memory
Predictive Inference
├─ Path Prediction
└─ Reasoning
```

Across these capacities, the recurring intervention functions are:

```text
Signal
Evidence
Predictive Calibration
Commit
```

Predictive Calibration is mainly estimated across Evidence and Commit rather than treated as a separate game.

## Important boundary

The ontology does not diagnose individuals and does not assume that every workflow failure should be solved through individual training. Each route must consider four possible intervention loci:

```text
person
task / interface
team / process
organisation / system
```

Where avoidable workflow design is the primary source of cognitive strain, redesign should take priority over training.

## Current product availability

The ontology may identify functions whose product modules are not yet available. Product availability is applied by the commercial website layer, not encoded as scientific truth here.

Current IQ Mindware coverage includes:

- G Track measurement: attention, working memory, OMIB matrix reasoning and provisional zone context;
- Attention Coach Signal Control;
- WM Coach Relational Memory Signal;
- WM Coach Binding Memory Signal.

Evidence, Commit, Path Prediction and explicit Reasoning modules remain under development unless a separate approved beta or research protocol exists.

## Directory map

```text
workflow-ontology/
├── docs/        method, evidence, validation, commercial translation, release and website-import rules
├── schemas/     JSON Schema contracts
├── ontology/    canonical concepts and dimensions
├── mappings/    many-to-many workflow, function and governance mappings
├── evidence/    source, claim, measurement and training-fit registries
├── examples/    worked workflow-stage records
├── tests/       expected routes and boundary cases
├── scripts/     validation and release tooling
├── studies/     staged content, behavioural and intervention validation
└── releases/    immutable release manifests
```

## Evidence registry

The canonical current-product evidence layer is indexed at:

- [`evidence/README.md`](evidence/README.md)

Its machine-readable files are:

```text
evidence/evidence-sources.json
    source metadata, populations, constructs, outcomes and limitations

evidence/evidence-claims.json
    atomic claims, approved public wording and required caveats

evidence/measurement-registry.json
    G Track measurement-source and exact-implementation status

evidence/training-fit-mappings.json
    user-goal to current-product route mappings
```

The governing build plan is:

- [`docs/EVIDENCE_REGISTRY_BUILD_PLAN.md`](docs/EVIDENCE_REGISTRY_BUILD_PLAN.md)

The registry separates:

```text
workflow-demand support
function mapping
measurement/source validity
exact implementation validity
training-benefit evidence
workflow-transfer evidence
```

These must not be collapsed into one generic evidence score.

The human-readable Training-Fit Registry is the reviewed seed for current-product claims. The broader IQM Stack Evidence document is a discovery backlog and must be regraded claim by claim before import. Source-document provenance is recorded at:

- [`evidence/reviews/SOURCE_DOCUMENTS.md`](evidence/reviews/SOURCE_DOCUMENTS.md)

Only approved records may enter a tagged production release.

## Research validation programme

The canonical staged research plan is:

- [`docs/RESEARCH_VALIDATION_PLAN.md`](docs/RESEARCH_VALIDATION_PLAN.md)

It separates six evidence dimensions:

```text
W — workflow representation
D — cognitive-demand mapping
F — cognitive-function mapping
P — protocol fit
O — workflow outcome evidence
I — implementation readiness
```

These dimensions must not be collapsed into one generic evidence score.

The study sequence is indexed at:

- [`studies/README.md`](studies/README.md)

Current study scaffolds:

1. [`studies/001-content-validation/`](studies/001-content-validation/) — workflow, demand, function and intervention-locus validation;
2. [`studies/002-behavioural-validation/`](studies/002-behavioural-validation/) — prospective prediction of workflow performance;
3. [`studies/003-intervention-pilot/`](studies/003-intervention-pilot/) — cognitive training, workflow redesign and combined-route evaluation.

The first research objective is to validate the ontology’s workflow and mapping assumptions. It is not yet to claim that an IQ Mindware route causes improved organisational or educational outcomes.

## Commercial website pathway

The canonical translation policy for IQMindware.com is:

- [`docs/WEBSITE_COMMERCIAL_PATHWAY.md`](docs/WEBSITE_COMMERCIAL_PATHWAY.md)

Its governing rule is:

> **Return a route, not an evidence verdict.**

The scientific ontology remains strict and preserves separate evidence dimensions. The website should use those dimensions to assemble the strongest claims-safe route:

```text
workflow demand
→ available cognitive route
→ workflow-support route
→ outcome plan
→ evidence boundary
→ appropriate next action
```

A lack of direct workflow-effect evidence does not automatically produce a `no evidence` result. Where the workflow, demand, function and protocol mapping meet the minimum commercial evidence floor, the website may return an **evidence-informed** and **pilot-ready** route while clearly stating that the applied outcome remains to be tested.

The commercial layer must remain separate from the canonical ontology and apply:

```text
product availability
governance eligibility
approved copy
commercial route status
CTA policy
```

It must not alter the scientific mappings to favour whichever product is currently available.

## First target niches

1. Professional and AI-assisted work
2. Higher education and independent study
3. Research and evidence work
4. Health and service pathways — partner-led or research-governed only

## Release principle

Production websites and apps must import a tagged, validated release. They must not read the latest `main` branch dynamically.

Every derived website route should retain:

```text
ontology_version
evidence_registry_version
route_engine_version
product_availability_version
copy_version
```

A route should also retain or be traceable to its six-part research evidence profile once that schema is implemented.

## Public-methods boundary

This directory may publish definitions, schemas, evidence grading, illustrative mappings and aggregate validation. It must not contain user-level data, customer information, secrets, private infrastructure, clinical eligibility logic or proprietary anti-gaming controls.
