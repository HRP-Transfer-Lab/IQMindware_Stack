# Versioning and Release Policy

## Semantic versioning

The ontology uses semantic versions:

```text
MAJOR.MINOR.PATCH
```

- **MAJOR:** breaking changes to identifiers, schemas or interpretation.
- **MINOR:** new niches, workflows, stages, mappings or outcome families that preserve existing contracts.
- **PATCH:** corrections, wording changes, metadata or evidence updates that do not alter routing semantics materially.

## Immutable production releases

A tagged release is immutable once imported by a production system.

Research edits may continue on branches or `main`, but production systems must import only a tagged release with a validated manifest.

## Required release manifest

Each release must record:

```text
ontology_version
source_commit
created_at
schemas
included_files
record_counts
validation_status
evidence_review_cutoff
approved_by
known_limitations
```

## Production import

The IQ Mindware website should copy the approved release bundle into its own contract directory and retain a lock file containing:

```text
source_repository
release
source_commit
manifest_sha256
imported_at
approved_for_production
```

The website must not fetch the latest branch at runtime.

## Record-level version fields

Every canonical record should include:

```text
record_version
ontology_version
review_status
created_at
updated_at
reviewed_by
source_ids
```

## Deprecation

Records are retired rather than silently deleted when they have been used in a release.

Allowed lifecycle states:

```text
draft
expert_reviewed
approved
deprecated
retired
```

A replacement record should identify `supersedes` and `superseded_by` where relevant.

## Route reproducibility

A saved route or pilot report should retain:

```text
ontology_version
evidence_registry_version
route_engine_version
product_availability_version
copy_version
governance_profile_version
```

This allows a historical recommendation to be reproduced after the ontology changes.

## Release gates

A release fails if:

- required files do not validate against schema;
- an identifier is duplicated;
- a mapping points to a missing record;
- an approved record lacks provenance;
- a health-related record lacks a governance profile;
- a high-stakes use is marked as self-service;
- a production mapping lacks a claims boundary;
- tests for expected routes fail.
