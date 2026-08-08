# Changelog

All notable changes to the Cognitive Workflow Ontology are recorded here.

## [Unreleased]

### Added

- Initial ontology scope, intended-use and evidence-grading rules.
- Versioning and IQ Mindware website-import contract.
- Initial niche registry for AI-heavy work, higher education, research, health/service pathways and individual professional use.
- Ten reusable workflow archetypes.
- Sixteen workflow-demand dimensions.
- Fifteen friction signatures.
- Four intervention loci.
- Workflow-support and outcome-measure registries.
- Initial demand-to-function mappings based on the APC architecture.
- Governance profiles for individual, workplace, education, research and health-partner routes.
- Initial evidence-source and evidence-claim registries.
- Five canonical workflow-stage records.
- Worked examples for AI-output verification and higher-education source synthesis.
- Expected-route and boundary-case tests.
- Dependency-free validation script.
- Canonical `RESEARCH_VALIDATION_PLAN.md` covering the six-part W/D/F/P/O/I confidence model and staged ontology, behavioural, intervention and deployment validation.
- Study programme index under `studies/`.
- Study 001 content-validation scaffold.
- Study 002 behavioural-validation scaffold.
- Study 003 intervention-pilot scaffold.
- Canonical `WEBSITE_COMMERCIAL_PATHWAY.md` defining how strict research evidence is translated into constructive, claims-safe website routes rather than binary `proven` or `no evidence` outputs.
- Commercial route statuses, minimum evidence floor, abstention rules, mandatory result structure, product-availability fallback policy and worked AI-verification and higher-education examples.
- Canonical `evidence/README.md` and `EVIDENCE_REGISTRY_BUILD_PLAN.md` for the website evidence-table programme.
- Expanded evidence-source registry covering MFT-M, G Track tasks, working-memory training, attention training, transfer and clinical-adjacent category evidence.
- Expanded atomic claims registry with separate measurement, implementation, training-benefit, conflicting-evidence and claims-boundary records.
- `measurement-registry.json` with ten draft G Track measurement and longitudinal-interpretation records.
- `training-fit-mappings.json` with fifteen draft goal-to-route mappings across G Track, Attention Coach Signal and WM Coach Signal.
- Source-document provenance and SHA-256 records for the Training-Fit Registry and broader Stack Evidence discovery table.
- `GT_ATTENTION_ZONE_EVIDENCE_REVIEW_v0.1.md` with peer-reviewed evidence, an arXiv/bioRxiv watchlist, scoring recommendations and a prospective validation plan.
- `FULL_VERTICAL_STACK_MODE_EVIDENCE_REVIEW_v0.1.md` extending the evidence review from Attention Control through explicit Reasoning, including formal reasoning, belief calibration and evidence-sensitive reframing.
- `vertical-stack-mode-matrix.candidate.json` with the 20 capacity-by-mode cells across Signal, Evidence, Predictive Calibration and Commit.
- `vertical-stack-sources.candidate.json` with peer-reviewed sources and an explicitly labelled prepublication watchlist for the full-stack review.
- Candidate application records separating non-clinical evidence-sensitive reframing, professional belief calibration and health/research interpretation-bias routes.
- `LIVE_SIGNAL_AND_REASONING_MEASUREMENT_REVIEW_v0.1.md`, the first promotion-oriented audit of the three live Signal implementations and the explicit-reasoning measurement model.
- `live-signal-reasoning-overrides.candidate.json` with literature-audited candidate overrides, protocol-variant separation and promotion recommendations.
- `live-signal-reasoning-source-additions.candidate.json` with verified sources for adaptive MFT-M, n-back psychometrics, visual-working-memory reliability, swap-error modelling, metacognitive prompting, debiasing and belief updating.
- `evidence/reviews/README.md` documenting the review and promotion workflow.
- `EXPLICIT_REASONING_COGNITIVE_RESTRUCTURING_REVIEW_v0.1.md` distinguishing formal relational reasoning, professional belief calibration, non-clinical evidence-sensitive reframing, clinical cognitive restructuring and cognitive reappraisal.
- `explicit-reasoning-intervention-families.candidate.json` with separate candidate records for formal reasoning, belief calibration, reframing, behavioural experiments, condition-specific restructuring, reappraisal and LLM-assisted delivery.
- `explicit-reasoning-cbt-sources.candidate.json` with peer-reviewed component, process and meta-analytic sources plus a clearly labelled prepublication dialogue-design watchlist.
- `website-release/`, a narrow first IQMindware.com release-candidate package based only on products confirmed as commercially available now.
- `website-release/product-availability.json` locking G Track with Zone Check, Attention Coach Signal and WM Coach Relational/Binding Signal as the live commercial catalogue.
- `website-release/route-templates.json` with six curated first-release routes for focus, synthesis, verification, interruption re-entry, higher-education source work and objective progress tracking.
- `website-release/route-copy.json` with candidate public headings, workflow explanations, module labels, status labels, coming-soon explanations, evidence boundaries and CTAs.
- `website-release/evidence-slice.json` with eight compact website-safe evidence cards, each preserving scientific basis, exact implementation, training benefit and workflow transfer as separate dimensions.
- `website-release/route-builder-config.json` with the deterministic three-question homepage questionnaire, scoring rules, client-side data policy and controlled eligibility fallbacks.
- JSON Schemas for the website evidence slice, route-builder configuration and normalised rendered route result.
- `website-release/ontology-lock.template.json` with fail-closed defaults and explicit production-approval roles.
- `website-release/tests/website-route-cases.json` covering live-module enforcement, coming-soon fallbacks, deterministic resolution of all six primary needs, four-dimensional evidence, Matrix Reasoning boundaries, Zone Check boundaries, health-partner routing and exclusion of free-text interpretation.
- `website-release/scripts/validate_website_release.py`, `run_website_route_cases.py`, `render_route_result.py` and `build_website_release.py` for cross-reference validation, deterministic matching, normalised result rendering, checksums and later website import.
- `website-release/reference/route-builder.reference.ts`, a dependency-free TypeScript reference for Codex implementation.
- `website-release/IMPLEMENTATION_HANDOFF.md`, defining website file placement, component structure, privacy, accessibility, analytics and preview acceptance criteria.
- `website-release/examples/report-review-route.example.json`, a compact reference payload for the homepage and expanded result page.
- GitHub Actions validation of the canonical registries, website release, route cases, reference rendering and checksummed bundle build.

### Changed

- First commercial niche wording broadened from AI-heavy work to **professional and AI-assisted work**, with AI treated as a context modifier rather than the entire professional category.
- Working-memory evidence is decomposed into strong mechanism fit, moderate/small untrained-WM benefit, unvalidated exact WM Coach effects and no established fluid-intelligence transfer.
- Attention evidence is decomposed into strong MFT-M mechanism fit, moderate/emerging direct training evidence and unestablished sustained everyday-focus transfer.
- The Evidence Registry Build Plan now includes a separate full-stack candidate phase before workflow and governed application evidence.
- Predictive Calibration is fixed as a cross-cutting derived profile rather than a fourth gameplay component.
- Explicit Reasoning is separated into formal validity, sequential evidence evaluation, belief calibration, conclusion timing and domain-semantic application.
- Reframing is separated into a non-clinical evidence-sensitive reasoning route and a health/research-governed interpretation-bias or reappraisal route.
- Attention Signal now requires separate evidence statuses for classic absolute MFT-M, adaptive absolute MFT-M, relative/polar extensions and optic-flow extensions.
- Relational Memory Signal and Binding Memory Signal are recommended for downgrade from `exact_protocol: moderate` to `plausible_but_not_established` pending exact-task psychometrics.
- The proposed Reasoning score is replaced by a multi-parameter model separating validity sensitivity, response bias, semantic/belief effects, cannot-tell discrimination, lure acceptance and confidence calibration.
- Swap errors are no longer assumed to be pure binding failures; candidate cue, encoding, conjunction, retrieval, lag and response-strategy causes must be compared.
- SMART-style relational training is now treated as one formal-reasoning evidence family rather than the entire basis of the Reasoning layer.
- Cognitive restructuring is defined as a distinct applied explicit-reasoning intervention family involving appraisal identification, evidence examination, calibrated alternatives, behavioural testing and outcome-based model revision.
- Cognitive reappraisal is kept separate from cognitive restructuring and from generic executive-function or reasoning training.
- Clinical cognitive-restructuring evidence is retained as condition-specific category evidence and cannot be transferred directly to the generic IQ Mindware Reasoning app.
- The non-clinical public route is labelled **Evidence-Sensitive Reframing** and explicitly excludes therapy, diagnosis and treatment claims.
- The owner-confirmed public release state is explicit: **G Track with Zone Check, Attention Coach Signal and WM Coach Signal are available for sale now; all Evidence, Calibration, Commit, Path Prediction and Explicit Reasoning modules are coming soon.**
- The website import contract requires separate canonical-science and commercial-overlay bundles, version locks, checksum verification and fail-closed handling when a coming-soon module would otherwise be treated as live.
- The website release candidate is advanced from `rc1` to `rc2`, adding a self-contained evidence slice, deterministic route matcher, rendering contract, reference implementation and import lock.
- The first homepage release excludes free-text and LLM interpretation so it can run entirely client-side with reproducible recommendations and a narrow privacy surface.
- Each curated route now links directly to its workflow explanation and evidence-card IDs, avoiding runtime reconstruction of public claims from the wider research registry.

### Status

The initial ontology and scientific route records are `draft` unless specifically marked `approved` at the evidence-source or evidence-claim level. No production evidence release has yet been issued.

The website package is now `iqm-website-slice-v0.1.0-rc2`: an implementation-ready preview contract, not a production import. It permits only the current live product set in available route steps and labels the remainder of the stack as coming soon.

The next evidence and release priorities are:

1. human scientific review of the ten G Track measurement records and eight compact website evidence cards;
2. product-equivalence and claims review of Attention Coach Signal;
3. exact-task wording and claims review of WM Coach Relational and Binding Signal;
4. human review of the six curated routes and their person-versus-system balance;
5. claims and governance review of the questionnaire, public labels and CTAs;
6. immutable canonical evidence and commercial release bundles with checksums and completed reviewer records;
7. import into a non-production IQMindware.com branch using the completed ontology lock;
8. accessible preview testing of all routes, coming-soon states, health/research diversion and fail-closed behaviour;
9. production approval only after the exact release commit passes technical and human sign-off.

The next workflow-research priority remains Phase 0 technical and conceptual validation followed by Study 001 content validation. The research plan does not treat current workflow-to-app mappings as established intervention effects.

The commercial website pathway may classify an adequately specified route as **evidence-informed** and **pilot-ready** where the workflow, demand, function, available protocol, outcome and governance requirements meet the documented minimum commercial evidence floor. It must still state that direct applied benefit remains to be tested.
