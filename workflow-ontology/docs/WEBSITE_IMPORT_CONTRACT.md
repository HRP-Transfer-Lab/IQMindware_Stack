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

Current release candidate:

```text
iqm-website-slice-v0.1.0-rc2
```

It is an implementation-ready preview contract rather than a production release. It locks the owner-confirmed current commercial state:

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

## Two-bundle architecture

The website imports two independently versioned bundles.

### Canonical scientific release

```text
workflow-ontology.json
workflow-evidence.json
outcome-registry.json
governance-profiles.json
release-manifest.json
SHA256SUMS
```

This bundle provides the scientific and workflow ground truth.

### Commercial website overlay

```text
product-availability.json
evidence-slice.json
route-builder-config.json
route-templates.json
route-copy.json
schemas/website-evidence-slice.schema.json
schemas/route-builder-config.schema.json
schemas/rendered-route.schema.json
tests/website-route-cases.json
commercial-release-manifest.json
commercial-SHA256SUMS
```

This bundle provides the current public offer, deterministic selection policy, compact evidence display, approved copy and route-result contract.

The website should import both bundles, validate the cross-references and record both source versions in one local lock file.

## Recommended website-repository location

```text
products/trident-g-iq/websites/iqmindware/
└── contracts/workflow-routing/
    ├── canonical/
    │   ├── workflow-ontology.json
    │   ├── workflow-evidence.json
    │   ├── outcome-registry.json
    │   ├── governance-profiles.json
    │   ├── release-manifest.json
    │   └── SHA256SUMS
    ├── commercial/
    │   ├── product-availability.json
    │   ├── evidence-slice.json
    │   ├── route-builder-config.json
    │   ├── route-templates.json
    │   ├── route-copy.json
    │   ├── schemas/
    │   ├── release-manifest.json
    │   └── SHA256SUMS
    └── ontology-lock.json
```

## Availability overlay

The website applies the separate `product-availability.json` file.

Example:

```json
{
  "component_id": "attention_evidence",
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

A coming-soon function may appear only in:

```text
target_functions_in_development
coming_soon_targets
roadmap displays
```

It must never appear in:

```text
available_protocol_route
available product CTA
sales copy implying present access
```

## Website evidence slice

The commercial bundle contains a compact evidence layer for homepage and route-result rendering.

Every evidence card must preserve four dimensions:

```text
scientific basis
exact implementation
training benefit
workflow transfer
```

The website must not average these dimensions into one percentage, star rating or generic `science-backed` badge.

The compact evidence slice may simplify the canonical wording, but it must retain:

```text
source claim IDs
measurement IDs where applicable
supported public claim
required boundary
review status
```

## Deterministic route-builder contract

The first release uses a controlled questionnaire rather than free-text or LLM interpretation.

```text
Who is this for?
→
What are they trying to accomplish?
→
What tends to happen when the workflow becomes difficult?
```

The primary need determines route eligibility. Audience and friction choices refine the score.

Selection must be reproducible from:

```text
route-builder-config.json
+
route-templates.json
```

Free-text interpretation is excluded until a separately tested and governed intent classifier exists.

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

The imported ontology contains no user answers.

The first questionnaire should run in the browser.

A server call is needed only when a user explicitly:

```text
saves a route
downloads a personalised summary
submits a pilot enquiry
enters an authenticated organisation workspace
```

The user should see a useful result before contact details are requested.

Health context, cognitive scores and personal route histories must not be sent to advertising platforms.

## Required normalised route payload

Each rendered route should contain:

```text
route_id
heading
status_labels
workflow_explanation
available_protocol_route
coming_soon_targets
evidence_cards
workflow_supports
outcomes
evidence_boundary
primary_cta
versions
```

The route must retain version metadata for:

```text
ontology
evidence
product availability
route-builder configuration
copy
```

The full stored or downloadable record may additionally retain:

```text
created_at
workflow_stage_ids
demand_profile
friction_ids
intervention_loci
function_mappings
governance_profile
```

## Lock-file requirement

The website repository must retain a lock record based on:

```text
website-release/ontology-lock.template.json
```

Minimum structure:

```json
{
  "ontology_release": "v0.1.0",
  "evidence_release": "v0.1.0",
  "commercial_release": "iqm-website-slice-v0.1.0",
  "route_builder_config": "0.1.0",
  "copy_version": "0.1.0",
  "source_commits": {},
  "manifest_hashes": {},
  "file_hashes": {},
  "imported_at": "ISO-8601 timestamp",
  "approved_for_production": true,
  "approval_roles": {},
  "fail_closed": true
}
```

A website deployment must fail closed when:

- the imported files do not match their manifests;
- checksums differ;
- a referenced ID is missing;
- the lock file does not match the imported releases;
- `approved_for_production` is not true;
- a required review role is absent.

## Reference implementation

The release candidate provides:

```text
reference/route-builder.reference.ts
scripts/render_route_result.py
examples/report-review-route.example.json
IMPLEMENTATION_HANDOFF.md
```

These define the intended deterministic selection and normalised result payload without imposing a specific front-end framework.

## Failure behaviour

The website must abstain rather than guess when:

- no approved curated route matches the required primary need;
- governance eligibility is unclear;
- the requested outcome is clinical or high stakes;
- product availability cannot be resolved;
- a coming-soon module would be required as though it were live;
- the evidence registry is inconsistent;
- a route references an unknown evidence card, support or outcome;
- the ontology or commercial release fails validation;
- the lock file or checksum verification fails.

Recommended explicit failure states:

```text
research_collaboration
not_eligible
no_approved_route
contract_error
```

None of these states should silently fall back to whichever current product is commercially convenient.
