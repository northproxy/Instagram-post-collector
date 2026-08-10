# Architecture

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
│  - image conversion                  │
│  - Markdown/JSON generation          │
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
           │ HTTP initially
           ▼
┌──────────────────────┐
│ Mobile/desktop web   │
│ browser              │
└──────────────────────┘
```

## Component Responsibilities

### Telegram

- Provides the mobile collection interface.
- Receives plain Instagram URLs.
- Temporarily stores pending updates.
- Receives the batch completion report.
- Does not provide durable project state.

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

- Runs scheduled and manual jobs.
- Installs dependencies.
- retrieves pending Telegram updates;
- downloads and transforms supported content;
- synchronizes files to FTP;
- sends processing reports;
- uploads sanitized diagnostic artifacts when useful.

### Python Application

Suggested modules:

- `config.py`
- `telegram_client.py`
- `url_parser.py`
- `instagram_client.py`
- `media_processor.py`
- `metadata_builder.py`
- `state_repository.py`
- `ftp_client.py`
- `catalog_builder.py`
- `reporter.py`
- `main.py`

### FTP Server

Acts as:

- permanent media archive;
- persistent state store;
- frontend hosting location;
- recovery source for repeated workflow runs.

### Static Frontend

- Reads generated JSON files.
- Does not call Instagram or Telegram.
- Provides a catalog, filters, detail display, and image downloads.
- Is protected by hosting-level Basic Auth.

## Data Zones

```text
server-root/
├── archive/      # original archived post packages
├── state/        # workflow state; should not be web-accessible
├── public/       # frontend and generated public catalog data
└── backup/       # optional previous state and index versions
```

The `state` directory must not be published through the web server.

## Processing Boundary

A post is considered successfully processed only after:

1. media download succeeds;
2. required metadata is generated;
3. all post files are uploaded;
4. catalog state is updated successfully;
5. processed-state entry is durably written.

Only then may the related Telegram update be acknowledged.

## Failure Isolation

Each URL is processed independently. One failure must not stop other posts.

Failure categories:

- invalid input;
- unsupported content;
- unauthorized sender;
- duplicate;
- Instagram access failure;
- media processing failure;
- FTP failure;
- catalog generation failure;
- Telegram reporting failure.

## Scheduling

The desired schedule is 06:19 Europe/Vienna. GitHub cron uses UTC and scheduled runs can be delayed. The recommended design is:

- run at both possible UTC equivalents;
- check `Europe/Vienna` inside Python;
- process only during the intended local-time window;
- include a manual trigger;
- use a lock file to prevent duplicate concurrent runs.

## Future Migration

The architecture separates domain logic from infrastructure so that a later version can replace:

- GitHub Actions with a home-server scheduler;
- FTP with local or object storage;
- JSON state with SQLite or PostgreSQL;
- static frontend with a modern framework;
- batch Telegram polling with a webhook or continuous bot.
