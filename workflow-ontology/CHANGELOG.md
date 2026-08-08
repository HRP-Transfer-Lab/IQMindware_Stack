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

### Status

The initial ontology and route records are `draft` unless specifically marked `approved` at the evidence-source or evidence-claim level. No production release has yet been issued.

The next evidence priorities are:

1. human review of the live-Signal and Reasoning candidate overrides;
2. CBT-qualified review of the cognitive-restructuring evidence and governance boundaries;
3. structured review of the ten G Track measurement records;
4. review of the fifteen initial training-fit mappings;
5. promotion-oriented review of the remaining full-stack capacity-by-mode cells;
6. conversion of accepted candidate sources and judgements into canonical atomic records;
7. exact WM Coach metadata and relative-frame/optic-flow Attention Coach records;
8. protocol records for Evidence, Commit, Path Prediction and explicit Reasoning;
9. prototype validation of the low-risk Evidence-Sensitive Reframing scaffold before any clinical-route development.

The next workflow-research priority is Phase 0 technical and conceptual validation followed by Study 001 content validation. The research plan does not treat current workflow-to-app mappings as established intervention effects.

The commercial website pathway may nevertheless classify an adequately specified route as **evidence-informed** and **pilot-ready** where the workflow, demand, function, available protocol, outcome and governance requirements meet the documented minimum commercial evidence floor.
