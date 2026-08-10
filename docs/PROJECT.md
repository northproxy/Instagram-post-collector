# Project Definition

## Project Name

**IPcoll — Instagram Post Collector**

## Project Type

A minimal learning project developed as a public GitHub portfolio repository.

## Vision

Create a personal, independent, searchable archive of useful public Instagram image posts without requiring an always-on home server.

## Primary Outcome

A mobile-friendly web catalog that allows the user to browse archived Instagram posts and download selected images to a phone or computer.

## Project Motivation

The project is not only intended to solve a personal archiving problem. Its main portfolio purpose is to demonstrate disciplined project execution:

- requirements discovery;
- MVP definition;
- architecture design;
- documented technical decisions;
- backlog and milestone management;
- implementation in clear stages;
- validation and evidence;
- responsible AI-assisted development.

## Core User Story

> As a user browsing Instagram, I want to share an interesting public image-post URL with my Telegram bot so that the post is processed automatically, archived on my FTP server, and displayed in a browser-based catalog where I can later review and download its images.

## Project Goals

1. Build a working end-to-end automation.
2. Use GitHub Actions as the scheduled execution environment.
3. Use Telegram as the collection interface.
4. Use the existing FTP server as storage and web hosting.
5. Build the first frontend with HTML, CSS, and vanilla JavaScript.
6. Create professional English-language documentation.
7. Maintain a visible decision and learning history.
8. Demonstrate effective human–AI collaboration.

## Non-Goals for MVP

- Supporting private Instagram posts
- Downloading Reels or video
- Running a permanent server process
- User registration or multi-user accounts
- Full-text search
- Editing posts in the browser
- Advanced frontend frameworks
- Native mobile applications
- Guaranteed execution at exactly 06:19
- Bypassing access restrictions or platform protections

## Stakeholder

The project owner, primary user, product manager, tester, and learner are the same person.

## Working Language

- User–ChatGPT communication: Russian
- Repository documentation: English
- Source code, comments, commits, issues, and pull requests: English

## Delivery Method

Development is organized into major stages. Before beginning each major stage, scope and expected outputs are reviewed. Unfamiliar technical work may be split into one-action-at-a-time instructions.

## MVP Definition of Done

The MVP is complete when the following scenario works reliably:

> The user shares a public Instagram image-post URL with the Telegram bot. A scheduled GitHub Actions workflow processes the URL, uploads original images, JPEG derivatives, Markdown, and JSON metadata to the FTP server, updates the protected static web catalog, and sends a success or error report to Telegram. The user can then open the catalog on a phone or computer, filter posts by author or tag, open a post, and download an image locally.

## Success Metrics

- At least 20 test posts processed
- At least 90% successful processing for supported public test posts
- No duplicate archive entries after workflow retries
- Failed posts retained for retry or manual review
- Catalog usable on a current mobile browser
- Secrets absent from repository history and workflow logs
- Documentation matches the implemented system
- Each major decision and learning outcome is recorded

## Ethical and Legal Position

IPcoll is designed for personal archiving of content the user can lawfully access. It must not be used to bypass private-account restrictions, access controls, or technical protections. Original authors retain rights to downloaded content.
