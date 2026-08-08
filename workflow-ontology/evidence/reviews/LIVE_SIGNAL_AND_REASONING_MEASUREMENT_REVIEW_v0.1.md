# Live Signal Modes and Explicit Reasoning Measurement Review

**Version:** draft v0.1.0  
**Date:** 8 August 2026  
**Status:** literature-audited candidate review; human expert approval pending; not for production claims  
**Repository branch:** `feat/workflow-ontology-v0.1`  
**Scope:** the three commercially available Signal implementations, the proposed explicit-reasoning measurement model, and their place in the full 20-cell capacity-by-mode matrix  
**Parent records:** `../vertical-stack-mode-matrix.candidate.json`  
**Machine-readable decisions:** `../live-signal-reasoning-overrides.candidate.json`  
**Source additions:** `../live-signal-reasoning-source-additions.candidate.json`

---

# 1. Purpose

This review performs the first promotion-oriented audit of the full vertical-stack evidence matrix.

It concentrates on:

```text
AVAILABLE NOW
Attention Control — Signal
Relational Memory — Signal
Binding Memory — Signal

IN DEVELOPMENT
Reasoning — Signal
Reasoning — Evidence
Reasoning — Predictive Calibration
Reasoning — Commit
```

The remaining capacity-by-mode cells retain the judgements in the full-stack review pending their own source-by-source promotion audits.

The review distinguishes:

```text
construct basis
→ evidence that the cognitive function is scientifically meaningful

task-family basis
→ evidence for substantially similar experimental tasks

exact-protocol validity
→ evidence for the precise IQ Mindware implementation and score

training evidence
→ evidence that practice changes a separate cognitive measure

workflow transfer
→ evidence that change reaches a meaningful professional, educational or other applied outcome
```

No record is promoted to `expert_reviewed` or `approved` by this document. The output is a candidate decision package for human scientific review.

---

# 2. Executive decisions

| Cell | Construct basis | Task-family basis | Exact IQM protocol | Exact training benefit | Workflow transfer | Promotion recommendation |
|---|---:|---:|---:|---:|---:|---|
| **Attention Signal** | **Strong** | **Strong for classic/adaptive MFT-M** | **Moderate / provisional** | **Moderate / emerging** | **Not established** | Candidate for expert review after implementation-equivalence and timing checks |
| **Relational Memory Signal** | **Strong** | **Moderate** | **Plausible, not established** | **Not established** | **Not established** | Retain as draft; describe the trained operation, not a validated capacity benefit |
| **Binding Memory Signal** | **Strong** | **Strong for change-detection/binding paradigms** | **Plausible, not established** | **Not established; broad transfer evidence includes strong null findings** | **Not established** | Retain as draft; add error-model and psychometric validation before promotion |
| **Reasoning Signal** | **Strong** | **Strong for formal reasoning; moderate for wrapper-transfer design** | **Plausible, not established** | **Not established for the exact game; adjacent instructional evidence moderate** | **Not established** | Measurement model ready for prototype validation, not a benefit claim |
| **Reasoning Evidence** | **Strong** | **Moderate–strong adjacent instructional basis** | **Plausible, not established** | **Not established for the exact task** | **Not established** | Prototype as a sequential argument-evaluation task |
| **Reasoning Calibration** | **Strong** | **Strong measurement basis; moderate general training signal** | **Plausible, not established** | **Moderate for adaptive metacognitive training generally; not established for IQM** | **Not established** | Implement as a derived profile, not a fourth game |
| **Reasoning Commit** | **Moderate–strong** | **Moderate adjacent decision/sampling basis** | **Plausible, not established** | **Not established** | **Not established** | Prototype only after Evidence mode is stable |

The main correction to the previous candidate matrix is:

```text
Relational Memory Signal and Binding Memory Signal
should not currently have exact_protocol = moderate.

They have strong or moderate scientific task-family foundations,
but the precise IQ Mindware implementations have no direct
reliability, construct-validity or training study.
```

---

# 3. Attention Control — Signal

## 3.1 What is well supported

The backward-masked Majority Function Task provides a direct experimental method for varying information demand and exposure time while estimating cognitive-control capacity.

Wu et al. (2016) reported:

- a formal information-rate account of masked majority decisions;
- a fitted capacity estimate in bits per second;
- useful split-half and test–retest reliability in the laboratory implementation;
- a grouping-search model that outperformed simpler alternatives.

He et al. (2022) then tested a computerised-adaptive administration:

- 40 healthy young adults;
- scores highly correlated with the original administration;
- high test–retest reliability;
- fewer than 216 trials and approximately 20 minutes, compared with 864 trials and approximately 86 minutes in the original format;
- openly available source code and data.

Zhang et al. (2024) provide the only direct MFT-M training study currently in the registry:

- 84 healthy young adults randomised to MFT-M or sham training;
- seven consecutive days;
- benefits on selected revised Attention Network Test conditions;
- better performance across verbal-learning acquisition trials;
- ERP changes during working-memory and task-switching measures.

This supports:

```text
classic MFT-M construct basis:
STRONG

adaptive MFT-M task-family basis:
STRONG / DIRECT

MFT-M training evidence:
MODERATE / EMERGING
```

It does not establish broad attention, sustained everyday focus, workplace performance or fluid-intelligence improvement.

## 3.2 Required protocol split

The current Attention Signal record must separate four variants.

| Variant | Evidence status | Interpretation |
|---|---|---|
| **Classic absolute-direction MFT-M** | Published anchor | Closest match to the validated laboratory task family |
| **Adaptive absolute-direction MFT-M** | Adapted published model | Supported by the He et al. adaptive administration, subject to implementation equivalence |
| **Relative/polar MFT-M** | Principled extension | Preserves majority extraction but adds a reference-frame transformation that has not been directly validated |
| **Optic-flow MFT-M** | Principled transfer extension | Changes the carrier and introduces display/device timing demands; no direct validation of the exact task |

The classic task cannot lend its full evidence grade automatically to the relative-frame and optic-flow variants.

## 3.3 Exact IQ Mindware status

The exact app should remain **moderate/provisional**, not strong, until it demonstrates:

```text
frame-counted timing fidelity
browser and device transport
recovery of the expected entropy/exposure function
reliability of fitted capacity estimates
concordance with a reference MFT-M implementation
stable scoring under adaptive administration
separate performance by wrapper
```

The strongest claims-safe wording is:

> **Attention Coach Signal uses the masked Majority Function approach to train controlled extraction of a majority relation under visual interference and time pressure.**

Required caveat:

> **The classic task has a published measurement and emerging training basis. IQ Mindware’s relative-frame, optic-flow and browser-based implementations require their own validation, and everyday or workflow benefits are not established.**

## 3.4 Promotion decision

```text
Promotion recommendation:
EXPERT-REVIEW CANDIDATE

Condition:
implementation-equivalence evidence and protocol-variant separation
must be documented before any production approval.
```

---

# 4. Relational Memory — Signal

## 4.1 Construct basis

Relational integration and maintenance are credible cognitive targets.

Chuderski (2014) found that a relational-integration task predicted fluid reasoning above several conventional working-memory measures. Cho, Holyoak and Cannon (2007) showed that analogical reasoning draws on:

```text
relational integration
+ active maintenance
+ interference resolution
```

These findings support the importance of holding and comparing relations. They are correlational/mechanistic evidence, not proof that training a relational n-back task improves reasoning.

## 4.2 N-back is not interchangeable with complex span

The proposed Relational Memory task is a custom relation-token or majority-relation n-back. Its interpretation must not borrow validity automatically from G Track complex span.

Jaeggi et al. (2010) concluded that n-back was useful experimentally but, in their studies, was not a useful individual-differences working-memory measure partly because of insufficient reliability.

Redick and Lindsey’s (2013) meta-analysis found only a weak relationship between complex span and n-back and concluded that the paradigms should not be used interchangeably. Later psychometric commentary correctly notes that both may indicate a wider latent working-memory construct when task-specific and paradigm-specific variance are modelled. The appropriate conclusion is therefore:

```text
n-back is a legitimate experimental task family

but

one n-back score is not automatically a general working-memory-capacity score
and is not interchangeable with complex span.
```

## 4.3 Training-transfer boundary

The broader training literature is cautionary.

De Simoni and von Bastian (2018) found strong task-specific gains following updating and binding training but Bayesian evidence against broad near and far transfer.

Ripp et al. (2022) found no cognitive or neuroimaging transfer after eight weeks of adaptive n-back training in healthy middle-aged adults.

Recent systematic work suggests that observed working-memory benefits are generally small and strongly influenced by similarity between training and outcome tasks.

The exact Relational Memory Signal task has no direct training study.

## 4.4 Revised judgement

```text
construct basis:
STRONG

task-family basis:
MODERATE

exact protocol:
PLAUSIBLE, NOT ESTABLISHED

exact training benefit:
NOT ESTABLISHED

workflow transfer:
NOT ESTABLISHED
```

The previous `exact_protocol: moderate` should be downgraded.

## 4.5 Required validation

The first exact-task study should test:

```text
internal consistency and reliability curves
7–14-day test–retest reliability
wrong-lag lure discrimination
relation-reversal errors
response bias and match-frequency effects
separate clean and majority-relation factors
convergence with relational integration and complex span
separation from perceptual extraction performance
practice effects and adaptive-level stability
```

The app must preserve two outputs:

```text
Clean Relational Memory
maintenance/comparison with minimal perceptual uncertainty

Relational Memory under uncertainty
majority extraction + relation maintenance + n-back comparison
```

The second should not be described as a cleaner pure working-memory measure. It is a compound processing-under-uncertainty measure.

## 4.6 Public wording

> **WM Coach Relational Memory practises maintaining and comparing visual relations across delay and interference.**

Required caveat:

> **The trained operation is clearly defined, but the exact task’s reliability and benefits on untrained memory, reasoning or professional workflows have not yet been established.**

---

# 5. Binding Memory — Signal

## 5.1 Construct and task-family basis

Visual working-memory change-detection and binding paradigms provide a strong basis for studying whether features and locations remain correctly associated.

The G Track and WM Coach specifications target:

```text
feature maintenance
location maintenance
feature–location conjunctions
partial-match lures
swap lures
source/context analogues
```

This is consistent with the established visual-binding literature and the wider source-monitoring framework.

## 5.2 Reliability evidence does not validate the exact app

Dai et al. (2019) found test–retest correlations for visual-working-memory K estimates ranging from approximately `.50` to `.76`, with reliability tending to improve at larger set sizes and when testing occurred at the same time of day.

Zhao, Vogel and Awh (2023) found that change localisation measured substantially overlapping variance with change detection while offering higher reliability and requiring fewer trials. In their experiments, split-half reliability was around `.90` or above for localisation, and approximately 50–75 trials could achieve strong reliability.

These findings show that short, reliable visual-working-memory assessment is possible with deliberate design. They do not validate the exact IQ Mindware binary same/different binding n-back.

## 5.3 Swap errors require a model, not a label

A swap response should not automatically be interpreted as a pure binding failure.

McMaster et al. (2022) showed that swap errors in cued visual recall could be quantitatively explained by variability in the cue feature, causing selection of a similar non-target item.

A 2025 arXiv preprint by Radmard, Bays and Lengyel uses a flexible Bayesian non-parametric mixture model and suggests that swap errors may have multiple dependencies, including possible encoding contributions. This is a useful modelling watchlist source, not product validation.

The app should therefore distinguish candidate causes:

```text
cue or location uncertainty
feature-encoding noise
conjunction loss
retrieval selection error
wrong-lag intrusion
response strategy
```

## 5.4 Training-transfer boundary

De Simoni and von Bastian (2018) provide directly relevant negative evidence: binding-training practice gains did not generalise broadly under their active-control design.

The exact WM Coach Binding Signal task has no direct training study.

## 5.5 Revised judgement

```text
construct basis:
STRONG

task-family basis:
STRONG for visual binding/change detection

exact protocol:
PLAUSIBLE, NOT ESTABLISHED

exact training benefit:
NOT ESTABLISHED

broad transfer:
CONFLICTING, WITH STRONG NULL EVIDENCE

workflow transfer:
NOT ESTABLISHED
```

The previous `exact_protocol: moderate` should be downgraded.

## 5.6 Required validation

```text
internal consistency and reliability curves
7–14-day test–retest reliability
partial-match and swap-error models
comparison of binary detection with change localisation
convergence with an established visual-binding task
separation of feature memory from conjunction memory
set-size and lure-balance optimisation
practice effects
source/context transfer as a separate outcome
```

A change-localisation benchmark should be considered for G Track or as an implementation-validation comparator because it may offer a better reliability/efficiency trade-off than a binary detection score.

## 5.7 Public wording

> **WM Coach Binding Memory practises remembering which visual feature, location or context belongs with which other element.**

Required caveat:

> **The paradigm basis is strong, but the exact app’s reliability, error model and benefits for source memory or real workflows remain under validation.**

---

# 6. Explicit Reasoning — measurement architecture

## 6.1 Alignment with the app specification

The reasoning specification correctly preserves three wrappers:

```text
symbolic
nonsense-semantic
domain-semantic verbal
```

and four relation families:

```text
Order / Chain
Transformation / Analogy
Rule / Constraint
Prediction / Strategic Path
```

The purpose is not to create one verbal quiz. It is to test recovery of the same relation across formal, unfamiliar-semantic and meaningful wrappers.

This is consistent with the full-app requirement that one shared graph structure be projected into different cognitive operations.

## 6.2 Why percentage correct is insufficient

Belief-bias research demonstrates that semantic believability can influence endorsement independently of logical validity.

Trippas et al. (2018) reanalysed 22 confidence-rating studies with 993 participants using hierarchical Bayesian signal-detection models. Their results show why validity discriminability and acceptance bias must be separated rather than analysed only through linear accuracy averages.

The reasoning task must therefore separate:

```text
formal validity sensitivity
response/acceptance criterion
semantic believability or desirability influence
cannot-tell discrimination
lure false acceptance
confidence calibration
```

A current bioRxiv preprint by Kean et al. reports dissociation between formal logical reasoning and the natural-language network using fMRI and severe-aphasia evidence. It supports keeping formal and natural-language wrappers distinct as a design hypothesis. It does not validate a training protocol and remains prepublication evidence.

## 6.3 Required factorial item design

Every item should be coded across independent dimensions.

### Structural factors

```text
graph family
operation tags
premise count
relation count
identity-binding count
operation-mix count
delay or distractor condition
lure type
formal status
```

### Surface factors

```text
wrapper: symbolic / nonsense / domain
semantic congruence
believability
outcome desirability where ethically appropriate
domain familiarity
reading demand
```

### Formal-status factors

For deductive items:

```text
follows / valid
contradicted / invalid
underdetermined / cannot tell
```

For analogy items:

```text
same relation
different relation
underdetermined
```

For probabilistic path items:

```text
probability estimate
or
likely / rare / impossible / cannot tell
```

Probabilistic conclusions should not be scored using the same binary-validity model as deductive conclusions.

## 6.4 Trial response and confidence

Each scored item should include:

```text
primary judgement
response time
trial-level confidence or probability
optional request for another diagnostic sample in Evidence/Commit modes
```

Confidence should preferably be recorded on a scale that permits proper scoring, such as a probability or sufficiently granular confidence scale.

## 6.5 Core measurement outputs

### Reasoning Signal

```text
formal discriminability / validity sensitivity
acceptance criterion / response bias
cannot-tell discrimination
belief-congruence effect
lure false-acceptance rate
wrapper-specific performance
wrapper recovery
```

### Reasoning Evidence

```text
diagnostic-evidence weighting
independent-versus-repeated evidence sensitivity
disconfirmation response
belief revision after counterevidence
alternative-model comparison
cannot-tell preservation
```

### Reasoning Predictive Calibration

```text
Brier score or proper probability score
calibration intercept and slope
confidence resolution
meta-d′ / d′ where SDT assumptions are suitable
overconfidence by lure and wrapper
confidence update after diagnostic evidence
```

### Reasoning Commit

```text
samples to closure
premature acceptance/rejection
excess sampling
appropriate defer/test choices
threshold adaptation to cost, risk and reversibility
forced-choice at maximum samples
```

## 6.6 Candidate statistical models

The first model tournament should compare:

```text
hierarchical item-response model
hierarchical signal-detection model
multinomial processing-tree model for validity and bias
joint accuracy–confidence model
sequential-sampling model for Evidence and Commit
```

No one model should be declared universal across all four relation families.

Primary held-out evaluation should use participant-isolated predictive likelihood or log density, supplemented by:

```text
probability calibration
item and participant parameter recovery
bootstrap stability
whole-dataset transport
next-session prediction
```

## 6.7 Instructional and training evidence

The adjacent literature offers a positive but bounded training signal.

- Adaptive metacognitive feedback improved Brier calibration and metacognitive efficiency in Carpenter et al. (2019), with generalisation to untrained stimuli and a recognition-memory task.
- Guo’s (2022) meta-analysis found positive effects of metacognitive prompts on self-regulated-learning activities and learning outcomes in computer-based learning environments; effects depended on prompt specificity, adaptability and feedback.
- Nesbit and Liu’s (2025) systematic review found a large and varied higher-education argument-mapping literature, but not a single homogeneous effect estimate that validates a short reasoning game.
- A 2025 Nature Human Behaviour meta-analysis of 54 randomised trials and 10,941 participants found a small improvement in targeted cognitive-bias outcomes (`g = .26`) but unclear/high risk of bias, some publication-bias risk and unresolved real-world transfer.
- Natural-frequency formats improve Bayesian reasoning relative to conditional-probability formats, but performance depends partly on numeracy and users may employ multiple non-Bayesian strategies.
- O’Leary and Fletcher (2024) found that reflecting on counterevidence could support belief updating, but the added metacognitive-reflection manipulation produced limited incremental evidence.

This supports:

```text
adjacent instructional evidence:
MODERATE

exact IQ Mindware reasoning-game training benefit:
NOT ESTABLISHED

consequential professional judgement transfer:
NOT ESTABLISHED
```

---

# 7. Reasoning mode decisions

## 7.1 Reasoning Signal

```text
construct basis:
STRONG

exact item bank:
PLAUSIBLE, NOT ESTABLISHED

exact training benefit:
NOT ESTABLISHED

adjacent instructional evidence:
MODERATE
```

Candidate public wording:

> **The planned Reasoning task measures whether a relational structure can be recovered across symbolic, unfamiliar-semantic and meaningful verbal forms.**

Do not say that the task trains general critical thinking until a controlled study with an independent reasoning outcome supports that claim.

## 7.2 Reasoning Evidence

```text
construct basis:
STRONG

exact sequential argument task:
PLAUSIBLE, NOT ESTABLISHED

adjacent instructional evidence:
MODERATE

workflow transfer:
NOT ESTABLISHED
```

The task should compare repeated and independent evidence, include explicit counterevidence and protect cannot-tell responses.

## 7.3 Reasoning Predictive Calibration

```text
construct/measurement basis:
STRONG

general adaptive metacognitive-training signal:
MODERATE

exact IQM profile:
PLAUSIBLE, NOT ESTABLISHED
```

It remains a derived profile, not a fourth game or truth score.

## 7.4 Reasoning Commit

```text
construct basis:
MODERATE–STRONG

exact task:
PLAUSIBLE, NOT ESTABLISHED

training benefit:
NOT ESTABLISHED
```

Commit should be built after the sequential Evidence task because a stopping threshold cannot be interpreted without a well-defined sampling environment.

---

# 8. Belief calibration and reframing

## 8.1 Professional belief calibration

The defensible non-clinical target is:

```text
separate validity from believability
separate evidence strength from repetition
preserve underdetermination
track confidence against evidence quality
seek disconfirmation
choose accept / reject / defer / test
```

Website status:

```text
EVIDENCE-INFORMED
PILOT-READY AFTER TASK VALIDATION
NOT VALIDATED IN WORKFLOW
```

It is not a truth detector, ideology measure, personality assessment or employee-selection tool.

## 8.2 Evidence-sensitive reframing

A non-clinical domain-semantic route may use:

```text
initial interpretation
→ plausible alternatives
→ evidence for and against each
→ calibrated confidence
→ small informational or behavioural test
→ update after feedback
```

This is a structured reasoning and model-testing exercise. It must not be represented as psychotherapy or treatment.

## 8.3 Health-related interpretation or reappraisal

Any condition-specific use remains:

```text
partner-led
research/service governed
condition-specific
professionally overseen
separate from ordinary self-service recommendations
```

Category-level reappraisal or interpretation-bias evidence is not direct evidence for the exact Reasoning Coach.

---

# 9. 20-cell promotion board

| Capacity | Signal | Evidence | Predictive Calibration | Commit |
|---|---|---|---|---|
| **Attention Control** | **Literature-audited; expert-review candidate with variant split** | Remain draft | Remain draft / derived | Remain draft |
| **Relational Memory** | **Literature-audited; retain draft pending exact-task psychometrics** | Remain draft | Remain draft / derived | Remain draft |
| **Binding Memory** | **Literature-audited; retain draft pending exact-task psychometrics and error model** | Remain draft | Remain draft / derived | Remain draft |
| **Path Prediction** | Retain draft | Retain draft | Retain draft / derived | Retain draft |
| **Reasoning** | **Measurement model specified; retain draft** | **Measurement model specified; retain draft** | **Derived model specified; retain draft** | **Prototype requirements specified; retain draft** |

This board does not reject the remaining cells. It records that they still require promotion-oriented source audits and exact-task validation.

---

# 10. Required studies

## Study 1 — Attention Signal implementation equivalence

```text
reference MFT-M versus IQM classic absolute implementation
adaptive score concordance
frame-count timing and device transport
reliability curves
entropy/exposure response function
relative-frame and optic-flow variant separation
```

## Study 2 — Relational and Binding Signal psychometrics

```text
repeated sessions
reliability curves
clean versus uncertain relational factors
wrong-lag and lure validity
binding partial-match and swap models
comparison with complex span, relational integration and established VWM tasks
practice effects
```

## Study 3 — Explicit Reasoning item-bank calibration

A factorial item pool should cross:

```text
4 graph families
× 3 wrappers
× formal status
× semantic congruence
× lure type
× controlled demand dimensions
```

It should estimate:

```text
item difficulty and discrimination
formal validity sensitivity
response bias
cannot-tell discrimination
belief/believability effects
confidence calibration
test–retest reliability
alternate-form equivalence
```

## Study 4 — Mode dissociation

Within Reasoning, test whether Signal, Evidence and Commit provide separable held-out parameters and whether the Calibration model predicts later performance beyond accuracy and response time.

## Study 5 — Controlled training and transfer

Only after measurement validity:

```text
active control
reasoning Signal only
reasoning Evidence + Calibration
full Evidence + Calibration + Commit
```

Outcomes:

```text
trained-item learning
held-out item families
wrapper recovery
independent reasoning benchmark
workflow simulation
delayed re-check
```

---

# 11. Prepublication policy

The following may inform design but cannot alone support production approval:

- Kean et al. formal-reasoning/language dissociation, bioRxiv;
- Radmard, Bays and Lengyel swap-error mixture model, arXiv;
- other quality preregistered or open-analysis preprints added to the watchlist.

Every material preprint contribution must remain labelled:

```text
publication_status: preprint
review_status: prepublication_watchlist
```

---

# 12. Final candidate position

```text
Attention Signal
has the strongest direct route to expert review,
provided the classic/adaptive anchor is separated from original wrappers.

Relational Signal
has a strong construct rationale but not yet an exact-app validation basis.

Binding Signal
has a strong paradigm rationale but requires an exact psychometric and error model.

Explicit Reasoning
has a strong measurement-development rationale,
but needs a calibrated factorial item bank and hierarchical measurement model
before any broad training or critical-thinking claim.
```

The commercially useful public distinction is:

> **Available task** does not mean **validated transfer benefit**. IQ Mindware can accurately describe what each live task practises while using G Track and future workflow outcomes to test what changes beyond the task.

---

# References added or emphasised in this review

- Carpenter, J., Sherman, M. T., Kievit, R. A., Seth, A. K., Lau, H., & Fleming, S. M. (2019). Domain-general enhancements of metacognitive ability through adaptive training. *Journal of Experimental Psychology: General, 148*(1), 51–64. https://doi.org/10.1037/xge0000505
- Dai, M., Li, Y., Gan, S., & Du, F. (2019). The reliability of estimating visual working memory capacity. *Scientific Reports, 9*, 1155. https://doi.org/10.1038/s41598-019-39044-1
- De Simoni, C., & von Bastian, C. C. (2018). Working memory updating and binding training: Bayesian evidence supporting the absence of transfer. *Journal of Experimental Psychology: General, 147*(6), 829–858. https://doi.org/10.1037/xge0000453
- Guo, L. (2022). Using metacognitive prompts to enhance self-regulated learning and learning outcomes: A meta-analysis of experimental studies in computer-based learning environments. *Journal of Computer Assisted Learning, 38*(3), 811–832. https://doi.org/10.1111/jcal.12650
- He, X., Qiu, B., Deng, Y., Liu, T., Chen, Y., & Zhang, W. (2022). Adaptive assessment of the capacity of cognitive control. *Quarterly Journal of Experimental Psychology, 75*(1), 43–52. https://doi.org/10.1177/17470218211030838
- Jaeggi, S. M., Buschkuehl, M., Perrig, W. J., & Meier, B. (2010). The concurrent validity of the N-back task as a working memory measure. *Memory, 18*(4), 394–412. https://doi.org/10.1080/09658211003702171
- Kean, H., et al. (2026). Evidence from formal logical reasoning reveals that the language of thought is not natural language. *bioRxiv*. https://doi.org/10.1101/2025.07.26.666979
- Kim, S. (2024). Natural frequencies improve public understanding of medical test results: An experimental study on various Bayesian inference tasks with multiple scoring methods and non-Bayesian reasoning strategies. *Medical Decision Making, 44*(8), 890–899. https://doi.org/10.1177/0272989X241275191
- McMaster, J. M. V., Tomić, I., Schneegans, S., & Bays, P. M. (2022). Swap errors in visual working memory are fully explained by cue-feature variability. *Cognitive Psychology, 137*, 101493. https://doi.org/10.1016/j.cogpsych.2022.101493
- Nesbit, J. C., & Liu, Q. (2025). Argument mapping in higher education: A systematic review. *Higher Education Quarterly, 79*(4), e70063. https://doi.org/10.1111/hequ.70063
- O’Leary, A. P., & Fletcher, W. (2024). Thinking about believing: Can metacognitive reflection encourage belief updating? *Journal of Intelligence, 12*(5), 47. https://doi.org/10.3390/jintelligence12050047
- Radmard, P., Bays, P. M., & Lengyel, M. (2025). A flexible Bayesian non-parametric mixture model reveals multiple dependencies of swap errors in visual working memory. *arXiv:2505.01178*. https://doi.org/10.48550/arXiv.2505.01178
- Redick, T. S., & Lindsey, D. R. (2013). Complex span and n-back measures of working memory: A meta-analysis. *Psychonomic Bulletin & Review, 20*, 1102–1113. https://doi.org/10.3758/s13423-013-0453-9
- Ripp, I., Emch, M., Wu, Q., et al. (2022). Adaptive working memory training does not produce transfer effects in cognition and neuroimaging. *Translational Psychiatry, 12*, 512. https://doi.org/10.1038/s41398-022-02272-7
- Swaryandini, G., Graham, J., Griffith, S., et al. (2025). Systematic review and meta-analysis of educational approaches to reduce cognitive biases among students. *Nature Human Behaviour, 9*, 2510–2538. https://doi.org/10.1038/s41562-025-02253-y
- Trippas, D., Kellen, D., Singmann, H., et al. (2018). Characterizing belief bias in syllogistic reasoning: A hierarchical Bayesian meta-analysis of ROC data. *Psychonomic Bulletin & Review, 25*, 2141–2174. https://doi.org/10.3758/s13423-018-1460-7
- Zhao, C., Vogel, E., & Awh, E. (2023). Change localization: A highly reliable and sensitive measure of capacity in visual working memory. *Attention, Perception, & Psychophysics, 85*(5), 1681–1694. https://doi.org/10.3758/s13414-022-02586-0
