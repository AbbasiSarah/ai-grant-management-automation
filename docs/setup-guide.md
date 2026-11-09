# Local Setup Guide

## 1. Prerequisites

- Python 3.10 or later
- GitHub repository access
- A code editor such as Visual Studio Code

## 2. Download the Project

Clone the repository using Git:

```bash
git clone https://github.com/AbbasiSarah/ai-grant-management-automation.git
cd ai-grant-management-automation
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

## 3. Run the Grant Tracker

Open a terminal in the project folder and run:

```bash
python scripts/grant_tracker.py
```

On some Windows systems, use:

```bash
py scripts/grant_tracker.py
```

The script should read the sample CSV file and print a grant data quality and deadline report, provided the tracker contains the expected code and the CSV file exists in the expected location.

## 4. Find the Generated Report

After a successful run, look for:

```text
reports/grant_review.txt
```

The report folder is created by the script if necessary.

## 5. Dependencies

The current tracker uses Python standard-library modules. No external packages are required.

## 6. Troubleshooting

- **Python not found:** Install Python and ensure it is available from your terminal.
- **CSV file not found:** Check that `sample-data/grants.csv` exists.
- **Unexpected output:** Check the CSV column headings and the Python script.

## 7. Important Note

This is a learning project using fictional grant data. Running the script locally should be tested before claiming that the complete workflow works end to end.
