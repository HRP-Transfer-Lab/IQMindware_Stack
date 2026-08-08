# IQ Mindware Website Release Candidate — Review Checklist

**Release:** `iqm-website-slice-v0.1.0-rc1`  
**Status:** human review and production approval outstanding  
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

## 2. Scientific claim review

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

## 3. Curated route review

For every route, verify:

```text
workflow relevance
cognitive-function mapping
person-versus-system balance
live product coverage
coming-soon target functions
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

## 4. Claims and commercial copy review

- [ ] No route implies that a coming-soon module is currently available.
- [ ] No route claims established workflow improvement without direct evidence.
- [ ] No route promises sustained everyday focus improvement.
- [ ] No route promises broad working-memory or reasoning transfer.
- [ ] No route describes Matrix Reasoning as an official IQ score or promised training gain.
- [ ] Zone Check is consistently described as provisional and non-diagnostic.
- [ ] Pilot-ready wording is used only where a separate outcome plan and governance route exist.
- [ ] Health-related goals route to research or partner discussion rather than self-service treatment.

## 5. Governance review

- [ ] Workplace routes are voluntary and aggregate-first.
- [ ] No recruitment, promotion, disciplinary or covert productivity use is permitted.
- [ ] Education routes are support-focused rather than selection or grading tools.
- [ ] Health and care uses require partner/research governance.
- [ ] User data, questionnaire answers and contact details are not stored in the static ontology bundle.
- [ ] Consent and lead-capture flows are separate from showing a useful route result.

## 6. Technical release checks

Run:

```bash
python workflow-ontology/scripts/validate_registry.py
python workflow-ontology/website-release/scripts/validate_website_release.py
python workflow-ontology/website-release/scripts/run_website_route_cases.py
```

Then build the import bundle:

```bash
python workflow-ontology/website-release/scripts/build_website_release.py \
  --version 0.1.0-rc1
```

- [ ] Canonical registry validation passes.
- [ ] Website release validation passes.
- [ ] Website route and boundary cases pass.
- [ ] Release bundle is generated.
- [ ] SHA-256 checksums are generated.
- [ ] Release manifest records the source commits.
- [ ] Approved reviewers are recorded.

## 7. Website-repository import

- [ ] Import into a non-production IQ Mindware website branch.
- [ ] Store the canonical and commercial bundles locally.
- [ ] Create `ontology-lock.json` with source versions, commits and hashes.
- [ ] Make deployment fail closed on lock or checksum mismatch.
- [ ] Build the route-builder preview from the imported files.
- [ ] Test all six curated routes manually.
- [ ] Test mobile and accessible interaction.
- [ ] Confirm that no answers are sent to analytics or advertising platforms.
- [ ] Approve production deployment.

## Sign-off

| Review role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Product owner |  |  |  |  |
| Scientific reviewer |  |  |  |  |
| Claims / governance reviewer |  |  |  |  |
| Website implementation reviewer |  |  |  |  |

A production release must not be issued until the required review roles have recorded a decision and the technical checks pass against the exact release commit.
