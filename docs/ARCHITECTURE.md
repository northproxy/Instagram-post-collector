# Architecture

## Status

This document describes the planned MVP architecture and clearly separates it from the parts already implemented and validated.

### Implemented and Validated

As of 2026-08-12:

- the Python project uses a project-local `.venv`;
- dependencies and pytest configuration are defined in `pyproject.toml`;
- Instaloader `4.15.3` has been validated locally against a public Instagram image carousel;
- the proof-of-concept post contained nine images and its caption and raw metadata were retrieved successfully;
- `src/naming.py` implements deterministic caption prefixes, metadata filenames, media filenames, monthly archive directories, and complete relative archive paths;
- `tests/test_naming.py` validates the naming behavior with 15 passing tests.

### Planned but Not Yet Implemented

- Telegram intake;
- GitHub Actions batch processing;
- FTP persistence;
- persistent workflow state;
- normalized post metadata model;
- image conversion pipeline;
- static catalog generation;
- Telegram completion reporting;
- hosting-level access protection.

## Overview

IPcoll uses a scheduled batch architecture because no always-on home server is currently available.

```text
┌──────────────────────┐
│ Instagram mobile app │
└──────────┬───────────┘
           │ share public post URL
           ▼
┌──────────────────────┐
│ Telegram Bot API     │
│ temporary updates    │
└──────────┬───────────┘
           │ getUpdates
           ▼
┌──────────────────────────────────────┐
│ GitHub Actions runner                │
│                                      │
│  Python batch application            │
│  - authorization                     │
│  - URL validation                    │
│  - duplicate detection               │
│  - Instagram extraction              │
│  - image processing                  │
│  - normalized metadata generation    │
│  - FTP synchronization               │
│  - Telegram reporting                │
└──────────┬───────────────────────────┘
           │ FTP / preferred secure alternative
           ▼
┌──────────────────────────────────────┐
│ FTP server and web hosting           │
│                                      │
│  archive/                            │
│  state/                              │
│  public/                             │
│  protected static catalog            │
└──────────┬───────────────────────────┘
           │ HTTP/HTTPS according to    │
           │ hosting capabilities       │
           ▼
┌──────────────────────┐
│ Mobile/desktop web   │
│ browser              │
└──────────────────────┘
```

## Component Responsibilities

### Telegram

Planned responsibilities:

- provide the mobile collection interface;
- receive plain Instagram URLs;
- temporarily store pending updates;
- receive batch completion reports;
- not act as durable project state.

### GitHub Repository

Stores:

- source code;
- tests;
- workflows;
- frontend source;
- project documentation;
- sample fixtures without copyrighted media;
- release history.

Does not store:

- Instagram media;
- Telegram tokens;
- FTP credentials;
- Instagram sessions;
- Basic Auth passwords;
- production state files.

### GitHub Actions

Planned responsibilities:

- run scheduled and manual jobs;
- install project dependencies;
- retrieve pending Telegram updates;
- download and transform supported content;
- synchronize files to FTP;
- send processing reports;
- upload sanitized diagnostic artifacts when useful.

### Python Application

Currently implemented:

- `naming.py` — deterministic archive naming and relative path generation.

Likely future modules should be introduced only when their responsibilities become necessary. Current planned areas include:

- configuration;
- Telegram client;
- URL parsing;
- Instagram adapter;
- media processing;
- metadata normalization;
- state persistence;
- FTP transport;
- catalog building;
- reporting;
- application entry point.

The final module boundaries should follow actual implementation needs rather than a fixed speculative file list.

### FTP Server

Planned responsibilities:

- permanent media archive;
- persistent workflow state;
- frontend hosting;
- recovery source for repeated workflow runs.

### Static Frontend

Planned responsibilities:

- read generated catalog data;
- avoid direct Instagram or Telegram calls;
- provide catalog browsing, filtering, post detail, and image download;
- use hosting-level access protection where supported.

## Data Zones

Planned server layout:

```text
server-root/
├── archive/      # archived post media and normalized metadata
├── state/        # workflow state; must not be web-accessible
├── public/       # frontend and generated public catalog data
└── backup/       # optional previous state and index versions
```

The `state` directory must not be published through the web server.

The archive itself uses the accepted monthly structure documented in `DECISIONS.md`.

## Processing Boundary

The intended processing boundary is:

1. media download succeeds;
2. required normalized metadata is generated;
3. all required post files are persisted;
4. catalog state is updated successfully;
5. processed-state entry is durably written.

Only then should the related Telegram update be considered successfully processed.

This behavior is planned and has not yet been validated end to end.

## Failure Isolation

Each URL should be processed independently so that one failure does not stop other posts.

Planned failure categories include:

- invalid input;
- unsupported content;
- unauthorized sender;
- duplicate;
- Instagram access failure;
- media processing failure;
- FTP failure;
- catalog generation failure;
- Telegram reporting failure.

The exact error model will be defined during core pipeline implementation.

## Scheduling

The desired schedule is 06:19 Europe/Vienna.

GitHub cron uses UTC and scheduled runs can be delayed. The planned design is:

- run at both relevant UTC equivalents where needed for daylight-saving changes;
- check `Europe/Vienna` inside Python;
- process only during the intended local-time window;
- provide a manual trigger;
- prevent duplicate concurrent processing.

This scheduling design has not yet been implemented or validated.

## Future Migration

The architecture should keep domain logic separate from infrastructure so that a later version can replace:

- GitHub Actions with a home-server scheduler;
- FTP with local or object storage;
- JSON state with SQLite or PostgreSQL;
- the static frontend with another frontend architecture;
- batch Telegram polling with a webhook or continuously running bot.
