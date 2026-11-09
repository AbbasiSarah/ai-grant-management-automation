# AI Grant Management Automation — Architecture

## 1. Overview

This project demonstrates a workflow for organizing grant information, checking data quality, monitoring deadlines, and supporting AI-assisted grant preparation.

## 2. System Components

### Sample Grant Data
**File:** `sample-data/grants.csv`

Stores fictional grant records, including grant name, funder, deadline, eligibility, funding amount, and required documents.

### Python Grant Tracker
**File:** `scripts/grant_tracker.py`

Responsible for:
- Reading grant records from a CSV file.
- Checking required fields.
- Identifying missing information.
- Monitoring grant deadlines.
- Generating a text report.

### AI Prompt Templates
**Directory:** `prompts/`

Contains instructions for extracting grant requirements and identifying missing information without inventing facts.

### Documentation
**Directory:** `docs/`

Describes the workflow, testing examples, client readiness checks, data quality, and project roadmap.

## 3. Workflow

1. Store grant information in the CSV file.
2. Validate required grant fields.
3. Check deadline status.
4. Generate a report for review.
5. Use an AI prompt to extract grant requirements when needed.
6. Collect missing client information.
7. Review and verify information before drafting an application.

## 4. Data Flow

CSV grant records → Python validation → Deadline checks → Text report → Human review

AI-assisted requirement extraction is a separate workflow component and should be connected to the tracker only when implemented.

## 5. Responsible AI

- Use fictional data for demonstrations.
- Verify requirements against official funder documents.
- Never assume missing client information.
- Protect confidential client information.
- Require human approval before submitting an application.

## 6. Current Limitations

This is a learning project. Features described in the workflow or roadmap may not yet be fully implemented or tested. No live grant database, external AI API, or automatic application submission is assumed.
