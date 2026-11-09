
import csv
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = PROJECT_DIR / "sample-data" / "grants.csv"
REPORT_DIR = PROJECT_DIR / "reports"
REPORT_FILE = REPORT_DIR / "grant_review.txt"

REQUIRED_FIELDS = [
    "Grant Name",
    "Funder",
    "Deadline",
    "Eligibility",
    "Funding Amount",
    "Required Documents"
]


def check_grants():
    """Check grant records for missing required information."""

    if not CSV_FILE.exists():
        print(f"Error: CSV file not found: {CSV_FILE}")
        return

    with CSV_FILE.open(
        "r", newline="", encoding="utf-8-sig"
    ) as file:
        reader = csv.DictReader(file)
        grants = list(reader)

    report = [
        "GRANT DATA QUALITY REPORT",
        "=" * 35,
        ""
    ]

    incomplete_count = 0

    for grant in grants:
        grant_name = (
            grant.get("Grant Name") or ""
        ).strip() or "Unnamed Grant"

        missing_fields = []

        for field in REQUIRED_FIELDS:
            value = grant.get(field)

            if value is None or not value.strip():
                missing_fields.append(field)

        report.append(f"Grant: {grant_name}")

        if missing_fields:
            incomplete_count += 1
            report.append("Status: INCOMPLETE")
            report.append(
                "Missing fields: " + ", ".join(missing_fields)
            )
        else:
            report.append(
                "Status: All required fields present"
            )

        report.append("")

    report.append("=" * 35)
    report.append(f"Total records checked: {len(grants)}")
    report.append(f"Incomplete records: {incomplete_count}")
    report.append("")

    if incomplete_count > 0:
        report.append(
            "ACTION REQUIRED: Review incomplete grant records."
        )
    else:
        report.append(
            "All grant records passed the required-field check."
        )

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text(
        "\n".join(report), encoding="utf-8"
    )

    print("\n".join(report))
    print(f"\nReport saved to: {REPORT_FILE}")


if __name__ == "__main__":
    check_grants()
