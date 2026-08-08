# G Track Attention and Zone Evidence Review

**Version:** draft v0.1.0  
**Date:** 8 August 2026  
**Status:** research review; not approved for production claims  
**Scope:** SART, Stroop, Flanker, the combined Attention profile, the four exploratory response profiles and the provisional Zone estimate  
**Parent registry:** `../measurement-registry.json`  
**Governing evidence policy:** `../../docs/EVIDENCE_GRADING.md`

---

## 1. Purpose

This review evaluates the scientific basis for the G Track Attention and Zone records before they are promoted from `draft` to `expert_reviewed` or `approved`.

It separates four questions that are often conflated:

```text
1. Does the task produce a robust experimental effect?
2. Does it measure stable differences between people reliably?
3. Does it measure meaningful within-person change or state variation reliably?
4. Has the exact G Track implementation and scoring model been validated?
```

A robust Stroop effect, for example, does not by itself establish that a short Stroop difference score is a reliable measure of an individual or of day-to-day state change. Likewise, evidence that attention fluctuates among latent states does not validate the exact G Track four-profile solution.

The current human-readable evidence registry already makes the correct high-level distinction among measurement/source validity, exact implementation validity and training-benefit evidence. This review sharpens those distinctions for the Attention and Zone components.

---

## 2. Evidence hierarchy and prepublication policy

### 2.1 Evidence order

Use this order when grading a registry claim:

```text
peer-reviewed direct evidence for the exact task and interpretation
→ peer-reviewed evidence for a closely matched task or scoring model
→ peer-reviewed adjacent mechanistic evidence
→ high-quality preprint or preregistered report
→ internal retrospective or pilot evidence
→ theory-led hypothesis
```

The position of a source in this hierarchy does not automatically determine quality. Study design, sample size, measurement fidelity, analysis transparency, directness and replication all matter.

### 2.2 Preprints

arXiv, PsyArXiv and bioRxiv papers may be included when they contribute:

- a relevant new statistical model;
- an openly inspectable analysis pipeline;
- a large or unusually dense dataset;
- a direct challenge to an existing measurement assumption;
- a useful preregistered or replication-oriented design.

They must carry:

```text
publication_status: preprint
review_status: watchlist or expert_reviewed
```

A preprint must not, by itself:

- upgrade an exact product claim to `strong`;
- justify a validated-state label;
- justify consequential routing;
- override higher-quality peer-reviewed contrary evidence;
- appear in public copy without a visible prepublication status where it materially supports the claim.

Recommended tag:

```text
prepublication_watchlist
```

---

# 3. Executive evidence decisions

## 3.1 Main conclusions

1. **The SART has a defensible sustained-attention and slips-of-action origin, but it is a multi-process task.** Commission errors, response speed, omissions and variability are jointly shaped by attention, response strategy, motor control and the high-Go/low-No-Go structure.

2. **SART commission errors should not be used alone as a direct vigilance or mind-wandering score.** Instructions, Go-trial prevalence, motor-response requirements and speed–accuracy policy can substantially change commission rates.

3. **The Stroop and Flanker effects are strong experimental phenomena, but conventional short difference scores are often weak measures of individual differences.** This is the reliability paradox.

4. **Short conflict tasks can be made substantially more reliable.** Calibrated task variants, stronger between-person discrimination, trial-level modelling and carefully constructed short forms have produced good psychometric results. Those findings support redesign and modelling, not automatic validation of the current G Track versions.

5. **The Stroop is currently a weak basis for session-level Zone inference if scored as a conventional congruent-minus-incongruent difference.** Intensive longitudinal evidence reports poor within-person reliability and modest occasion-specific variance for standard Stroop scores.

6. **A multi-indicator battery is scientifically preferable to treating one task as “attention”.** However, Stroop, Flanker, SART performance and self-reported focus do not necessarily form one simple factor, and the exact G Track combined model remains pilot-supported rather than externally validated.

7. **External sustained-attention research supports probabilistic and time-varying attention states, but not the exact G Track four-profile taxonomy.** The number, duration and meaning of latent states vary with task, model and measurement modality.

8. **The provisional Zone estimate should remain a behavioural context estimate.** It should use repeated personal baselines, probabilities, uncertainty and abstention. It should not be described as a brain state, diagnosis, cause of performance, or validated intervention selector.

---

## 3.2 Proposed grade summary

| G Track record | Experimental / construct basis | Stable individual-difference measurement | Within-person / state measurement | Exact G Track status | Proposed public status |
|---|---|---|---|---|---|
| **SART engagement consistency** | **Moderate–strong** | **Moderate** when multi-indicator and sufficiently sampled | **Moderate / promising** for repeated brief mobile use | **Moderate; validation required** | Published anchor with multi-process qualification |
| **SART response-control stability** | **Moderate** | **Moderate** | **Moderate** under repeated measurement | **Moderate; validation required** | Established Go/No-Go basis, strategy-sensitive |
| **Stroop conflict control** | **Strong experimental effect** | **Weak–moderate for a standard short difference; stronger in calibrated variants** | **Weak for conventional session-level difference scores** | **Moderate/provisional** | Published anchor; reliability caution required |
| **Flanker selective attention / response competition** | **Strong experimental effect** | **Weak–moderate for a standard short difference; stronger in calibrated variants** | **Unestablished for the exact short G Track form** | **Moderate/provisional** | Published anchor; reliability caution required |
| **Combined Attention profile** | **Moderate rationale for multi-indicator measurement** | **Model dependent** | **Model dependent** | **Plausible / pilot-supported** | Research profile; prospective validation required |
| **Four response profiles** | **Adjacent support for heterogeneous performance patterns** | **Not externally validated as these four profiles** | **Internal pilot only** | **Internal recovery / pilot-supported** | Exploratory behavioural response profiles |
| **Zone estimate** | **Adjacent support for fluctuating attention dynamics** | **Requires repeated personal baseline** | **Pilot-supported; prospective validation required** | **Plausible / pilot-supported** | Provisional behavioural context estimate |

The key grading correction is to distinguish:

```text
robust task effect
from
reliable person-level or state-level measurement
```

---

# 4. Detailed task review

## 4.1 SART — engagement consistency

### Original evidence

Robertson et al. (1997) introduced the SART as a laboratory model of slips of action and sustained-attention failures. In the original work, SART performance correlated with established sustained-attention measures and reports of everyday attentional failures, and pre-error responses accelerated before commission errors.

This supports a genuine sustained-attention origin, but it does not establish that every SART output is a pure measure of vigilance.

### Multi-process boundary

Later experimental work shows that SART performance is highly sensitive to response policy:

- changing Go-stimulus prevalence changes response speed and commission errors;
- speed versus accuracy emphasis shifts the speed–accuracy trade-off;
- prolonging or complicating the motor response reduces commission errors;
- response delays can reduce commission errors even when stimulus duration is brief.

The most defensible interpretation is therefore:

```text
SART performance reflects a joint system involving
sustained task engagement
+ response policy
+ motor inhibition/control
+ speed–accuracy calibration
+ occasional lapses or disengagement
```

### Repeated smartphone evidence

Perzl et al. (2024) adapted the SART for daily smartphone administration over two weeks in healthy adults. The 90-second version showed promising reliability and validity of change, supporting brief repeated measurement in naturalistic contexts. This is directly relevant to G Track, but it is not validation of the exact G Track trial count, interface, timing, scoring or population.

### Construct-valid battery evidence

Welhaf and Kane (2024), and Welhaf, Meier and Kane (2025), argue that sustained-attention consistency is better represented by shared variance among objective performance indicators and subjective task-unrelated-thought reports than by either measurement family alone. This supports a multi-indicator approach and cautions against treating one SART score as the whole construct.

### Recommended record change

```text
measurement_source_level:
moderate_strong

exact_implementation_level:
moderate

state_measurement_status:
promising_repeated_measurement
```

Recommended public wording:

> **Estimates the consistency of task engagement during repetitive responding.**

Required caveat:

> Performance also reflects response strategy, motor control, speed–accuracy trade-offs and the task’s high-Go/low-No-Go structure. It does not identify why engagement was less stable.

Do not use:

- “measures arousal”;
- “detects mind wandering”;
- “detects fatigue”;
- “measures vigilance” without qualification;
- one commission-error threshold as a state label.

---

## 4.2 SART — response-control stability

The SART has a clear Go/No-Go and response-inhibition component, but its commission errors are not a process-pure inhibition score. They are conditional on:

- Go/No-Go prevalence;
- response deadline;
- motor interface;
- task instructions;
- participant strategy;
- anticipatory responding;
- current speed–accuracy policy.

A response-control interpretation is more defensible than treating commissions as a pure attention-lapse index, provided the score is interpreted jointly with omissions, anticipations, response speed and variability.

### Recommended record change

```text
measurement_source_level:
moderate

exact_implementation_level:
moderate
```

Recommended public wording:

> **Tracks response-control stability alongside response speed and variability.**

Required caveat:

> Commission errors cannot be interpreted independently of omissions, anticipations, response speed, variability and the participant’s speed–accuracy strategy.

---

## 4.3 Stroop — conflict-control estimate

### Strong experimental effect

The congruency effect in Stroop tasks is a robust experimental phenomenon. It is reasonable to describe the task as imposing conflict between task-relevant and task-irrelevant information.

### Reliability paradox

Hedge et al. (2018) showed that classic cognitive tasks can produce highly replicable group effects while providing poor reliability for individual differences. Kucina et al. (2023) demonstrated that benchmark Stroop, Flanker and Simon implementations can require very large trial counts for stable person-level estimates, but carefully calibrated variants can produce reliable estimates in under 100 trials.

Burgoyne et al. (2023) developed Stroop Squared, Flanker Squared and Simon Squared tasks that each take under three minutes and reported high internal consistency, meaningful test–retest reliability and strong latent-variable convergence. This is important positive evidence that brief tasks can work when specifically designed for individual-difference measurement.

The conclusion is not that any three-minute Stroop is reliable. It is that psychometric task design matters.

### State measurement boundary

Hachenberger et al. (2024/2025) used intensive longitudinal measurement and dynamic structural equation modelling. Conventional Stroop error rates and congruency RT differences showed poor within-person reliability and only modest occasion-specific variance. This is particularly important for the Zone use case: a standard short Stroop difference score should not be treated as a high-confidence session-state measure.

### Recommended record change

Separate the construct and score claims:

```text
experimental_construct_level:
strong

standard_difference_score_reliability:
weak_to_moderate

within_person_state_reliability:
weak_for_conventional_score

exact_implementation_level:
moderate_provisional
```

Recommended public wording:

> **Estimates performance when relevant and irrelevant response information conflict.**

Required caveat:

> The Stroop effect is robust at group level, but a short congruent-minus-incongruent difference score may be unreliable for comparing individuals or interpreting one session. G Track must validate its trial count and scoring model.

---

## 4.4 Flanker — selective attention and response competition

The Flanker task robustly manipulates response competition from surrounding distractors. As with Stroop, however, a robust experimental effect does not ensure a reliable individual-difference score.

The reliability-paradox evidence applies directly to classic Flanker scores. Kucina et al. demonstrate that calibrated Flanker designs can overcome much of the problem, and Burgoyne et al. show that a brief Flanker Squared task can achieve good psychometric properties. These results support redesign or calibration if G Track’s exact short form proves unreliable.

The Stroop and Flanker should not automatically be treated as interchangeable indicators of one inhibition process. Latent-variable work often finds weak cross-task correlations and substantial task-specific variance.

### Recommended record change

```text
experimental_construct_level:
strong

standard_difference_score_reliability:
weak_to_moderate

within_person_state_reliability:
unestablished_for_exact_form

exact_implementation_level:
moderate_provisional
```

Recommended public wording:

> **Estimates selective attention when surrounding information activates a competing response.**

Required caveat:

> Reliability depends on trial count, condition balance, timing, scoring and task design. A simple congruency difference should not be used alone.

---

# 5. Combined Attention profile

## 5.1 Why a combined battery is sensible

A combined battery is preferable to equating one task with attention because the tasks sample partly different processes:

```text
SART
engagement consistency + response policy + Go/No-Go control

Stroop
semantic / response conflict

Flanker
surrounding distractor and response competition
```

Recent sustained-attention work supports combining objective indicators and, where appropriate, subjective context measures. Multi-task measurement can reduce dependence on one task’s idiosyncrasies.

## 5.2 Why a simple average is not justified

The external literature also warns that:

- conflict-task correlations are often low;
- difference scores can be unreliable;
- within-person reliability differs from between-person reliability;
- state variance and measurement error can be confused;
- motivation, goals, fatigue, device and response strategy influence performance;
- latent structures can differ across samples and task implementations.

Therefore:

```text
combined battery rationale:
moderate

exact G Track composite or mixture model:
pilot_supported / plausible
```

Do not calculate a single attention score by blindly averaging standardised task outputs.

---

# 6. Four exploratory behavioural profiles

## 6.1 What external research supports

External research supports the general propositions that:

- sustained attention fluctuates over multiple timescales;
- periods of stable and variable performance can be distinguished;
- latent-state and hidden-Markov approaches can recover multiple behavioural states;
- attention dynamics differ substantially between people;
- RT distribution components convey different information.

Esterman et al. (2013) distinguished relatively stable/accurate and variable/error-prone periods during a gradual continuous performance task. Yamashita et al. (2021) used more than 20,000 participants and ex-Gaussian modelling to separate a strategy component, pervasive variability and a long-tail component. Only the pervasive variability component consistently distinguished the two fMRI-derived attention states in two independent datasets.

Glukhova et al. (2026) used hidden-state modelling in a common virtual-reality task across mice, monkeys and humans and recovered multiple attention states with similar temporal organisation across species.

These findings make latent-state modelling scientifically plausible.

## 6.2 What external research does not support

The external literature does not validate:

```text
exactly four G Track profiles
or
Regulated / Slow compensatory / Globally overloaded / Fast brittle
as natural kinds
or
those profiles as brain states
or
those profiles as treatment or training selectors
```

The number and meaning of states depend on:

- task design;
- observables;
- time window;
- model family;
- number of components selected;
- population;
- data quality;
- whether state or trait variance is being modelled.

### Recommended terminology

Prefer:

> **Exploratory behavioural response profile**

or:

> **Current task-performance pattern**

Avoid, until prospectively validated:

- cognitive type;
- brain state;
- neurocognitive state;
- stable profile;
- validated Zone;
- intervention selector.

---

# 7. Provisional Zone estimate

## 7.1 Current defensible interpretation

The Zone estimate can currently be described as:

> **A provisional, uncertainty-aware summary of the current task-performance pattern, interpreted relative to a developing personal baseline.**

It should integrate, at minimum:

- SART engagement-consistency indicators;
- response-policy and inhibition indicators;
- Stroop and Flanker condition-level performance;
- data quality;
- timing quality;
- trial yield;
- uncertainty;
- repeated personal history.

## 7.2 Trait–state separation

The model should produce two separate objects:

```text
PERSONAL BASELINE PROFILE
estimated across repeated usable sessions

CURRENT SESSION DEVIATION
how today differs from that baseline, with uncertainty
```

Kadlec et al. (2024) show that multiple days may be required for trait-like stability and that reliability curves differ across cognitive domains. Perzl et al. (2024) supports repeated brief mobile SART measurement. Hachenberger et al. shows why task-specific within-person reliability must be demonstrated rather than assumed.

## 7.3 Required abstention

The system should return `insufficient evidence` or `timing limited` when:

- too few valid trials are available;
- device timing is unstable;
- response omissions suggest disengagement or technical failure;
- the posterior profile probabilities are diffuse;
- the session is globally inconsistent;
- the current device/input method differs materially from baseline;
- no stable personal baseline exists and a population classification would be over-interpreted.

## 7.4 Routing boundary

No Zone output should alter training dosage or recommend a health action as a validated rule until a low-risk prospective routing study demonstrates benefit and absence of material harm.

---

# 8. Required scoring architecture

## 8.1 SART outputs

Retain separate outputs rather than one composite:

```text
commission rate
omission rate
anticipation rate
median correct-Go RT
robust within-session RT variability
RT slope / time-on-task trend
post-error slowing or policy adjustment
response criterion / bias where estimable
```

Consider distributional modelling:

```text
ex-Gaussian μ
= central response strategy / speed component

ex-Gaussian σ
= pervasive variability component

ex-Gaussian τ
= tail / occasional extreme component
```

Yamashita et al. supports the value of separating these components, but G Track should compare ex-Gaussian, shifted-lognormal and robust non-parametric alternatives rather than assuming one distribution is correct.

## 8.2 Stroop and Flanker outputs

Do not use a simple RT difference as the sole primary score.

Retain:

```text
condition-level RT distributions
condition-level accuracy
fast-error rates
omissions and anticipations
conflict-related random slope
trial-level posterior uncertainty
speed–accuracy relationship
practice and time-on-task trends
```

Recommended model family:

```text
hierarchical trial-level model
with person intercepts
+ person-specific conflict slopes
+ trial difficulty / condition effects
+ lapse or contaminant component
+ device / input covariates
```

Candidate observation models include:

- shifted lognormal RT models;
- diffusion or evidence-accumulation models where identifiable;
- hierarchical Bayesian accuracy/RT models;
- robust mixed-effects models;
- latent state–trait models for repeated sessions.

## 8.3 Combined profile models

Compare at least:

```text
M0: probabilistic one-factor model
M1: correlated task-specific factors
M2: dimensional profile model
M3: finite mixture / latent profile model
M4: hidden-state model across repeated sessions
```

Model comparison should use participant-isolated held-out predictive log density or likelihood per valid observation, with calibration, bootstrap stability and whole-dataset transport as secondary criteria.

BIC, AIC, reconstruction error, entropy and cluster-separation indices are diagnostics rather than the universal primary score.

---

# 9. Device and online-administration requirements

Timed cognitive tests are sensitive to device and input differences. Large web datasets show slower measured RTs on mobile devices, particularly Android phones, and differences associated with touchscreen versus keyboard/mouse input.

Every G Track session should log:

```text
device class
operating system
browser and version
screen dimensions
input method
estimated refresh rate
actual frame timing where relevant
visibility / focus loss
network-independent local timestamps
requested and observed stimulus duration
```

Recommended policy:

- compare baseline and follow-up on the same device/input class where possible;
- treat cross-device changes as a separate measurement condition;
- develop device-specific calibration or statistical adjustment;
- do not pool mobile and desktop norms blindly;
- include timing-quality flags in all public reports.

---

# 10. Prepublication watchlist

These sources are useful for model development but should not independently determine public evidence grades.

## 10.1 Westrin (2026), arXiv

**Information-Theoretic Reliability is Robust to Analytic Choice: A 24-Specification Multiverse on Public Cognitive Test-Retest Data.**

Signal:

- reanalyses public Flanker, Stroop, Stop-Signal, Go/No-Go and Posner datasets;
- reports that replacing or augmenting ICC with an information-theoretic criterion does not rescue reliability;
- provides a reproducible multiverse and provenance-oriented pipeline.

Boundary:

- single preprint and reanalysis;
- proposed information-theoretic headline rule is novel;
- should reinforce the reliability caution, not establish the final G Track scoring model.

Recommended tag:

```text
prepublication_watchlist
reliability_paradox
open_pipeline
```

## 10.2 Bian, Wang and Guo (2026), arXiv

**Shared Hidden-factor Information Framework for Multiple Behavioral Tasks.**

Signal:

- jointly models multiple tasks;
- allows subject-specific latent factors, temporal structure and strategy switching;
- illustrates how cross-task information can improve parameter estimation.

Boundary:

- demonstrated with Probabilistic Reward and Flanker tasks in MDD;
- not a validation of the G Track battery or Zone states.

Use:

- candidate architecture for joint task modelling;
- simulation comparison against separate-task models.

## 10.3 Mistry et al. (2024), bioRxiv

**Computational Modeling of Proactive, Reactive, and Attentional Dynamics in Cognitive Control.**

Signal:

- hierarchical Bayesian separation of proactive, reactive and attentional components;
- large ABCD dataset;
- explicit treatment of intra-individual variability and nonergodicity.

Boundary:

- stop-signal/inhibitory-control context rather than G Track tasks;
- preprint status.

Use:

- supports modelling latent processes instead of relying on crude averages.

## 10.4 Kucyi et al. (2024), bioRxiv

**Individual variability in neural representations of mind-wandering.**

Signal:

- dense within-person neuroimaging;
- substantial idiographic variability;
- large-sample predictive models did not fully generalise to densely sampled individuals.

Boundary:

- neural and self-report study, not a behavioural Zone validation.

Use:

- supports personal-baseline and idiographic modelling;
- cautions against universal state labels.

## 10.5 Debele, Goytom and Misbah (2026), arXiv

**Pulse Focus: Validation of the Focus Performance Score as a Behavioral Signal for Human Attentional State Modeling Toward Attention-Aware AI.**

Signal:

- large mobile Stroop dataset;
- app-specific scoring and test–retest analyses;
- illustrates commercial-scale behavioural validation.

Boundary:

- unreviewed, app-specific and commercially adjacent;
- score relies heavily on incongruent RT;
- neural association analysis does not validate a momentary state classifier.

Use:

- product-validation watchlist only;
- do not upgrade Stroop or Zone evidence from this source alone.

---

# 11. Recommended source additions to the canonical registry

Suggested IDs:

```text
robertson_1997_sart
wilson_2016_sart_response_strategy
mensen_2022_sart_feedback_emphasis
perzl_2024_smartphone_sart
welhaf_kane_2024_attention_consistency
welhaf_meier_kane_2025_attention_battery
hedge_2018_reliability_paradox
kucina_2023_conflict_calibration
burgoyne_2023_attention_control_squared
hachenberger_2024_stroop_state_trait
kadlec_2024_reliability_convergence
yamashita_2021_attention_rt_components
esterman_2013_attention_states
glukhova_2026_cross_species_attention_states
germine_2021_device_effects
westrin_2026_info_reliability_preprint
bian_2026_shift_preprint
mistry_2024_prad_preprint
kucyi_2024_mind_wandering_preprint
debele_2026_pulse_focus_preprint
```

Each preprint record should include:

```json
{
  "publication_status": "preprint",
  "evidence_role": "model-development-watchlist",
  "may_support_public_claim_alone": false
}
```

---

# 12. Proposed validation study for G Track Attention

## 12.1 Primary aim

Determine whether the exact short G Track SART, Stroop and Flanker implementations provide reliable and interpretable:

```text
between-person estimates
within-person session deviations
combined profile estimates
```

## 12.2 Suggested initial design

```text
N = 200–300 adults
3–5 sessions per participant
at least one same-day retest subset
at least one 7–14 day retest
same-device repeat where possible
```

Include:

- the current G Track tasks;
- an independent sustained-attention comparator, such as gradCPT or another well-characterised continuous-performance measure;
- a calibrated brief attention-control task, such as an approved Squared or calibrated conflict-task implementation;
- short subjective context reports, treated as separate indicators rather than ground truth;
- device and timing metadata;
- a separate functional task relevant to the first workflow pilot.

## 12.3 Preregistered analyses

1. reliability curves by number of trials;
2. split-half and test–retest reliability;
3. within-person reliability and occasion specificity;
4. condition-level and difference-score comparisons;
5. hierarchical trial-level model comparison;
6. trait–state decomposition;
7. latent one-factor versus correlated-factor versus mixture models;
8. participant-isolated predictive scoring;
9. bootstrap stability;
10. cross-device and whole-dataset transport;
11. profile probability calibration;
12. abstention performance;
13. prospective prediction of an independent subsequent task.

## 12.4 Promotion gates

A record should not become `approved` merely because the task produces the expected group-level effect.

Minimum gates should include:

```text
construct check passes
+ exact implementation reliability characterised
+ intended state or trait use supported
+ scoring-model uncertainty reported
+ device effects bounded or modelled
+ claims wording reviewed
```

For Zone routing, add:

```text
prospective next-task prediction
+ low-risk routing trial
+ evidence of benefit or non-inferiority
+ no material adverse routing pattern
```

---

# 13. Immediate registry decisions

## Keep as draft

All Attention and Zone records should remain `draft` until the exact implementation data are analysed.

## Revise before expert review

1. change SART engagement from a pure `strong` vigilance interpretation to a `moderate–strong, multi-process` construct basis;
2. retain SART response control as `moderate`, with a strategy and motor-control caveat;
3. split Stroop and Flanker evidence into experimental-effect evidence and person/state reliability evidence;
4. prohibit simple interference difference scores as sole primary measures;
5. distinguish general multi-indicator rationale from exact combined-profile evidence;
6. rename the four outputs `exploratory behavioural response profiles` in public-facing materials;
7. keep Zone as `pilot_supported + prospective_validation_required`;
8. add repeated personal-baseline, uncertainty and abstention requirements;
9. add a `prepublication_watchlist` source class;
10. prevent preprints from independently upgrading public evidence levels.

---

# 14. Claims-safe website wording

## SART

> **A brief measure of engagement consistency and response-control stability during repetitive responding.**

Boundary:

> Results reflect several processes, including response strategy and motor control. They do not identify the cause of a less stable session.

## Stroop

> **A conflict task that compares performance when relevant and irrelevant information point towards the same or competing responses.**

Boundary:

> The conflict effect is well established, but the reliability of this exact short-form score is still being validated.

## Flanker

> **A selective-attention task that measures performance when surrounding information activates a competing response.**

Boundary:

> The exact short-form score requires implementation-specific reliability evidence.

## Combined profile

> **A research-stage profile combining complementary indicators rather than relying on one attention task.**

Boundary:

> The profile model remains under prospective validation.

## Zone

> **A provisional estimate of how today’s task-performance pattern compares with your developing personal baseline.**

Boundary:

> It is not a diagnosis, brain-state detector, cause attribution or proven training selector.

---

# 15. Key peer-reviewed references

Burgoyne, A. P., Tsukahara, J. S., Mashburn, C. A., & Engle, R. W. (2023). Nature and measurement of attention control. *Journal of Experimental Psychology: General*. https://doi.org/10.1037/xge0001408

Esterman, M., Noonan, S. K., Rosenberg, M., & DeGutis, J. (2013). In the zone or zoning out? Tracking behavioral and neural fluctuations during sustained attention. *Cerebral Cortex, 23*(11), 2712–2723. https://doi.org/10.1093/cercor/bhs261

Glukhova, M., Tlaie, A., Taylor, R., et al. (2026). Sharing the spotlight: Uncovering common attentional dynamics across species. *PLOS Computational Biology, 22*(4), e1014191. https://doi.org/10.1371/journal.pcbi.1014191

Hachenberger, J., Mayer, A., Kerkhoff, D., et al. (2024/2025). Within-subject reliability, occasion specificity, and validity of fluctuations of the Stroop and go/no-go tasks in ecological momentary assessment. *Behavior Research Methods, 57*, 29. https://doi.org/10.3758/s13428-024-02567-1

Hedge, C., Powell, G., & Sumner, P. (2018). The reliability paradox: Why robust cognitive tasks do not produce reliable individual differences. *Behavior Research Methods, 50*, 1166–1186. https://doi.org/10.3758/s13428-017-0935-1

Kadlec, J., Walsh, C. R., Sadé, U., Amir, A., Rissman, J., & Ramot, M. (2024). A measure of reliability convergence to select and optimize cognitive tasks for individual differences research. *Communications Psychology, 2*, 64. https://doi.org/10.1038/s44271-024-00114-4

Kucina, T., Wells, L., Lewis, I., et al. (2023). Calibration of cognitive tests to address the reliability paradox for decision-conflict tasks. *Nature Communications, 14*, 2234. https://doi.org/10.1038/s41467-023-37777-2

Mensen, J. M., Dang, J. S., Stets, A. J., & Helton, W. S. (2022). The effects of real-time performance feedback and performance emphasis on the sustained attention to response task (SART). *Psychological Research, 86*, 1972–1979. https://doi.org/10.1007/s00426-021-01602-6

Perzl, J., Riedl, E. M., & Thomas, J. (2024). Measuring situational cognitive performance in the wild: A psychometric evaluation of three brief smartphone-based test procedures. *Assessment, 31*(6). https://doi.org/10.1177/10731911231213845

Robertson, I. H., Manly, T., Andrade, J., Baddeley, B. T., & Yiend, J. (1997). ‘Oops!’: Performance correlates of everyday attentional failures in traumatic brain injured and normal subjects. *Neuropsychologia, 35*(6), 747–758. https://doi.org/10.1016/S0028-3932(97)00015-8

Welhaf, M. S., & Kane, M. J. (2024). A nomothetic span approach to the construct validation of sustained attention consistency. *Psychological Research, 88*, 39–80. https://doi.org/10.1007/s00426-023-01820-0

Welhaf, M. S., Meier, M. E., & Kane, M. J. (2025). Building a construct-valid battery of performance and self-report indicators of sustained attention consistency. *Behavior Research Methods, 57*, 306. https://doi.org/10.3758/s13428-025-02798-w

Wilson, K. M., Finkbeiner, K. M., de Joux, N. R., Russell, P. N., & Helton, W. S. (2016). Go-stimuli proportion influences response strategy in a sustained attention to response task. *Experimental Brain Research, 234*, 2989–2998. https://doi.org/10.1007/s00221-016-4701-x

Yamashita, A., Rothlein, D., Kucyi, A., et al. (2021). Variable rather than extreme slow reaction times distinguish brain states during sustained attention. *Scientific Reports, 11*, 14883. https://doi.org/10.1038/s41598-021-94161-0

---

# 16. Prepublication references

Bian, Y., Wang, Y., & Guo, X. (2026). *Shared hidden-factor information framework for multiple behavioral tasks*. arXiv:2605.24707.

Debele, Y., Goytom, I., & Misbah, A. (2026). *Pulse Focus: Validation of the Focus Performance Score as a behavioral signal for human attentional state modeling toward attention-aware AI*. arXiv:2606.03164.

Kucyi, A., Anderson, N., Bounyarith, T., et al. (2024). *Individual variability in neural representations of mind-wandering*. bioRxiv 2024.01.20.576471.

Mistry, P. K., Warren, S. L., Branigan, N. K., Cai, W., & Menon, V. (2024). *Computational modeling of proactive, reactive, and attentional dynamics in cognitive control*. bioRxiv 2024.10.01.615613.

Westrin, M. (2026). *Information-Theoretic Reliability is Robust to Analytic Choice: A 24-Specification Multiverse on Public Cognitive Test-Retest Data*. arXiv:2605.24995.

---

# 17. Review status

```text
review_status:
draft

production_claims_changed:
false

canonical_registry_records_promoted:
false

next_action:
translate the decisions into candidate source, claim and measurement-record revisions;
then conduct human expert review before changing review_status.
```
