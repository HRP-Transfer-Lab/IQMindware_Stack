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

## Minimum imported artefacts

```text
workflow-ontology.json
workflow-evidence.json
outcome-registry.json
governance-profiles.json
release-manifest.json
SHA256SUMS
```

## Availability overlay

The website applies a separate `product-availability.json` file.

Example:

```json
{
  "function_id": "attention_evidence",
  "status": "in_development",
  "nearest_available_foundation": "attention_signal"
}
```

The ontology must not be rewritten merely to match current commercial availability.

## Claims overlay

The production layer selects only approved claims and caveats. It may simplify wording but must not strengthen the evidence level.

## Data boundary

The imported ontology contains no user answers. Questionnaire processing may run in the browser. A server call is needed only when a user explicitly saves, downloads or submits a route.

## Required route metadata

Each generated route should contain:

```text
route_id
created_at
ontology_version
workflow_stage_ids
demand_profile
friction_ids
intervention_loci
function_mappings
available_protocol_route
workflow_support_route
outcome_plan
governance_profile
claims_and_caveats
```

## Failure behaviour

The website must abstain rather than guess when:

- no approved workflow-stage mapping exists;
- governance eligibility is unclear;
- the requested outcome is clinical or high stakes;
- product availability cannot be resolved;
- the evidence registry is inconsistent;
- the ontology release fails validation.
