# Learning Log

This log records verified learning outcomes, not only completed tasks.

Use it for lessons that are reusable beyond a single command or minor implementation step.

## Entry Template

### YYYY-MM-DD — Topic

**Objective**

What was being learned or validated?

**What I did**

What concrete actions were completed?

**What I learned**

Explain the concept in my own words.

**AI contribution**

How was AI used: planning, explanation, code generation, debugging, review, or documentation?

**My validation**

What did I personally inspect, run, or verify?

**Evidence**

- issue:
- commit:
- workflow:
- screenshot:
- test result:

**Open questions**

What remains unclear?

---

## 2026-07-25 — Project Definition

**Objective**

Define IPcoll as a structured learning and portfolio project.

**What I did**

- defined the user journey;
- selected a minimal batch architecture;
- selected GitHub Actions, Telegram, FTP, and a static frontend;
- defined the MVP boundary;
- identified security and platform risks;
- created the initial documentation plan.

**What I learned**

A project should separate the user problem, MVP scope, architecture, technical decisions, risks, and implementation plan before coding begins.

**AI contribution**

AI helped structure requirements, identify missing decisions, compare architecture options, and generate the first documentation baseline.

**My validation**

I reviewed the requirement questions and confirmed the intended workflow.

**Evidence**

- documentation baseline;
- initial decision log;
- MVP acceptance criteria.

**Open questions**

- FTP security capabilities;
- Basic Auth configuration;
- HTTPS availability;
- long-term reliability of the Instagram extraction approach;
- tag source.

---

## 2026-08-12 — Instagram Extraction Proof of Concept

**Objective**

Validate whether a supported public Instagram image post can be retrieved without building the full adapter first.

**What I did**

- installed and tested Instaloader `4.15.3`;
- processed a real public Instagram carousel locally;
- derived the post shortcode from the URL;
- downloaded all nine carousel images;
- retrieved the caption;
- inspected the raw Instaloader metadata;
- confirmed that the proof of concept worked without login for this test post.

**What I learned**

A public Instagram URL does not contain the media itself; extraction depends on platform behavior and an adapter that can retrieve the post data.

The proof of concept demonstrated that Instaloader can currently retrieve the required image carousel, caption, and metadata for the tested post, but this does not guarantee long-term platform stability.

Raw extractor metadata contains many implementation-specific and temporary fields, so it should not automatically become the permanent IPcoll data model.

**AI contribution**

AI helped compare extraction options, design the proof of concept, inspect the result, and separate useful archive metadata from extractor-specific data.

**My validation**

I ran the Instaloader command locally and inspected the downloaded images, caption file, and decompressed metadata.

**Evidence**

- local successful extraction of a nine-image carousel;
- caption retrieved;
- raw metadata inspected.

**Open questions**

- whether the same approach works reliably in GitHub Actions;
- whether anonymous extraction remains sufficient;
- how extractor failures should be classified and retried.

---

## 2026-08-12 — Project-Local Python Environment and Dependencies

**Objective**

Make the Python environment reproducible and keep project dependencies separate from global Python packages.

**What I did**

- used a project-local `.venv`;
- configured dependencies in `pyproject.toml`;
- separated runtime and development dependencies;
- installed the project with `python -m pip install -e ".[dev]"`;
- configured pytest through `pyproject.toml`.

**What I learned**

The virtual environment contains the actual locally installed packages, while `pyproject.toml` records what the project requires so the environment can be recreated.

Using `python -m pip` makes it explicit which Python interpreter owns the installed package.

Editable installation also validates that the Python project metadata is internally consistent.

**AI contribution**

AI explained the relationship between `.venv`, `pip`, and `pyproject.toml` and helped diagnose an incomplete project configuration.

**My validation**

I activated `.venv`, installed the project dependencies, and successfully ran pytest using the project configuration.

**Evidence**

- pytest recognized `pyproject.toml`;
- project tests executed from the local virtual environment.

**Open questions**

- none for the current environment setup.

---

## 2026-08-12 — Deterministic Archive Naming

**Objective**

Implement and validate the accepted monthly archive naming convention.

**What I did**

- implemented deterministic caption-prefix normalization;
- ensured normalization occurs before the 14-character limit;
- implemented metadata and media filenames;
- implemented `archive/YYYY/MM/` directory generation;
- implemented complete relative archive paths;
- added automated tests for normal and edge-case behavior.

**What I learned**

The order of normalization operations matters.

If the caption is truncated before removing emoji or collapsing whitespace, discarded characters consume the length limit and produce unstable or unintuitive filenames.

Small deterministic transformations are good candidates for unit tests because their expected behavior can be specified precisely without external services.

**AI contribution**

AI helped identify the normalization-order bug, propose focused functions, and expand test coverage.

**My validation**

I ran the complete test suite after each change.

**Evidence**

- `src/naming.py`;
- `tests/test_naming.py`;
- test result: `15 passed`.

**Open questions**

- practical collision handling for posts with the same publication date and identical caption prefix;
- whether additional filename rules are needed after real FTP testing.
