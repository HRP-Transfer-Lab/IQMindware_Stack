# Attention Coach MFT-M Horizontal Transfer Protocol

License: MIT

Version: v1.0

Status: Public high-level protocol specification

## Purpose

Attention Coach is a non-diagnostic cognitive training protocol built around
the backward Masking Majority Function Task, usually abbreviated as MFT-M or
MFT-m. The classic MFT-M asks a user to decide the majority direction of a
briefly exposed arrow array after backward masking. The task is used as a
behavioural route to estimate cognitive-control throughput under uncertainty.

Attention Coach uses this task family as the baseline training format and then
adds a progressive horizontal-transfer route. The app changes the surface
carrier and the reference computation while preserving the core requirement:
identify the majority relation under brief exposure, conflict, and masking.

The public app goal is coaching and longitudinal self-monitoring. It is not a
clinical instrument, a certificate, a selection test, or a full IQ test.

The current implementation identifier is:

```text
protocolVersion = attention-horizontal-v2
```

## Scientific Basis

The original MFT-M paradigm was introduced by Wu, Dufford, Mackie, Egan, and
Fan (2016) to estimate the capacity of cognitive control. The study manipulated
stimulus uncertainty and exposure time, then fitted accuracy as a function of
information-processing demand in bits per second.

The classic laboratory protocol:

- presents arrow arrays around fixation;
- asks for the majority arrow direction;
- varies majority/minority structure and exposure time;
- applies a backward mask after the stimulus;
- estimates capacity of cognitive control from accuracy across demand levels.

The original paper reported cognitive-control capacity in the approximate
range of 3 to 4 bits per second in healthy young adults. Later work evaluated
adaptive and abbreviated MFT-M administration and showed that shorter adaptive
forms can retain useful correspondence with the longer laboratory form.
Recent training work has also used MFT-M as an attention-control training task
and examined transfer to other executive-function outcomes.

Key references:

- Wu, T., Dufford, A. J., Mackie, M. A., Egan, L. J., & Fan, J. (2016). The
  Capacity of Cognitive Control Estimated from a Perceptual Decision Making
  Task. Scientific Reports, 6, 34025. https://doi.org/10.1038/srep34025
- He, X., Qiu, B., Deng, Y., Liu, T., Chen, Y., & Zhang, W. (2021). Adaptive
  assessment of the capacity of cognitive control. Quarterly Journal of
  Experimental Psychology, 75(1), 43-52.
  https://doi.org/10.1177/17470218211030838
- Chen, Y., Spagna, A., Wu, T., Kim, T. H., Wu, Q., Chen, C., Wu, Y., & Fan,
  J. (2019). Testing a Cognitive Control Model of Human Intelligence.
  Scientific Reports, 9, 2898. https://doi.org/10.1038/s41598-019-39685-2
- Zhang, H., Fan, S., Yang, J., Yi, J., Guan, L., He, H., Zhang, X., Luo, Y.,
  & Guan, Q. (2024). Attention control training and transfer effects on
  cognitive tasks. Neuropsychologia, 200, 108910.
  https://doi.org/10.1016/j.neuropsychologia.2024.108910

## Classic MFT-M Form

In its classic form, MFT-M is a backward-masked majority-direction judgement.
On each trial, a set of arrows is briefly displayed around fixation. Most
arrows point in one direction and the remainder, when present, point in the
opposite direction. The user reports the majority direction as accurately and
quickly as possible.

The original laboratory task varies the information rate by changing both the
amount of direction information and the exposure duration. Published laboratory
forms include arrays with different set sizes, majority/minority ratios, and
exposures such as 250 ms, 500 ms, 1000 ms, and 2000 ms. The response is then
modelled against demand in bits per second to estimate cognitive-control
capacity.

The cognitive interpretation is not that the task measures visual acuity alone.
The task requires the user to maintain a goal, sample multiple briefly exposed
items, resolve majority/minority conflict, tolerate uncertainty, and respond
under time pressure.

## Attention Coach Baseline Adaptation

Attention Coach uses a browser-based MFT-M training adaptation rather than the
full laboratory assessment. The baseline task preserves the central MFT-M logic
but constrains the display so the same structure can be carried into transfer
variants.

Current baseline implementation:

```text
wrapperId = arrow_abs
carrier = arrow
referenceComputation = fixed_axis
responseAxis = LEFT / RIGHT
construct = ACC
```

Each Attention Coach MFT-M trial contains:

- five stimulus tokens;
- positions sampled from eight octagonal locations around the display centre;
- a majority relation count of 5, 4, or 3 out of 5;
- a corresponding ratio of `5:0`, `4:1`, or `3:2`;
- a brief exposure selected from the adaptive exposure grid;
- a backward mask;
- a two-choice response for the primary attention-control construct.

The current exposure grid is:

```text
100 ms
150 ms
200 ms
300 ms
400 ms
500 ms
700 ms
1000 ms
1500 ms
```

The default starting staircase level is the `4:1` ratio at `500 ms`. Correct
responses move the next level harder; incorrect responses move the next level
easier. The levels combine ratio and exposure time, so both uncertainty and
time pressure contribute to demand.

The app uses five tokens throughout the training route. This differs from the
full original MFT-M set-size grid, but it is deliberate: horizontal transfer is
cleaner when the number of tokens, mask structure, and response budget remain
fixed while the carrier and reference computation change.

## Primary And Companion Constructs

Attention Coach stores two task constructs:

```text
ACC = Attention Control Practice
BSE = Binding Focus Practice
```

`ACC` is the primary MFT-M-style attention-control construct. It asks for the
majority direction or relation. `ACC` drives the horizontal-transfer
progression controller.

`BSE` is a companion binding probe. It adds token colour and asks for the
majority relation-colour pair. For example, fixed-axis BSE response options
are:

```text
left_blue
left_yellow
right_blue
right_yellow
```

`BSE` is collected every guided session, but it does not block wrapper swaps or
portable-status decisions. It is used as a coaching signal for relation-colour
binding under the current training format.

## Session Structure

Each guided Attention Coach session contains:

```text
80 trials total
4 mini-blocks
20 trials per mini-block
60 ACC trials
20 BSE trials
```

The target training envelope is:

```text
20 guided sessions
```

This is an envelope, not an automatic progression clock. Session number alone
does not advance the protocol. If readiness evidence is incomplete, timing is
poor, or recovery has not stabilised, the app continues collecting evidence in
the current route state.

## Progressive Wrapper Variations

The protocol uses four atomic wrapper IDs. These IDs are preserved for data
compatibility and are the main public protocol cells.

| Wrapper | Carrier | Reference computation | Response axis |
| --- | --- | --- | --- |
| `arrow_abs` | Static arrows | Fixed horizontal axis | LEFT / RIGHT |
| `flow_abs` | Local optic-flow patches | Fixed horizontal axis | LEFT / RIGHT |
| `arrow_rel` | Static arrows | Common-centre radial relation | IN / OUT |
| `flow_rel` | Local optic-flow patches | Common-centre radial relation | IN / OUT |

`arrow_abs` is the classic baseline training form: users classify the majority
left/right direction of arrows. The classification is independent of where an
arrow appears on the screen.

`flow_abs` preserves the left/right response rule but changes the visual
carrier from static arrows to local motion patches. Each aperture contains
sparse moving dots. Dots translate leftward or rightward according to the
trial relation.

`arrow_rel` preserves the arrow carrier but changes the reference computation.
The user now classifies whether arrows point inward or outward relative to the
shared display centre.

`flow_rel` combines both changes: local optic-flow patches and common-centre
in/out classification. In the arrows-first commercial route, this is the
protected held-out recombination.

The four-wrapper route does not generate clockwise, anticlockwise, spiral,
displaced-centre, response-remapping, evidence-accumulation, or working-memory
variants. Those are outside the current Attention Coach horizontal-transfer
protocol.

## Rule Cues

When a block can switch between fixed-axis and common-centre response rules,
the app shows a brief pre-stimulus rule cue:

```text
LEFT / RIGHT
IN / OUT
```

The cue tells the user which response axis applies to the next trial. Cue time
precedes fixation and is not counted as stimulus exposure time. It is also
excluded from capacity and trial-demand calculations.

No rule cue is added to fixed-axis carrier-only mixing, such as
`arrow_abs / flow_abs`, because both wrappers use the same LEFT / RIGHT
response axis.

## Horizontal Transfer Route

The default commercial route is arrows-first:

```text
arrow_abs baseline
-> diagnostic flow_abs probe
-> formal 20% flow_abs transition probe
-> flow_abs recovery
-> return to arrow_abs
-> progressive arrow_abs / flow_abs mixing
-> arrow_rel probe and recovery
-> return to arrow_abs
-> progressive arrow_abs / arrow_rel mixing
-> protected flow_rel probe
-> flow_rel recovery
-> all-four-wrapper mixing
-> delayed all-four-wrapper re-check
```

A validation route can use a flow-first counterbalanced order:

```text
flow_abs baseline
-> arrow_abs carrier transfer
-> flow_rel reference transfer
-> arrow_rel held-out recombination
-> all-four-wrapper mixing
-> delayed all-four-wrapper re-check
```

The route is designed to distinguish narrow task practice from more portable
control. A surface carrier change tests whether the same majority function can
survive a change from arrows to motion. A reference-computation change tests
whether the user can preserve the majority function when the relevant
direction is no longer fixed left/right, but must be computed relative to the
common centre. The held-out recombination tests whether these changes compose
without direct prior practice on the exact combined format.

## Evidence Gates

The route advances only when evidence from valid `ACC` trials meets the
configured stability gates.

Baseline fluency requires:

```text
valid ACC trials >= 240
rolling windows >= 4
absolute recent capacity slope < 0.02
balanced accuracy >= 0.70
lapse rate <= 0.18
timing quality is not poor
```

After at least 80 valid baseline trials, the app may insert a small diagnostic
probe at approximately 5% target-wrapper exposure. This is a diagnostic check,
not a formal transition.

The formal transition probe introduces the target wrapper at approximately
20% exposure. A temporary dip is expected and is not treated as failure by
itself.

Recovery and readiness to mix require:

```text
target valid ACC trials >= 40
target rolling windows >= 2
target/source capacity ratio >= 0.80
balanced accuracy >= 0.70
lapse rate <= 0.20
timing quality is not poor
```

Recovery can start earlier when either:

```text
target/source capacity ratio >= 0.70
```

or the target has at least one valid rolling window, a positive recent slope,
and at least 12 valid target trials.

Return-to-base readiness requires:

```text
valid return ACC trials >= 12
balanced accuracy >= 0.70
lapse rate <= 0.20
timing quality is not poor
```

Mixed stability requires all active wrappers in the mix to be represented,
each represented wrapper to have at least 12 valid ACC trials, acceptable
accuracy and lapse values, and observed mixed-wrapper performance to reach at
least 80% of the weighted expected blocked capacity.

Accuracy above 82% does not block progression. The relevant accuracy gate is a
minimum-quality floor, not an upper target band.

## Probe And Evidence Rules

Diagnostic target-wrapper trials are logged but excluded from the target
wrapper's recovery and progression evidence. Valid base-wrapper trials from
the same diagnostic block remain usable evidence.

Formal transition probes, recovery trials, return trials, mix trials, and
delayed-recheck trials are stored with their evidence purpose. Mixed trials
store the actual atomic wrapper used on the trial, such as `arrow_rel` or
`flow_abs`; `mixed` is a block-level compatibility label rather than an
atomic wrapper.

## Held-Out Protection

In the arrows-first route, `flow_rel` is held out until the protected
composition probe. Before that probe, free-play options capable of generating
`flow_rel` are unavailable while the held-out status is clean.

If the held-out condition is exposed early, the app marks the held-out route
as contaminated or rebaseline-needed rather than treating later performance as
a clean compositional-transfer test.

## Delayed Re-Check And Portable Status

After all-four-wrapper mixing passes, the app schedules a delayed all-four
re-check. Portable status is not assigned merely because the user reaches or
completes a delayed session.

The delayed decision uses fresh delayed-recheck evidence only. The required
fresh evidence must:

- come from the current delayed-recheck session;
- belong to the same programme run and cycle;
- have block purpose `delayed_recheck`;
- have trial evidence purpose `delayed_recheck`;
- include all four atomic wrappers;
- include at least 12 valid ACC trials per wrapper;
- pass the existing all-four mixed-stability and timing-quality checks.

If fresh delayed evidence is missing, the state remains delayed or
maintenance-pending. If fresh delayed evidence is adequate but fails the
stability or timing checks, the route moves to maintenance mixing rather than
portable status.

## Scoring

The training score is based on estimated processing capacity in bits per
second. For each valid trial, demand is calculated from the task information
and the measured stimulus exposure time. Trials with poor browser timing are
excluded from capacity estimation.

For `ACC`, the implemented information values are:

| Ratio | Majority count | Information value |
| --- | ---: | ---: |
| `5:0` | 5 of 5 | 1.58 bits |
| `4:1` | 4 of 5 | 2.91 bits |
| `3:2` | 3 of 5 | 4.91 bits |

The trial demand is:

```text
demand bps = information value / exposure seconds
```

For `BSE`, the information value is based on the number of response options:

```text
information bits = log2(response option count)
```

The capacity model fits correctness as a function of demand, chance level,
and lapse rate. It estimates the capacity level associated with approximately
75% performance after chance and lapse adjustment.

The public training-score transform is:

```text
training score = round(85 + 5 * capacity_bps)
```

This is a coaching score, not an IQ score. When the app is in standardised
sync mode, any population-standardised scores shown in the proof area remain
separate from local Attention Coach training scores.

## Progress Metrics

The progress screen derives six longitudinal coaching metrics from current
evidence and session snapshots.

| Metric | Source |
| --- | --- |
| `cognitiveBandwidth` | `ACC` capacity from the active absolute/fixed-axis wrapper set |
| `frameBandwidth` | `ACC` capacity from the relational/common-centre wrapper set |
| `patternBinding` | `BSE` capacity from the active or best available wrapper evidence |
| `transfer` | Average of available transfer components |
| `wrapperRecovery` | Average of motion and relation recovery components |
| `delayedRecovery` | Delayed return-strength component |

The transfer component labels shown in the app are:

```text
Motion Recovery
Relation Recovery
Mixed Flexibility
Return Strength
```

`Motion Recovery` reflects recovery after carrier transfer. `Relation
Recovery` reflects recovery after the reference-computation change. `Mixed
Flexibility` reflects stable performance when wrappers switch. `Return
Strength` reflects delayed all-four stability.

## Data And Logging Contract

Each submitted trial stores the fields needed to audit the protocol without
exposing application code. The logged fields include:

- programme run and cycle;
- session and mini-block identifiers;
- protocol group and protocol version;
- construct (`ACC` or `BSE`);
- phase and phase status;
- cell key and atomic wrapper ID;
- carrier and reference frame;
- probe status and evidence purpose;
- transition key and transfer event ID;
- mix ratio when relevant;
- majority ratio, requested exposure, actual exposure, and frame count;
- response, correctness, response time, and timing quality;
- held-out route metadata.

This allows exports and coaching review to distinguish ordinary practice,
diagnostic probes, formal probes, recovery, return-to-base, mixed practice,
held-out exposure, and delayed re-check evidence.

## Implementation Consistency

This public protocol was checked against the current Attention Coach app
implementation in:

```text
src/wrapperDefinitions.ts
src/protocol.ts
src/transferController.ts
src/generator.ts
src/scoring.ts
src/progressMetrics.ts
src/ruleCue.ts
src/trialTiming.ts
src/delayedEvidence.ts
src/opticFlow.ts
```

It was also checked against the app's local implementation note:

```text
docs/horizontal-transfer-protocol.md
```

and the current protocol tests covering wrapper definitions, session
generation, rule cues, scoring, progression gates, optic-flow generation, and
delayed evidence.

## Non-Diagnostic Boundary

Attention Coach scores are personal training and coaching signals. They should
not be used as clinical diagnoses, certificates, hiring or selection evidence,
or claims of general intelligence. The protocol is intended to make a
training route auditable: what task was run, what changed, what evidence was
required before progression, and what scores mean in the app.
