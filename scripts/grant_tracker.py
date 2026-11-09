
import csv
from pathlib import Path
from datetime import date, datetime

# Project file locations
PROJECT_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = PROJECT_DIR / "sample-data" / "grants.csv"
REPORT_DIR = PROJECT_DIR / "reports"
REPORT_FILE = REPORT_DIR / "grant_review.txt"

# Required grant information
REQUIRED_FIELDS = [
    "Grant Name",
    "Funder",
    "Deadline",
    "Eligibility",
    "Funding Amount",
    "Required Documents"
]


def get_deadline_status(deadline_text):
    """Check whether a grant deadline is overdue or approaching."""

    try:
        deadline = datetime.strptime(
            deadline_text.strip(), "%Y-%m-%d"
        ).date()
    except (ValueError, AttributeError):
        return "INVALID DEADLINE"

    days_left = (deadline - date.today()).days

    if days_left < 0:
        return f"OVERDUE ({abs(days_left)} days ago)"
    elif days_left <= 30:
        return f"DUE SOON ({days_left} days left)"
    else:
        return f"UPCOMING ({days_left} days left)"


def check_grants():
    """Validate grant information and monitor deadlines."""

    if not CSV_FILE.exists():
        print(f"Error: CSV file not found: {CSV_FILE}")
        return

    with CSV_FILE.open(
        "r", newline="", encoding="utf-8-sig"
    ) as file:
        reader = csv.DictReader(file)
        grants = list(reader)

    report = [
        "GRANT DATA QUALITY AND DEADLINE REPORT",
        "=" * 42,
        ""
    ]

    incomplete_count = 0
    overdue_count = 0
    due_soon_count = 0
    invalid_deadline_count = 0

    for grant in grants:
        name = (grant.get("Grant Name") or "").strip()
        name = name or "Unnamed Grant"

        missing_fields = []

        for field in REQUIRED_FIELDS:
            value = grant.get(field)

            if value is None or not value.strip():
                missing_fields.append(field)

        deadline_status = get_deadline_status(
            grant.get("Deadline") or ""
        )

        if missing_fields:
            incomplete_count += 1

        if deadline_status.startswith("OVERDUE"):
            overdue_count += 1
        elif deadline_status.startswith("DUE SOON"):
            due_soon_count += 1
        elif deadline_status == "INVALID DEADLINE":
            invalid_deadline_count += 1

        report.append(f"Grant: {name}")

        if missing_fields:
            report.append("Data status: INCOMPLETE")
            report.append(
                "Missing fields: " + ", ".join(missing_fields)
            )
        else:
            report.append("Data status: COMPLETE")

        report.append(f"Deadline status: {deadline_status}")
        report.append("")

    report.append("=" * 42)
    report.append(f"Total grants checked: {len(grants)}")
    report.append(f"Incomplete records: {incomplete_count}")
    report.append(f"Overdue grants: {overdue_count}")
    report.append(f"Grants due within 30 days: {due_soon_count}")
    report.append(f"Invalid deadlines: {invalid_deadline_count}")
    report.append("")

    if incomplete_count > 0 or invalid_deadline_count > 0:
        report.append(
            "ACTION REQUIRED: Review incomplete records "
            "and invalid deadlines."
        )
    elif overdue_count > 0:
        report.append(
            "ACTION REQUIRED: Review overdue grant deadlines."
        )
    elif due_soon_count > 0:
        report.append(
            "REMINDER: Review grants approaching their deadlines."
        )
    else:
        report.append(
            "All grant records passed the required checks."
        )

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text(
        "\n".join(report), encoding="utf-8"
    )

    print("\n".join(report))
    print(f"\nReport saved to: {REPORT_FILE}")


if __name__ == "__main__":
    check_grants()
