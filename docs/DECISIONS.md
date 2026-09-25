# Architecture and Project Decisions

This document records significant technical and architectural decisions for IPcoll.

Only decisions that materially affect project structure, maintainability, security, dependencies, storage contracts, scope, or future development should be documented here.

---

## Decision 001 — Archive storage and naming convention

### Status

Accepted

### Implementation Status

Implemented and validated for deterministic path and filename generation.

The current implementation is covered by automated tests. End-to-end persistence to FTP has not yet been implemented.

### Context

IPcoll stores archived Instagram posts together with their media and normalized metadata.

A separate directory for every post would create too many folders and make the archive inconvenient to browse manually as the collection grows.

At the same time, storing every file in one directory would eventually create a very large and difficult-to-manage file list.

The archive therefore needs a structure that remains shallow, readable, and scalable.

### Decision

Archived files are organized by publication year and month:

```text
archive/YYYY/MM/
```

All posts published within the same month are stored directly inside that monthly directory.

Example:

```text
archive/
└── 2026/
    └── 08/
        ├── 260809_Eine_neue_Woch.json
        ├── 260809_Eine_neue_Woch-01.jpg
        ├── 260809_Eine_neue_Woch-02.jpg
        └── 260809_Eine_neue_Woch-03.jpg
```

The file naming convention is:

```text
YYMMDD_<caption-prefix>.json
YYMMDD_<caption-prefix>-NN.<ext>
```

Where:

- `YYMMDD` is the Instagram post publication date;
- `<caption-prefix>` is derived from the first 14 normalized characters of the caption;
- `NN` is the media position within the post, starting from `01`;
- `<ext>` is the media file extension;
- the JSON file contains normalized metadata for the post, including the Instagram shortcode and original source URL.

The caption prefix must be deterministic and filesystem-safe.

Detailed normalization behavior belongs in implementation and automated tests rather than in this decision record.

### Rationale

This structure balances a completely flat archive with a separate directory for every post.

Using one directory per month:

- keeps the number of directories small;
- prevents a single directory from growing indefinitely;
- keeps related files easy to browse manually;
- provides natural chronological organization.

Using the publication date at the beginning of every filename provides predictable chronological sorting.

The shared caption prefix keeps files belonging to the same post visually grouped and recognizable without opening the metadata file.

Instagram-specific identifiers such as the shortcode do not need to appear in every filename because they remain stored in normalized metadata.

### Consequences

The archive remains readable without requiring the IPcoll frontend or a database.

Filename collisions are theoretically possible if multiple posts on the same date have identical caption prefixes. Collision handling will be implemented only if this becomes a practical problem.

Changing the naming convention later may require migration of already archived files.

## Decision 002 — Normalized post metadata contract

### Status

Accepted

### Implementation Status

Designed and validated against metadata retrieved from a real supported public Instagram carousel.

Normalization code and automated tests have not yet been implemented.

### Context

IPcoll needs a stable metadata format for every archived Instagram post.

Raw Instagram and Instaloader metadata contains many extractor-specific, temporary, and currently unnecessary fields. Storing that structure directly would make the permanent archive unnecessarily dependent on the current extraction implementation.

The normalized metadata therefore needs to contain only the information required by IPcoll while remaining suitable for future archive migrations and replacement of the Instagram extraction layer.

### Decision

Each archived post has one normalized JSON metadata file.

Metadata schema version 1 contains:

```text
schema_version
shortcode
source_url
published_at
author
    id
    username
post_type
caption
media[]
    position
    filename
```

Field rules:

* `schema_version` is an integer and is `1` for this contract version;
* `shortcode` is the non-empty Instagram post shortcode;
* `source_url` is the original Instagram post URL;
* `published_at` is the Instagram publication timestamp represented as an ISO 8601 datetime with timezone information;
* `author` is an object identifying the Instagram account;
* `author.id` is the stable numeric source account identifier represented as a string;
* `author.username` is the Instagram username;
* `post_type` is either `image` or `carousel` for currently supported content;
* `caption` is a string and may be empty;
* `media` is a non-empty ordered array for a supported post;
* `media[].position` starts at `1` and preserves the original media order;
* `media[].filename` contains only the archived media filename, not an absolute or archive-root path.

Example structure:

```json
{
  "schema_version": 1,
  "shortcode": "Db07NdYD_Jx",
  "source_url": "https://www.instagram.com/p/Db07NdYD_Jx/",
  "published_at": "2026-08-09T17:00:14+00:00",
  "author": {
    "id": "3320679817",
    "username": "filmarchivaustria"
  },
  "post_type": "carousel",
  "caption": "Example caption",
  "media": [
    {
      "position": 1,
      "filename": "260809_Example-01.jpg"
    },
    {
      "position": 2,
      "filename": "260809_Example-02.jpg"
    }
  ]
}
```

### Rationale

The normalized format is controlled by IPcoll rather than by Instaloader or Instagram's current internal response structure.

This provides a stable boundary between source extraction and the permanent archive.

The Instagram shortcode provides a post-level source identifier suitable for duplicate detection.

The original source URL preserves provenance.

The publication timestamp preserves the original publication time and provides the date used by the archive naming logic.

Author information is grouped into a dedicated object because the author is a meaningful domain entity for catalog filtering and possible future author-based import workflows.

Both the source account ID and username are retained. The username is human-readable, while the numeric source ID provides a more stable account identity if a username changes.

Media entries explicitly preserve carousel order and point to IPcoll-controlled archive filenames.

Temporary Instagram CDN URLs are not part of the permanent normalized metadata contract.

### Consequences

The permanent archive is not tied to Instaloader's raw metadata format.

A future Instagram extractor or replacement library can produce the same normalized contract without requiring changes to downstream archive consumers.

Future metadata changes that alter the contract may require a new `schema_version` and migration logic.

Fields should not be added to the permanent metadata contract merely because they are available in raw Instagram metadata. New fields require a demonstrated project need.

Video and Reels metadata are outside the current MVP contract because those content types are not currently supported.
