# AI Grant Management Automation

## Project Overview

This is a beginner-friendly Python portfolio project that demonstrates how parts of a grant management workflow can be automated using structured data validation and deadline monitoring.

**Note:** This is a learning project using fictional grant data. It is not connected to real grant providers or clients.

## Features

- **Grant data validation:** Checks whether required fields are present.
- **Missing information detection:** Identifies incomplete grant records.
- **Deadline monitoring:** Classifies deadlines as overdue, due soon, upcoming, or invalid.
- **Report generation:** Produces a text report summarizing validation results.
- **Sample grant dataset:** Uses fictional grant records stored in CSV format.
- **Documented workflow:** Includes requirement extraction prompts, client information checklists, and testing documentation.

## Technologies Used

- Python
- CSV data processing
- `pathlib` for file handling
- `datetime` for deadline calculations
- Git and GitHub

## Project Structure

```text
ai-grant-management-automation/
├── docs/
│   ├── workflow.md
│   ├── client-information-checklist.md
│   ├── client-readiness-test.md
│   ├── data-quality-test.md
│   ├── validation-test-results.md
│   └── deadline-test-results.md
├── prompts/
│   └── grant-requirement-extraction.md
├── sample-data/
│   └── grants.csv
├── scripts/
│   └── grant_tracker.py
├── reports/
└── README.md
```

## How It Works

1. Reads grant records from a CSV file.
2. Checks required fields for missing information.
3. Evaluates each grant deadline.
4. Summarizes incomplete records and deadline statuses.
5. Saves the results to `reports/grant_review.txt`.

## How to Run

1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python scripts/grant_tracker.py
```

The generated report is saved in the `reports` folder.

## Testing

The project includes documentation for data quality checks and deadline test cases. Test results should be marked as passed only after verifying the program's actual output.

## Current Limitations

- Grant records are fictional.
- The program checks whether fields are present but does not verify grant eligibility with funding providers.
- Deadline monitoring runs only when the script is executed.
- Automatic emails, scheduled checks, and live grant discovery are not implemented.
- The program does not submit grant applications.

## Future Improvements

- Add automated deadline reminders.
- Validate funding amounts and date formats more thoroughly.
- Add automated unit tests.
- Integrate AI-assisted grant requirement extraction.
- Develop a simple dashboard for reviewing grants.

## Learning Goals

This project demonstrates beginner-level skills in Python programming, CSV processing, data validation, date handling, file management, workflow documentation, and GitHub version control.
