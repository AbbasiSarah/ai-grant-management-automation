
import csv
from pathlib import Path

# Find the project folder and grant data file
project_folder = Path(__file__).resolve().parent.parent
csv_file = project_folder / "sample-data" / "grants.csv"

# Fields that every grant record should contain
required_fields = [
    "Grant Name",
    "Funder",
    "Deadline",
    "Eligibility",
    "Funding Amount",
    "Required Documents",
]

# Read the CSV file
with csv_file.open("r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    grants = list(reader)

print("AI Grant Management Automation")
print("=" * 35)
print(f"Total grants found: {len(grants)}")

for grant in grants:
    print(f"\nGrant: {grant.get('Grant Name', 'Unknown')}")
    print(f"Deadline: {grant.get('Deadline', 'Unknown')}")

    missing = [
        field
        for field in required_fields
        if not grant.get(field, "").strip()
    ]

    if missing:
        print("Review needed: Missing " + ", ".join(missing))
    else:
        print("Basic data check: All required fields are present.")

# Save a simple report
report_folder = project_folder / "reports"
report_folder.mkdir(exist_ok=True)

report_file = report_folder / "grant_review.txt"

with report_file.open("w", encoding="utf-8") as file:
    file.write("Grant Tracker Review\n")
    file.write("====================\n")
    file.write(f"Total grants: {len(grants)}\n\n")

    for grant in grants:
        file.write(f"Grant: {grant.get('Grant Name', 'Unknown')}\n")
        file.write(f"Deadline: {grant.get('Deadline', 'Unknown')}\n")

        missing = [
            field
            for field in required_fields
            if not grant.get(field, "").strip()
        ]

        if missing:
            file.write("Missing fields: " + ", ".join(missing) + "\n")
        else:
            file.write("All required fields are present.\n")

        file.write("\n")

print(f"\nReport saved to: {report_file}")
