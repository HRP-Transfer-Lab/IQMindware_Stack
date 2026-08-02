<!-- SPDX-License-Identifier: MIT -->

# G Track Cognitive-Vigilance Zone Assessment Protocol

Protocol version: `g-track-cognitive-vigilance-zone-v2`  
App task version: `attention-readiness-sart-stroop-flanker-v2`  
Status: production protocol specification for the G Track app; non-diagnostic.

Copyright (c) 2026 HRP Transfer Lab. This protocol specification is released
under the MIT License. It describes the behavioral protocol and score
calculation at a cognitive-science level. It does not publish the application
source code.

## Scope

This protocol describes the cognitive/vigilance Zone assessment implemented in
G Track for the Attention Control benchmark. It is a cognitive-only assessment
based on:

- Sustained Attention to Response Task (SART), for engagement-vigilance and
  response inhibition signals.
- Colour-word Stroop, for response selection under conflict.
- Eriksen arrow Flanker, for selective attention and response competition.

It does not implement the RR/HRV body-state side of Flow Zone. The output is a
provisional cognitive-control profile and an engagement-vigilance signal, not a
medical, diagnostic, selection, employment, or certification score.

## Source Alignment

The protocol is grounded in the paired Stroop/SART/Flanker validation work in
`HRP-Transfer-Lab/flow-zone-zone-validation`, which re-analysed the published
Barzykowski et al. (2022) dataset of Stroop, SART, and Eriksen Flanker
performance.

The G Track scheduled benchmark now matches the source study's core full task
structure:

| Task | Source full structure | G Track scheduled benchmark |
|---|---:|---:|
| SART | 18 practice + 225 main trials | 18 practice + 225 scored trials |
| Stroop | 14 practice + 140 main trials | 14 practice + 140 scored trials |
| Flanker | 10 practice + 140 main trials | 10 practice + 140 scored trials |

G Track also includes a shorter Zone Check for current-state readings. It is
not used as the scheduled pre/post/follow-up benchmark:

| Task | G Track Zone Check |
|---|---:|
| SART | 18 practice + 96 scored trials |
| Stroop | 14 practice + 80 scored trials |
| Flanker | 10 practice + 80 scored trials |

The validation repository documents the 96-trial SART and 80-trial
Stroop/Flanker variants as shortened source-compatible research candidates.

## Task Protocol

### SART

The participant sees digits 1-9 one at a time and responds to every digit
except `3`.

| Element | Specification |
|---|---|
| Go digits | 1, 2, 4, 5, 6, 7, 8, 9 |
| No-go digit | 3 |
| Full scored trials | 225: 200 Go, 25 NoGo |
| Zone Check scored trials | 96: 88 Go, 8 NoGo |
| Practice | 18 trials |
| Stimulus onset asynchrony | 1250 ms |
| Digit display | 250 ms, followed by fixation/mask interval |
| Response | Single press/tap/keyboard response for Go digits |
| Anticipatory threshold | RT < 150 ms |

The public validation repository does not expose a reusable raw digit-by-digit
SART source sequence because the raw source workbooks are excluded from Git.
G Track therefore uses a deterministic balanced sequence with the same Go/NoGo
composition and timing, rather than claiming exact source-sequence identity.

### Stroop

The participant selects the ink colour while ignoring the word meaning.

| Element | Specification |
|---|---|
| Colours | red, green, blue, yellow |
| Conditions | 50% congruent, 50% incongruent |
| Full scored trials | 140: 70 congruent, 70 incongruent |
| Zone Check scored trials | 80: 40 congruent, 40 incongruent |
| Practice | 14: 7 congruent, 7 incongruent |
| Stimulus duration | Response-contingent, with 3000 ms engineering timeout |
| Inter-trial interval | 400 ms |
| Error feedback | 400 ms after incorrect or missing response |
| Response mapping | Fixed colour buttons/keys within the app |

The app does not include neutral Stroop trials in this protocol.

### Flanker

The participant responds to the direction of the central arrow and ignores the
flanking arrows.

| Element | Specification |
|---|---|
| Conditions | congruent, incongruent |
| Target responses | left, right |
| Full scored trials | 140: 70 congruent, 70 incongruent |
| Zone Check scored trials | 80: 40 congruent, 40 incongruent |
| Practice | 10: 5 congruent, 5 incongruent |
| Target display | Up to 1750 ms |
| Maximum trial duration | 2700 ms |
| Blank/fixation interval | 950 ms after response/timeout |

## Raw Metrics

All scored metrics exclude practice trials.

### Conflict Tasks

For Stroop and Flanker:

```text
accuracy = correct scored trials / scored trials
valid RT = correct response with RT within task range
mean RT = mean(valid RT)
median RT = median(valid RT)
RT CV = standard deviation(valid RT) / mean(valid RT)
throughput = accuracy / (mean RT / 1000)
RT conflict cost = mean incongruent RT - mean congruent RT
accuracy conflict cost = congruent accuracy - incongruent accuracy
```

Task RT ranges:

```text
Stroop valid RT: 150-3000 ms
Flanker valid RT: 150-1750 ms
```

### SART

For SART:

```text
Go trials = scored trials where digit != 3
NoGo trials = scored trials where digit == 3
omission rate = Go trials with no response / Go trials
commission rate = NoGo trials with response / NoGo trials
anticipatory response rate = Go responses with RT < 150 ms / Go trials
valid Go RT CV = standard deviation(valid Go RT >= 150 ms) / mean(valid Go RT >= 150 ms)
median Go RT = median(valid Go RT >= 150 ms)
```

## Zone Model

The task-active Zone profile is estimated from Stroop and Flanker features,
not from SART alone. G Track uses the validation-prior four-profile model
developed from the paired Stroop/Flanker/SART dataset.

Input features:

```text
stroop_accuracy
stroop_mean_rt
stroop_median_rt
stroop_rt_cv
stroop_throughput
stroop_congruent_accuracy
stroop_congruent_rt
stroop_incongruent_accuracy
stroop_incongruent_rt
stroop_cost_rt
stroop_cost_accuracy
flanker_accuracy
flanker_mean_rt
flanker_median_rt
flanker_rt_cv
flanker_throughput
flanker_congruent_accuracy
flanker_congruent_rt
flanker_incongruent_accuracy
flanker_incongruent_rt
flanker_cost_rt
flanker_cost_accuracy
```

Features are median-imputed where needed, robust-scaled using the frozen
validation-prior centers/scales, and passed to the four-class model. The
display labels are:

| Model component | Display label | Behavioral interpretation |
|---|---|---|
| C1 | Slow compensatory | Slower control with relatively preserved accuracy |
| C2 | Regulated | Best balance of speed, accuracy, and conflict cost |
| C3 | Globally overloaded | Broad speed and accuracy strain |
| C4 | Fast brittle | Fast responding with weaker accuracy under conflict |

Quality rules:

```text
Abstain if Stroop or Flanker has fewer than 80 scored trials.
Abstain if Stroop has fewer than 60 valid RT trials.
Abstain if Flanker has fewer than 60 valid RT trials.
Flag high nonresponse if Stroop or Flanker omission rate exceeds 20%.
Classify when the top profile probability is >= 0.60.
Return low-confidence profile information below that probability.
```

The four profiles are statistical task-active control profiles. They should not
be treated as fixed natural kinds.

## Engagement-Vigilance

SART adds a separate engagement-vigilance signal. It is not duplicated in the
task-active profile probability model.

The validation study defined:

```text
engagement-vigilance = mean(-robust_z(omission rate), -robust_z(Go RT CV))
inhibitory stability = mean(-robust_z(commission rate), -robust_z(anticipatory response rate))
```

with median/IQR standardization and a low-engagement threshold of:

```text
sart_engagement_index <= -0.5
```

G Track v2 preserves the same indicator orientation, but the public validation
outputs do not include frozen SART median/IQR constants. The production app
therefore uses a fixed-risk transform until those constants are published:

```text
engagement risks:
  omission reference = 0.12
  Go RT CV reference = 0.35

inhibitory risks:
  commission reference = 0.35
  anticipatory response reference = 0.03

risk ratio = observed value / reference
clipped risk = clamp(risk ratio, 0, 2)
index = 0.5 - mean(clipped risks)
display score = clamp(round(50 + 50 * index), 0, 100)
```

This means the task structure is source-compatible, but the SART index is a
transparent production approximation rather than an exact reproduction of the
validation-study robust score. The profile probabilities remain Stroop/Flanker
validation-prior outputs.

## Public Attention Control Score

The app displays an estimated standardized Attention Control score on a 100/15
scale where available. The score is a non-diagnostic validation-prior score:
100 is the validation-prior reference mean, 15 points is one reference standard
deviation, and higher values indicate better task performance in the scored
direction.

Component scores:

```text
Conflict control:
  average lower-better robust z values for Stroop/Flanker RT conflict cost
  and accuracy conflict cost.
  App field: publicScores.conflictControl.
  User label: Conflict control.

Sustained attention:
  SART engagement-vigilance index, oriented higher = steadier engagement.
  App field: publicScores.sustainedStability.
  User label: Sustained attention.

Response efficiency:
  average higher-better robust z values for Stroop/Flanker throughput.
  App field: publicScores.responseEfficiency.
  User label: Response efficiency.

Attention Control composite:
  average of available component z scores, transformed to 100 + 15*z.
  App field: publicScores.composite.
  User label: Attention Control Score.
```

Scores are clipped to the app's public display range and should be interpreted
as coaching signals, not IQ scores or clinical scores.

If `publicScores.composite` is available, it is the primary score displayed on
the G Track result screen, the G Track training graph, and the Attention Coach
Proof graph. For compatibility with older result rows, app displays may fall
back to the mean of the three available component standard scores. If no usable
standardized attention score exists, the result screen shows `Score saved` and
metric cards show `-`; it does not display `Collecting` or raw model
probabilities.

The same composite is also stored in the portable G Track proof score as
`provisionalIndex`. This is a compatibility field for history/proof views and
is not a separate psychological construct.

## App Display and Proof Sync Contract

The public user-facing Attention Control result screen contains:

```text
Attention Control Score:
  publicScores.composite.displayStandardScore or publicScores.composite.standardScore.

Conflict control card:
  publicScores.conflictControl.displayStandardScore or standardScore.

Sustained attention card:
  publicScores.sustainedStability.displayStandardScore or standardScore.

Response efficiency card:
  publicScores.responseEfficiency.displayStandardScore or standardScore.

Cognitive Zone panel:
  publicScores.zoneProtocol.profile when available.
  Engagement-vigilance is shown once as a compact secondary line.
```

The G Track My Results graph uses the same value order for Attention Control:

```text
1. publicScores.composite standard score
2. mean of conflictControl, sustainedStability, and responseEfficiency standard scores
3. provisionalIndex
```

The signed G Track proof summary used by Attention Coach exports scheduled
G Track proof scores for the same signed-in email account. For
`attention_control`, Attention Coach uses the same precedence order:

```text
1. publicScores.composite
2. mean(publicScores.conflictControl,
        publicScores.sustainedStability,
        publicScores.responseEfficiency)
3. provisionalIndex
```

Thus the pre-training Attention Control benchmark should populate both the G
Track My Results Attention graph and the Attention Coach Proof Attention graph
when cloud sync is enabled for the same email account.

Zone Check readings are current-state readings. They may remain in account
export data when present, but they are excluded from baseline/change
calculation and from the scheduled pre/post/follow-up proof graph.

## Confidence

User-facing confidence is based on recent score stability and data sufficiency:

```text
High:
  at least four recent attention readings,
  current standardized score exists,
  server confidence is not insufficient/unstable,
  recent composite SD <= 9 standard-score points.

Medium:
  at least two usable recent readings,
  or server confidence is moderate_confidence.

Low:
  fewer than two usable readings,
  missing current standardized score,
  insufficient_data,
  or unstable_estimate.
```

Confidence text must always be shown with the label, not color alone.

## Baseline Change

For G Track scheduled pre/post/follow-up tests, change from baseline is
computed from the first valid full Attention Control benchmark completion for
that metric. Zone Check readings are excluded from baseline computation because
they are shorter current-state checks.

```text
baseline value = first valid full benchmark metric score
delta = current standardized metric score - baseline value
display = +N, -N, or 0 standard-score points
```

If no valid baseline exists for a metric, the app leaves the delta blank or
shows `-`.

## Interpretation Boundary

Use these outputs for coaching and self-monitoring only. Do not use them for:

- diagnosis;
- treatment decisions;
- employment, school, or selection decisions;
- certificates, rankings, or claims of general intelligence;
- claims that the user is in a direct neural, autonomic, or physiological
  "brain state."

The safest interpretation is: a short, browser-based cognitive-control and
vigilance sample that estimates provisional task-active control profiles and
engagement-vigilance tendencies.

## Source References

- HRP Transfer Lab. `flow-zone-zone-validation`, commit
  `2d8d479befd73155d2215c1fef80a60cd27eaa5b`.
  https://github.com/HRP-Transfer-Lab/flow-zone-zone-validation
- HRP Transfer Lab. `Flow-Zone`, commit
  `8a1d52ba991a62908b461e2f5e22dc4cec846fc2`.
  https://github.com/HRP-Transfer-Lab/Flow-Zone
- Paired control-vigilance task specifications:
  https://github.com/HRP-Transfer-Lab/flow-zone-zone-validation/tree/main/studies/paired-control-vigilance
- Barzykowski, K., Wereszczynski, M., Hajdas, S., & Radel, R. (2022).
  Cognitive inhibition behavioral tasks in online and laboratory settings:
  Data from Stroop, SART and Eriksen Flanker tasks. Data in Brief, 43,
  108398. https://doi.org/10.1016/j.dib.2022.108398
- Open-access article page:
  https://pmc.ncbi.nlm.nih.gov/articles/PMC9249604/
- OSF source record:
  https://osf.io/2gxhy/?view_only=31aa5d5964a943df8d3e7d911d2d7141

