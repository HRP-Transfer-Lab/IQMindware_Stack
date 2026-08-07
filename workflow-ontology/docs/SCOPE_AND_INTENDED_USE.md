# Scope and Intended Use

## Purpose

The Cognitive Workflow Ontology describes how cognitive demands arise within real workflows and how those demands may relate to measurement, training, workflow redesign and outcome evaluation.

It is intended to support transparent, low-risk route configuration rather than automated diagnosis or treatment selection.

## Unit of analysis

The preferred unit is a **workflow stage**, not an occupation and not a symptom label.

Example:

```text
niche: higher education
workflow: source-based assignment
stage: integrate sources into an argument
```

A workflow stage should describe:

- the meaningful output being pursued;
- the information and relationships that must be maintained;
- the constraints, time horizon and consequence of error;
- the observed friction when the stage breaks down;
- person-, task-, process- and system-level intervention options;
- candidate cognitive functions and outcome measures.

## What the ontology may support

- deterministic website route generation;
- non-clinical individual training recommendations;
- bounded organisational and education pilots;
- research study design;
- health/service pathway co-design under separate governance;
- transparent evidence and limitation displays;
- pilot measurement plans.

## What the ontology must not do

It must not:

- infer a diagnosis from workflow descriptions or app performance;
- recommend clinical treatment;
- determine employment, educational admission, insurance or disciplinary outcomes;
- assume that low performance represents an individual deficit;
- replace workflow, ergonomic, staffing or governance analysis;
- imply that an in-development module is commercially available;
- convert theoretical relevance into an efficacy claim.

## Intervention-locus rule

Every route must consider:

```text
PERSON
capacity or control training

TASK / INTERFACE
reduce avoidable cognitive load

TEAM / PROCESS
improve communication, hand-offs or coordination

ORGANISATION / SYSTEM
change incentives, authority, staffing, policy or workflow architecture
```

The route must state when training is only an adjunct to workflow redesign.

## Health and care boundary

Health-related workflow records may be included for evidence mapping and partner-led research. They should normally route to:

```text
partner-led protocol development
research pathway
approved service pilot
```

They must not generate direct consumer treatment claims.

## Evidence and availability boundary

The canonical ontology identifies the closest cognitive function even when no current app implements it. The production layer then applies availability policy.

Example:

```text
scientific mapping: Evidence Control
production result: module in development;
nearest available foundation = Signal Control
```

## Review status

Allowed review statuses are:

```text
draft
expert_reviewed
approved
retired
```

Only `approved` records may enter a production release bundle.
