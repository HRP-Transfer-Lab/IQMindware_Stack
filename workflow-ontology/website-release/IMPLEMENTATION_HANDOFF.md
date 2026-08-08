# IQ Mindware Homepage Route Builder — Implementation Handoff

**Release candidate:** `iqm-website-slice-v0.1.0-rc2`  
**Status:** implementation-ready preview contract; scientific and claims sign-off pending  
**Target:** `Mindware-Lab/trident-g-platform/products/trident-g-iq/websites/iqmindware`  
**Source of truth:** HRP Transfer Lab Cognitive Workflow Ontology

---

# 1. Purpose

This package makes the first homepage Cognitive Route Builder deterministic, auditable and straightforward to implement.

The first release is deliberately bounded to products confirmed as complete and available for sale now:

```text
G Track
├─ Attention battery
├─ Zone Check
├─ Working-memory measures
├─ OMIB Matrix Reasoning Benchmark
└─ Baseline / follow-up comparison

Attention Coach
└─ Signal Control

WM Coach
├─ Relational Memory — Signal
└─ Binding Memory — Signal
```

Everything else is represented separately as **coming soon**.

The webapp must never turn:

```text
coming soon
into
available now
```

or:

```text
construct relevance
into
established workflow benefit
```

---

# 2. Runtime files

The homepage preview should import these files locally:

```text
product-availability.json
evidence-slice.json
route-builder-config.json
route-templates.json
route-copy.json
```

The following files support testing, validation and provenance:

```text
tests/website-route-cases.json
schemas/website-evidence-slice.schema.json
schemas/route-builder-config.schema.json
schemas/rendered-route.schema.json
ontology-lock.template.json
```

Do not fetch these files live from GitHub at runtime.

---

# 3. Recommended website repository location

After review and release, import the bundle to:

```text
products/trident-g-iq/websites/iqmindware/
└── contracts/workflow-routing/
    ├── product-availability.json
    ├── evidence-slice.json
    ├── route-builder-config.json
    ├── route-templates.json
    ├── route-copy.json
    ├── schemas/
    ├── ontology-lock.json
    └── SHA256SUMS
```

Recommended implementation files:

```text
assets/js/workflow-route-builder.js
assets/js/workflow-route-renderer.js
assets/js/workflow-route-analytics.js
build-your-route/index.html
```

The same engine can be embedded as a compact homepage card and opened as a fuller route-builder page.

---

# 4. User flow

The first release uses three questions.

```text
1. Who are you configuring this for?
2. What are you trying to accomplish?
3. What tends to happen when this becomes difficult?
```

Question 2 is the required route selector.

Question 1 and Question 3 refine the score and the explanation. They do not permit an unsupported route to replace the primary workflow match.

The result is shown before any email or contact request.

---

# 5. Deterministic selection

Use the reference implementation in:

```text
reference/route-builder.reference.ts
```

Selection rules:

```text
required primary-need match
→ base score
→ audience and friction weights
→ highest score
→ route priority
→ stable route-ID tie break
```

The first release excludes free-text or LLM interpretation.

Do not add free text until there is a separately tested intent classifier, a controlled vocabulary fallback and explicit health/high-stakes governance.

---

# 6. Route-result payload

Normalise the selected route into this order:

```text
1. Heading
2. Status labels
3. Workflow explanation
4. Available route
5. Coming-soon target functions
6. Evidence cards
7. Workflow supports
8. Outcome plan
9. Evidence boundary
10. CTA
11. Version metadata
```

Use:

```bash
python workflow-ontology/website-release/scripts/render_route_result.py \
  --route-id report_review_and_verification_v1
```

as the reference payload generator.

The output must conform to:

```text
schemas/rendered-route.schema.json
```

---

# 7. Evidence-card display

Every card must show four independent dimensions:

```text
Scientific basis
Exact implementation
Training benefit
Workflow transfer
```

Recommended compact UI:

```text
PUBLISHED FOUNDATION
Masked Majority Function task family

UNDER STAGED VALIDATION
Exact browser and wrapper implementation

INITIAL CONTROLLED EVIDENCE
Selected cognitive-task transfer

TO BE TESTED
Everyday and workflow outcomes
```

Do not calculate an overall percentage or star rating.

The evidence boundary should follow the constructive content, not replace it.

---

# 8. Coming-soon handling

A route may identify a coming-soon function when it is the closest target.

Example:

```text
Closest target:
Reasoning Evidence — coming soon

Available foundation:
Attention Signal + WM Binding Signal
```

The unavailable target belongs in `coming_soon_targets`.

It must never appear in `available_protocol_route`.

---

# 9. Homepage component contract

Recommended component tree:

```text
RouteBuilder
├── RouteQuestion
├── RouteProgress
├── RouteOption
├── RouteResult
│   ├── RouteHeader
│   ├── AvailableRouteSteps
│   ├── ComingSoonTargets
│   ├── EvidencePanel
│   ├── WorkflowSupportPanel
│   ├── OutcomePlan
│   ├── EvidenceBoundary
│   └── RouteCTA
└── RoutePrivacyNote
```

The compact homepage version may show:

```text
question flow
→ route heading
→ live route
→ one evidence summary
→ CTA
```

The expanded page should expose all evidence dimensions, supports, outcomes and version details.

---

# 10. State handling

Use explicit states:

```text
idle
answering
route_found
research_collaboration
not_eligible
no_approved_route
contract_error
```

Do not silently choose a nearest route when no required primary-need rule matches.

A contract or checksum failure should disable recommendations and show a neutral service message.

---

# 11. Privacy and analytics

The first questionnaire should run client-side.

Allowed analytics:

```text
route_builder_started
question_answered using non-sensitive option ID
route_builder_completed
route_result_viewed
evidence_panel_opened
pilot_cta_clicked
individual_cta_clicked
```

Do not send:

```text
free text
health context
clinical goals
raw cognitive scores
personal route history
```

to advertising platforms.

Saving, downloading or submitting a route requires a separate explicit action and a Cloudflare Function or authenticated service.

---

# 12. Accessibility

Required:

```text
keyboard-operable choices
visible focus state
semantic fieldset and legend
screen-reader status announcements
no colour-only evidence labels
reduced-motion support
44px minimum touch targets
plain-language error state
```

The route should remain usable with JavaScript enhancement failure by showing links to the three current product pages.

---

# 13. Validation commands

Run from the repository root:

```bash
python workflow-ontology/scripts/validate_registry.py

python workflow-ontology/website-release/scripts/validate_website_release.py

python workflow-ontology/website-release/scripts/run_website_route_cases.py

python workflow-ontology/website-release/scripts/render_route_result.py \
  --route-id report_review_and_verification_v1
```

Build the import bundle:

```bash
python workflow-ontology/website-release/scripts/build_website_release.py \
  --version 0.1.0-rc2 \
  --source-commit "$GITHUB_SHA"
```

The builder generates:

```text
release-manifest.json
SHA256SUMS
ontology-lock.generated.json
```

The generated lock remains unapproved until the named review roles sign off.

---

# 14. Preview acceptance criteria

The preview is ready for human review when:

1. all six primary needs resolve deterministically;
2. only the three current products appear as available;
3. all future modules appear only as coming soon;
4. every route displays at least one evidence card;
5. the evidence card preserves all four dimensions;
6. every organisational or education route includes workflow supports and separate outcomes;
7. health/treatment intent routes to research collaboration;
8. selection or punitive intent is rejected;
9. route results render before contact capture;
10. version metadata is visible in an expandable methods panel;
11. mobile and keyboard flows pass;
12. checksum or lock mismatch fails closed.

---

# 15. Production gate

This package is suitable for a non-production homepage preview.

Production import still requires:

```text
scientific review
claims and governance review
curated-route approval
immutable source tag or commit
canonical evidence release
checksums
completed lock file
manual preview review
```

The implementation should therefore preserve the release status and make promotion a data release rather than a code rewrite.
