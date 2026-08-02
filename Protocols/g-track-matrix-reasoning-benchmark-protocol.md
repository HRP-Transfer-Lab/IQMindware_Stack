# G Track Matrix Reasoning / Matrices IQ Test Protocol

License: MIT

Version: v1.0

Status: Public high-level protocol specification

## Purpose

The G Track Matrix Reasoning benchmark is a non-diagnostic fluid-reasoning
assessment used in the G Track pre/post/follow-up battery. It is the matrices
IQ-test component of G Track: a short, browser-based figural matrices test that
estimates nonverbal abstract reasoning from matrix-completion items selected
from the Open Matrices Item Bank (OMIB).

The public construct label is:

```text
Matrix Reasoning
```

The app score object uses:

```text
construct = matrix_reasoning
```

The benchmark is for coaching and longitudinal self-monitoring. It is not a
clinical instrument, a certificate, a selection test, or a full-scale IQ test.

## Source Study

The item source is the Open Matrices Item Bank:

- Koch, M., Spinath, F. M., Greiff, S., & Becker, N. (2022). Development and
  Validation of the Open Matrices Item Bank. Journal of Intelligence, 10(3),
  Article 41. https://doi.org/10.3390/jintelligence10030041
- Source materials: https://osf.io/4km79/

The OMIB study developed 220 figural matrix items and administered the source
test sets to German medical-school applicants. The article reports 2,572
applicants in the administered sample and a final analytic sample of 2,561
participants after exclusions. G Track uses the final analytic sample size for
the source-prior metadata:

```text
calibrationN = 2561
```

In the OMIB source study, each participant solved two practice items and 28
scored figural matrix tasks without an item-level time limit. The item bank was
evaluated with classical test theory, IRT item-response modelling, and
reliability analyses. The source paper reports high internal consistency for
the test sets and two-parameter logistic item parameters for the item bank.
G Track uses selected OMIB items and their source-study item parameters.

## Current App Implementation

The current G Track implementation uses the OMIB source-study theta scale as
the prior standardization frame:

```text
modelId = omib_matrix_2pl_eap
modelVersion = v2
calibrationLabel = omib_2pl_theta_source_prior_koch_2022
```

This replaced an earlier 33-person IQMindware launch calibration:

```text
old calibrationLabel = brevo_calibration_2026_wave1_pooled
old calibrationN = 33
```

The replacement was made because the OMIB source-study calibration is the
stronger prior estimate for standardized scoring. IQMindware baseline data can
still be used later for app-specific recalibration, but the public Matrix Index
is no longer based on the small launch sample.

## Forms

The programme forms are:

```text
matrix-a
matrix-b
matrix-c
```

They are used for:

```text
baseline / pre-training
post-training
follow-up
```

The hook form is:

```text
matrix-d
```

The hook form is scored but is kept separate from scheduled programme
pre/post/follow-up interpretation.

Each G Track form contains 16 matrix items. Forms are balanced across rule
complexity so each form samples easier and harder items from the OMIB source
bank.

## User Task

Each item displays a matrix with the final cell missing. The user constructs
the missing cell by selecting from a fixed bank of construction elements.

The submitted answer is a binary vector:

```text
1 = selected element
0 = unselected element
```

An item is correct only when the submitted vector exactly matches the protected
answer vector.

## Raw Score

The raw score is:

```text
raw = number of exactly correct items
maxRaw = 16
```

Raw score is shown for transparency, but the standardized Matrix Index is based
on the item-response model rather than raw percent correct.

## IRT / EAP Scoring

The server estimates ability with a two-parameter logistic item-response model:

```text
P(correct | theta) = logistic(discrimination * (theta - difficulty))
```

For each submitted response pattern, the app computes an expected-a-posteriori
estimate:

```text
theta = posterior mean ability estimate
standardError = posterior SD
```

The EAP grid is:

```text
minimum theta = -4
maximum theta = 4
step = 0.05
prior density = standard normal
```

## Matrix Index

The public standardized score is:

```text
Matrix Index = 100 + 15*z
```

For the current source-prior model:

```text
z = (theta - 0) / 1
Matrix Index = 100 + 15*theta
```

Current app model metadata:

```text
modelId = omib_matrix_2pl_eap
modelVersion = v2
calibrationLabel = omib_2pl_theta_source_prior_koch_2022
calibrationMean = 0
calibrationSd = 1
calibrationN = 2561
```

The calibration frame is the OMIB source-study theta scale. This is stronger
than the earlier IQMindware 33-person launch sample prior, but it is still not
a representative general-population IQ norm because the OMIB source sample was
German medical-school applicants.

The app can display an uncertainty band by applying the same transformation to:

```text
theta - standardError
theta + standardError
```

## My Results and Proof Sync Contract

The G Track My Results graph uses:

```text
provisionalIndex = Matrix Index
```

The signed proof summary exports the same scheduled G Track score for the same
signed-in email account:

```text
construct = matrix_reasoning
testId = matrix-a, matrix-b, or matrix-c
timepoint = baseline, post, or follow_up
raw
maxRaw
theta
standardError
provisionalIndex
provisionalIndexLow
provisionalIndexHigh
calibrationLabel
```

Downstream coaching apps should treat `provisionalIndex` as the Matrix Index
for graphing and proof displays.

## Recalibration Policy

The current Matrix Index is an OMIB source-study-prior estimate. This is the
best current prior in the app because it comes from the original item-bank
validation publication rather than from a small internal launch sample.

IQMindware may replace or supplement it with G Track baseline recalibration
once enough valid baseline completions have accumulated to estimate:

- form effects;
- sample composition;
- retest and practice effects;
- device/browser effects;
- uncertainty around individual change.

Only valid baseline/pre-training attempts should be used for norm-building.
Post-training and follow-up attempts are saved for personal change evidence
but should not be mixed into baseline norm estimates.

## Interpretation Boundary

Use the Matrix Index for coaching and repeated self-monitoring only. Do not use
it for:

- diagnosis;
- treatment decisions;
- employment, school, or selection decisions;
- certificates, rankings, or claims of full-scale IQ;
- claims that a 16-item browser task is equivalent to a complete intelligence
  battery.

The safest interpretation is: a short OMIB-based fluid-reasoning benchmark,
standardized against the OMIB source-study theta scale and intended for
longitudinal coaching context.

## Source References

- Koch, M., Spinath, F. M., Greiff, S., & Becker, N. (2022). Development and
  Validation of the Open Matrices Item Bank. Journal of Intelligence, 10(3),
  41. https://doi.org/10.3390/jintelligence10030041
- ERIC record for the OMIB article:
  https://eric.ed.gov/?id=EJ1354162
- OMIB source materials:
  https://osf.io/4km79/
