# Roadmap

## Stage 0 — Project Foundation

**Status:** Complete

### Goal

Create a clean, professional project baseline before implementation.

### Work

- define project scope and MVP;
- establish a minimal repository structure;
- define working conventions;
- initialize Git and publish the repository;
- add a concise public README;
- document the roadmap and key decisions;
- prepare Stage 1.

### Definition of Done

- repository structure is clean and intentional;
- project scope and MVP are documented;
- GitHub repository is public and readable;
- working conventions are defined;
- Stage 1 is clearly described and ready to begin.

---

## Stage 1 — Technical Discovery and Proof of Concept

**Status:** In progress

### Goal

Validate the risky external integrations before building the full system.

### Validated So Far

- local Python environment is configured with a project-local `.venv`;
- project dependencies are managed through `pyproject.toml`;
- Instaloader `4.15.3` was validated locally against a public Instagram carousel;
- the test post was processed without login during the proof of concept;
- a nine-image carousel was downloaded successfully;
- caption retrieval was validated;
- raw Instaloader metadata was inspected;
- deterministic archive naming utilities were implemented as preparatory work for Stage 2;
- archive naming behavior is covered by 15 passing automated tests.

### Remaining Work

- verify FTP, FTPS, and SFTP support;
- identify remote web root;
- verify Basic Auth options;
- verify whether HTTPS can be enabled;
- test Telegram `getUpdates`;
- verify authorized user ID;
- test GitHub Actions runner compatibility with the selected Instagram extraction approach;
- upload a synthetic file to FTP;
- download the uploaded file over HTTP;
- validate the Instagram proof of concept in GitHub Actions rather than only locally.

### Definition of Done

One supported public post can be processed manually in GitHub Actions and uploaded to a non-production test directory.

---

## Stage 2 — Core Python Pipeline

**Status:** Not formally started

Some deterministic naming utilities have already been implemented and tested during Stage 1 because the archive naming convention was needed to validate the storage design.

### Goal

Build modular local processing with fake external services.

### Work

- configuration;
- URL parsing;
- domain models;
- normalized metadata generation;
- archive path and filename generation;
- image processing;
- state repository;
- duplicate detection;
- failure model;
- catalog builder;
- logging;
- unit tests.

### Definition of Done

Synthetic inputs produce deterministic archive packages and catalog indexes.

---

## Stage 3 — Telegram Intake

**Status:** Not started

### Goal

Collect and safely acknowledge Telegram updates.

### Work

- direct Bot API client;
- sender authorization;
- update pagination;
- URL extraction;
- offset handling;
- invalid-message handling;
- Telegram reports.

### Definition of Done

A test batch retrieves multiple links without losing or duplicating updates.

---

## Stage 4 — Instagram Adapter

**Status:** Not started

The local Instaloader proof of concept from Stage 1 is input to this stage, not yet the final adapter implementation.

### Goal

Process supported public image posts.

### Work

- adapter implementation;
- normalized post metadata;
- media download;
- carousel support;
- unsupported video detection;
- safe errors;
- retry logic.

### Definition of Done

A defined test set reaches the success target and failures are classified.

---

## Stage 5 — FTP Persistence and Deployment

**Status:** Not started

### Goal

Make server storage durable and retry-safe.

### Work

- secure transport choice;
- temporary upload;
- finalization;
- state backup;
- atomic replacement where available;
- archive validation;
- concurrency lock.

### Definition of Done

Repeated and interrupted test runs do not corrupt state or duplicate posts.

---

## Stage 6 — Mobile Frontend

**Status:** Not started

### Goal

Create the usable MVP catalog.

### Work

- responsive layout;
- catalog cards;
- post detail;
- author filter;
- tag filter;
- image download;
- loading and error states;
- Basic Auth;
- mobile browser testing.

### Definition of Done

The user can complete the target catalog journey on a phone.

---

## Stage 7 — Automation, Validation, and Release

**Status:** Not started

### Goal

Release MVP v1.0 with evidence.

### Work

- CI workflow;
- scheduled workflow;
- Vienna timezone guard;
- manual run;
- end-to-end tests;
- security review;
- screenshots;
- README update;
- release notes;
- Git tag.

### Definition of Done

All MVP acceptance criteria pass and release `v1.0.0` is published.

---

## Post-MVP Ideas

### v1.1

- full-text search;
- additional filters;
- manual tags;
- failed-item management;
- improved thumbnails;
- pagination.

### v1.2

- private content only through an explicitly reviewed lawful authentication design;
- richer Telegram commands;
- immediate webhook intake;
- stronger catalog access control.

### v2.0 — Home Server Migration

- Docker Compose;
- continuously running bot;
- SQLite or PostgreSQL;
- local or object storage;
- HTTPS;
- background workers;
- modern frontend framework selected through evaluation;
- user-controlled post management.
