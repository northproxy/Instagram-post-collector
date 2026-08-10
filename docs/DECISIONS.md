# Architecture Decision Log

This file uses lightweight Architecture Decision Records.

## ADR-001 — Use English for Repository Artifacts

- **Status:** Accepted
- **Date:** 2026-07-25

### Context

The user communicates with ChatGPT in Russian but wants a professional international portfolio.

### Decision

All documentation, code, comments, filenames, issues, commits, and release notes are written in English. Explanations and interactive guidance are provided in Russian.

### Consequences

The repository is accessible to a wider audience while the learning process remains comfortable.

---

## ADR-002 — Use Scheduled Batch Processing

- **Status:** Accepted
- **Date:** 2026-07-25

### Context

No always-on home server is available.

### Decision

Use GitHub Actions to process accumulated Telegram links in a scheduled batch.

### Consequences

The architecture remains inexpensive and simple, but it is not real-time and scheduled execution may be delayed.

---

## ADR-003 — Use Telegram `getUpdates`

- **Status:** Accepted for MVP
- **Date:** 2026-07-25

### Context

A permanent webhook endpoint is not available.

### Decision

Retrieve pending Telegram messages with direct Bot API calls during the GitHub Actions run.

### Consequences

No bot hosting is required. Telegram updates are temporary, so durable recovery state on FTP and frequent validation are necessary.

---

## ADR-004 — Use FTP Server as Persistent Storage

- **Status:** Accepted with security concern
- **Date:** 2026-07-25

### Context

The user already has a separate FTP server and no home server.

### Decision

Store archive files, generated catalog files, and workflow state on the existing server.

### Consequences

The MVP avoids new infrastructure. Plain FTP is insecure; FTPS and SFTP support must be investigated before production use.

---

## ADR-005 — Use Static Frontend

- **Status:** Accepted
- **Date:** 2026-07-25

### Decision

Build the MVP frontend with HTML, CSS, and vanilla JavaScript using generated JSON indexes.

### Consequences

The frontend works on basic hosting without a backend. Advanced search and editing are deferred.

---

## ADR-006 — Preserve Originals and Create JPEG Derivatives

- **Status:** Accepted
- **Date:** 2026-07-25

### Decision

Preserve each original downloaded file and create a JPEG display copy where conversion is appropriate.

### Consequences

The archive retains source quality while the frontend receives broadly compatible images. Storage usage increases.

---

## ADR-007 — Use JSON Files Instead of a Database

- **Status:** Accepted for MVP
- **Date:** 2026-07-25

### Decision

Use JSON files for processing state and frontend indexes.

### Consequences

The implementation stays simple. Atomic writes, backups, and file-size growth must be managed.

---

## ADR-008 — Protect the Catalog with Basic Auth

- **Status:** Accepted for learning
- **Date:** 2026-07-25

### Context

The user wants to learn Basic Auth.

### Decision

Configure Basic Auth at the hosting or web-server level.

### Consequences

The catalog is not openly browseable. Basic Auth must ideally be combined with HTTPS; over HTTP, credentials can be exposed.

---

## ADR-009 — Support Only Public Image Posts in MVP

- **Status:** Accepted
- **Date:** 2026-07-25

### Decision

Support public posts containing still images and caption text. Private posts, video, Reels, and Stories are excluded.

### Consequences

The first release remains focused and avoids authentication complexity.

---

## ADR-010 — Use Major Development Stages

- **Status:** Accepted
- **Date:** 2026-07-25

### Decision

Work in major stages, reviewing scope before each stage. Switch to one-step-at-a-time guidance for unfamiliar work.

### Consequences

The process remains structured without forcing an unnecessarily slow workflow.

---

## ADR-011 — Treat AI Usage as Portfolio Evidence

- **Status:** Accepted
- **Date:** 2026-07-25

### Decision

Document how AI supports planning, implementation, debugging, review, and learning. Clearly distinguish generated suggestions from tested results.

### Consequences

The repository demonstrates AI literacy without misrepresenting AI-generated code as independently authored or validated.

---

## Open Decisions

| ID | Question | Required Before |
|---|---|---|
| OD-001 | Does the server support FTPS? | FTP integration |
| OD-002 | Does the server support SFTP? | FTP integration |
| OD-003 | What is the exact remote web root? | Deployment |
| OD-004 | How is Basic Auth configured? | Frontend release |
| OD-005 | Can HTTPS be enabled? | Public exposure |
| OD-006 | Which Instagram extraction adapter passes the proof of concept? | Core implementation |
| OD-007 | How are MVP tags generated when the user sends only a URL? | Catalog implementation |
| OD-008 | Should repository visibility be public from the start? | GitHub setup |
