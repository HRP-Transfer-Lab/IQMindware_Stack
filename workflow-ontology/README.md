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
├── docs/        method, evidence, release and website-import rules
├── schemas/     JSON Schema contracts
├── ontology/    canonical concepts and dimensions
├── mappings/    many-to-many evidence and governance mappings
├── evidence/    source and claim records
├── examples/    worked workflow-stage records
├── tests/       expected routes and boundary cases
├── scripts/     validation and release tooling
└── releases/    immutable release manifests
```

## First target niches

1. AI-heavy knowledge work
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

## Public-methods boundary

This directory may publish definitions, schemas, evidence grading, illustrative mappings and aggregate validation. It must not contain user-level data, customer information, secrets, private infrastructure, clinical eligibility logic or proprietary anti-gaming controls.
