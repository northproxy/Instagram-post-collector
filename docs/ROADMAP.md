# Roadmap

## Stage 0 — Project Foundation

### Goal

Create a professional project baseline before implementation.

### Deliverables

- repository;
- documentation pack;
- license;
- GitHub Project;
- labels and milestones;
- initial issues;
- branch and commit conventions;
- security checklist.

### Definition of Done

All project documents are reviewed, open decisions are visible, and Stage 1 issues are ready.

---

## Stage 1 — Technical Discovery and Proof of Concept

### Goal

Validate the risky external integrations before building the full system.

### Work

- verify FTP, FTPS, and SFTP support;
- identify remote web root;
- verify Basic Auth options;
- verify whether HTTPS can be enabled;
- test Telegram `getUpdates`;
- verify authorized user ID;
- test one public Instagram image post;
- test one image carousel;
- test caption retrieval;
- test GitHub Actions runner compatibility;
- upload a synthetic file to FTP;
- download the uploaded file over HTTP.

### Definition of Done

One supported public post can be processed manually in GitHub Actions and uploaded to a non-production test directory.

---

## Stage 2 — Core Python Pipeline

### Goal

Build modular local processing with fake external services.

### Work

- configuration;
- URL parsing;
- domain models;
- metadata generation;
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

### Goal

Process supported public image posts.

### Work

- adapter proof;
- post metadata;
- media download;
- carousel support;
- unsupported video detection;
- safe errors;
- retry logic.

### Definition of Done

A defined test set reaches the success target and failures are classified.

---

## Stage 5 — FTP Persistence and Deployment

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
