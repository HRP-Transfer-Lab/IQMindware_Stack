# IQ Mindware Website Release Candidate — Review Checklist

**Release:** `iqm-website-slice-v0.1.0-rc2`  
**Status:** implementation-ready preview contract; human review and production approval outstanding  
**Date:** 8 August 2026

## 1. Product availability

Owner-confirmed live catalogue:

- [x] G Track is available for sale now.
- [x] G Track includes the Zone Check.
- [x] Attention Coach Signal Control is available for sale now.
- [x] WM Coach Relational Memory Signal is available for sale now.
- [x] WM Coach Binding Memory Signal is available for sale now.
- [x] Evidence modes are labelled coming soon.
- [x] Predictive Calibration is labelled coming soon and as a derived profile.
- [x] Commit / Decision Timing modes are labelled coming soon.
- [x] Path Prediction is labelled coming soon.
- [x] Explicit Reasoning and applied reasoning routes are labelled coming soon.

## 2. Implementation-contract completeness

- [x] Product availability is machine-readable.
- [x] The six curated routes are machine-readable.
- [x] Every route points to compact website evidence cards.
- [x] Every evidence card separates scientific basis, exact implementation, training benefit and workflow transfer.
- [x] The deterministic three-question route-builder configuration is present.
- [x] Free-text and LLM interpretation are excluded from the first release.
- [x] Route-builder, evidence-card and rendered-result schemas are present.
- [x] A fail-closed ontology lock template is present.
- [x] A TypeScript implementation reference is present.
- [x] A normalised route-result renderer is present.
- [x] A Codex implementation handoff is present.
- [x] A compact report-review route example is present.

## 3. Scientific claim review

### G Track

- [ ] Approve or revise SART engagement wording and caveat.
- [ ] Approve or revise SART response-control wording and caveat.
- [ ] Approve or revise Stroop wording and reliability caveat.
- [ ] Approve or revise Flanker wording and reliability caveat.
- [ ] Approve or revise the combined Attention profile wording.
- [ ] Approve or revise the provisional Zone Check wording and boundary.
- [ ] Approve or revise the complex-span-style measure wording.
- [ ] Approve or revise the visual-binding measure wording.
- [ ] Approve or revise the OMIB Matrix Reasoning wording.
- [ ] Approve or revise baseline/follow-up interpretation.

### Attention Coach Signal

- [ ] Confirm equivalence boundaries for the classic masked MFT-M implementation.
- [ ] Confirm that relative-frame and optic-flow variants are labelled as principled extensions where used.
- [ ] Approve the direct mechanism claim.
- [ ] Approve the selected transfer-evidence statement.
- [ ] Approve the everyday-focus and workflow-transfer caveat.

### WM Coach Signal

- [ ] Approve the Relational Memory operation description.
- [ ] Confirm that clean relation and majority-relation variants are not collapsed into one pure-WM score.
- [ ] Approve the exact-task psychometric caveat.
- [ ] Approve the Binding Memory operation description.
- [ ] Approve the partial-match, swap and source-memory caveat.
- [ ] Confirm that broad WM, reasoning and workflow transfer remain unestablished for the exact app.

### Compact evidence slice

For each of the eight website evidence cards:

- [ ] Confirm that its linked canonical claims are accurate.
- [ ] Confirm that its supported public claim does not exceed the evidence.
- [ ] Confirm that the exact-implementation status is sufficiently cautious.
- [ ] Confirm that training-benefit evidence is not confused with construct fit.
- [ ] Confirm that workflow transfer remains a separate outcome.
- [ ] Confirm that the required boundary is suitable for the homepage and expanded result page.

## 4. Curated route review

For every route, verify:

```text
workflow relevance
cognitive-function mapping
person-versus-system balance
live product coverage
coming-soon target functions
evidence cards
outcome plan
evidence boundary
governance profile
CTA
```

- [ ] Individual focus under competing information.
- [ ] Professional multi-source synthesis.
- [ ] Report review and verification.
- [ ] Complex-task re-entry after interruption.
- [ ] Higher-education source synthesis.
- [ ] Objective cognitive progress tracking.

## 5. Route-builder and UX copy review

- [ ] The three questions are understandable without cognitive-science terminology.
- [ ] The primary-need choices cover the six curated routes without misleading overlap.
- [ ] Friction choices describe observable breakdowns rather than diagnoses.
- [ ] A result is shown before any contact details are requested.
- [ ] The compact homepage result remains useful without opening the full evidence panel.
- [ ] The expanded result uses the mandatory route-result order.
- [ ] Coming-soon targets are visually distinct from available route steps.
- [ ] Evidence labels do not rely on colour alone.
- [ ] Version metadata is available in an expandable methods panel.
- [ ] Contract-error and no-route states are plain-language and fail closed.

## 6. Claims and commercial copy review

- [ ] No route implies that a coming-soon module is currently available.
- [ ] No route claims established workflow improvement without direct evidence.
- [ ] No route promises sustained everyday focus improvement.
- [ ] No route promises broad working-memory or reasoning transfer.
- [ ] No route describes Matrix Reasoning as an official IQ score or promised training gain.
- [ ] Zone Check is consistently described as provisional and non-diagnostic.
- [ ] Pilot-ready wording is used only where a separate outcome plan and governance route exist.
- [ ] Health-related goals route to research or partner discussion rather than self-service treatment.
- [ ] “Precision” is explained through defined protocols, adaptive rules, separate measures and evidence status.
- [ ] No overall evidence percentage, star score or “science-backed” badge collapses the evidence dimensions.

## 7. Governance and data review

- [ ] Workplace routes are voluntary and aggregate-first.
- [ ] No recruitment, promotion, disciplinary or covert productivity use is permitted.
- [ ] Education routes are support-focused rather than selection or grading tools.
- [ ] Health and care uses require partner/research governance.
- [ ] Questionnaire processing runs client-side by default.
- [ ] User answers and contact details are not stored in the static ontology bundle.
- [ ] Consent and lead-capture flows are separate from showing a useful route result.
- [ ] No health context, cognitive score or personal route history is sent to advertising platforms.
- [ ] Saved/downloaded routes use explicit consent and purpose-limited server processing.

## 8. Technical release checks

Run:

```bash
python workflow-ontology/scripts/validate_registry.py

python workflow-ontology/website-release/scripts/validate_website_release.py

python workflow-ontology/website-release/scripts/run_website_route_cases.py

python workflow-ontology/website-release/scripts/render_route_result.py \
  --route-id report_review_and_verification_v1 \
  --output /tmp/report-review-route.json
```

Then build the import bundle:

```bash
python workflow-ontology/website-release/scripts/build_website_release.py \
  --version 0.1.0-rc2 \
  --source-commit "$GITHUB_SHA"
```

- [ ] Canonical registry validation passes against the exact release commit.
- [ ] Website release validation passes.
- [ ] All route and boundary cases pass.
- [ ] All six primary needs resolve to the expected route.
- [ ] The reference route payload is valid JSON and conforms to the rendered-route schema.
- [ ] The release bundle is generated.
- [ ] SHA-256 checksums are generated.
- [ ] The release manifest records the source commit and file hashes.
- [ ] The generated lock defaults to `approved_for_production: false` and `fail_closed: true`.
- [ ] GitHub Actions passes on the exact release commit.
- [ ] Approved reviewers are recorded.

## 9. Website-repository import

- [ ] Import into a non-production IQ Mindware website branch.
- [ ] Store the canonical and commercial bundles locally.
- [ ] Create the completed `ontology-lock.json` with source versions, commits and hashes.
- [ ] Make deployment fail closed on lock or checksum mismatch.
- [ ] Build the compact homepage Route Builder from the imported files.
- [ ] Build the expanded `/build-your-route/` result page.
- [ ] Test all six curated routes manually.
- [ ] Test the coming-soon partial-fit presentation.
- [ ] Test the health/research and not-eligible states.
- [ ] Test mobile, keyboard and screen-reader interaction.
- [ ] Confirm that no answers are sent to analytics or advertising platforms.
- [ ] Approve production deployment.

## Sign-off

| Review role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Product owner |  |  |  |  |
| Scientific reviewer |  |  |  |  |
| Claims / governance reviewer |  |  |  |  |
| Website implementation reviewer |  |  |  |  |

A production release must not be issued until the required review roles have recorded a decision and the technical checks pass against the exact immutable release commit.
