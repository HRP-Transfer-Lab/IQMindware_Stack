# Website Import Contract

## Responsibility split

The HRP ontology owns scientific and workflow ground truth:

```text
workflow definition
demand dimensions
friction signatures
intervention loci
function mappings
evidence status
outcome taxonomy
governance classification
```

The IQ Mindware website owns commercial execution:

```text
question wording
public labels
current app availability
route ranking policy
approved result copy
CTA and pricing
lead capture
production analytics
```

## Import rule

Production must import a tagged release, validate it locally and store a lock file. Runtime requests must not depend on live GitHub access.

## Current release-candidate package

The narrow first website slice is maintained at:

- [`../website-release/`](../website-release/)

It is a release candidate rather than a production release. It locks the owner-confirmed current commercial state:

```text
AVAILABLE FOR SALE NOW

G Track
including the Zone Check, attention, working-memory,
matrix-reasoning and longitudinal-comparison measures

Attention Coach
Signal Control only

WM Coach
Relational Memory Signal
Binding Memory Signal
```

```text
COMING SOON

Evidence modes
Predictive Calibration profiles
Commit / Decision Timing modes
Path Prediction
Explicit Reasoning
Applied reasoning and restructuring routes
```

Coming-soon modules may appear in the public roadmap and as named target functions, but they must never be emitted as live route steps.

## Minimum imported artefacts

Canonical scientific release:

```text
workflow-ontology.json
workflow-evidence.json
outcome-registry.json
governance-profiles.json
release-manifest.json
SHA256SUMS
```

Commercial website overlay:

```text
product-availability.json
route-templates.json
route-copy.json
website-route-cases.json
commercial-release-manifest.json
commercial-SHA256SUMS
```

The website should import both bundles, validate the cross-references and record both source versions in one local lock file.

## Availability overlay

The website applies a separate `product-availability.json` file.

Example:

```json
{
  "function_id": "attention_evidence",
  "status": "coming_soon",
  "nearest_available_foundation": "attention_signal"
}
```

The ontology must not be rewritten merely to match current commercial availability.

The route result must distinguish:

```text
closest target function
from
currently available foundational route
```

## Claims overlay

The production layer selects only approved claims and caveats. It may simplify wording but must not strengthen the evidence level.

A route may describe a current app as:

```text
available now
construct-aligned
evidence-informed
pilot-ready
```

only when the corresponding scientific and commercial records support those labels.

The public copy must not convert:

```text
coming soon
into
available

construct basis
into
validated product benefit

pilot-ready
into
proven workflow improvement
```

## Data boundary

The imported ontology contains no user answers. Questionnaire processing may run in the browser. A server call is needed only when a user explicitly saves, downloads or submits a route.

## Required route metadata

Each generated route should contain:

```text
route_id
created_at
ontology_version
evidence_registry_version
product_availability_version
copy_version
workflow_stage_ids
demand_profile
friction_ids
intervention_loci
function_mappings
available_protocol_route
target_functions_in_development
workflow_support_route
outcome_plan
governance_profile
claims_and_caveats
```

## Lock-file requirement

The website repository should retain a lock record similar to:

```json
{
  "ontology_release": "v0.1.0",
  "evidence_release": "v0.1.0",
  "commercial_release": "v0.1.0",
  "source_commits": {},
  "manifest_hashes": {},
  "imported_at": "ISO-8601 timestamp",
  "approved_for_production": true
}
```

A website deployment must fail closed when the imported release does not match the lock file.

## Failure behaviour

The website must abstain rather than guess when:

- no approved workflow-stage mapping exists;
- governance eligibility is unclear;
- the requested outcome is clinical or high stakes;
- product availability cannot be resolved;
- a coming-soon module would be required as though it were live;
- the evidence registry is inconsistent;
- the ontology or commercial release fails validation;
- the lock file or checksum verification fails.
