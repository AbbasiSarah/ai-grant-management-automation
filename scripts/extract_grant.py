
import csv
import re
from pathlib import Path
from datetime import datetime


# --------------------------------------------------
# 1. PROJECT PATHS
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_DIR / "sample-data" / "sample-rfp.txt"

OUTPUT_CSV = PROJECT_DIR / "sample-data" / "extracted_grants.csv"

REPORT_DIR = PROJECT_DIR / "reports"

REPORT_FILE = REPORT_DIR / "extracted_grant_requirements.txt"


# --------------------------------------------------
# 2. READ THE GRANT ANNOUNCEMENT
# --------------------------------------------------

def read_grant_document():
    """Read the source grant announcement."""

    if not INPUT_FILE.exists():
        print(f"ERROR: Grant document not found: {INPUT_FILE}")
        return None

    return INPUT_FILE.read_text(encoding="utf-8")


# --------------------------------------------------
# 3. EXTRACT GRANT REQUIREMENTS
# --------------------------------------------------

def extract_requirements(text):
    """Extract fields from a consistently formatted text document."""

    lines = [line.strip() for line in text.splitlines()]

    # Remove empty lines for identifying the heading and funder.
    non_empty_lines = [line for line in lines if line]

    grant_name = re.search(
        r"(?m)^([A-Z][A-Z ]*GRANT)\s*$",
        text
    )

    funding = re.search(
        r"(?im)^Funding Limit:\s*(.+)$",
        text
    )

    deadline = re.search(
        r"(?im)^Application Deadline:\s*(.+)$",
        text
    )

    eligibility = re.search(
        r"(?is)^Eligibility:\s*\n(.+?)(?=\n\s*\n|\Z)",
        text
    )

    documents = re.search(
        r"(?is)^Required Documents:\s*\n(.+?)(?=\n\s*\n|\Z)",
        text
    )

    # The sample format places the funder on the second non-empty line.
    funder_name = "Not specified"

    if len(non_empty_lines) >= 2:
        candidate = non_empty_lines[1]

        if not candidate.upper().startswith(
            ("FUNDING LIMIT:", "APPLICATION DEADLINE:", "ELIGIBILITY:")
        ):
            funder_name = candidate

    # Extract each numbered required document as a separate item.
    document_list = []

    if documents:
        for line in documents.group(1).splitlines():
            item = re.sub(r"^\s*(?:\d+[.)]|[-*])\s*", "", line).strip()

            if item:
                document_list.append(item)

    requirements = {
        "Grant Name": (
            grant_name.group(1).strip()
            if grant_name else "Not specified"
        ),
        "Funder": funder_name,
        "Funding Amount": (
            funding.group(1).strip()
            if funding else "Not specified"
        ),
        "Deadline": (
            deadline.group(1).strip()
            if deadline else "Not specified"
        ),
        "Eligibility": (
            " ".join(eligibility.group(1).split())
            if eligibility else "Not specified"
        ),
        "Required Documents": (
            "; ".join(document_list)
            if document_list else "Not specified"
        ),
        "Status": "Needs Review",
        "Next Action": "Verify extracted information against the source",
    }

    return requirements


# --------------------------------------------------
# 4. VALIDATE EXTRACTED FIELDS
# --------------------------------------------------

def validate_requirements(requirements):
    """Identify fields that could not be extracted."""

    required_fields = [
        "Grant Name",
        "Funder",
        "Funding Amount",
        "Deadline",
        "Eligibility",
        "Required Documents",
    ]

    missing_fields = []

    for field in required_fields:
        value = requirements.get(field, "")

        if not value or value == "Not specified":
            missing_fields.append(field)

    # Check that the deadline uses the expected date format.
    deadline = requirements.get("Deadline", "")

    if deadline != "Not specified":
        try:
            datetime.strptime(deadline, "%B %d, %Y")
        except ValueError:
            missing_fields.append("Deadline format requires review")

    return missing_fields


# --------------------------------------------------
# 5. SAVE STRUCTURED CSV OUTPUT
# --------------------------------------------------

def save_csv(requirements):
    """Save extracted requirements as a new CSV record."""

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "Grant Name",
        "Funder",
        "Deadline",
        "Eligibility",
        "Funding Amount",
        "Required Documents",
        "Status",
        "Next Action",
    ]

    # Create a separate output file; do not overwrite the original grants.
    with OUTPUT_CSV.open(
        "w", newline="", encoding="utf-8-sig"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({
            field: requirements.get(field, "")
            for field in fieldnames
        })

    print(f"CSV saved to: {OUTPUT_CSV}")


# --------------------------------------------------
# 6. GENERATE A HUMAN-READABLE REPORT
# --------------------------------------------------

def save_report(requirements, missing_fields):
    """Save extracted data and review warnings."""

    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    with REPORT_FILE.open("w", encoding="utf-8") as file:
        file.write("GRANT REQUIREMENT EXTRACTION REPORT\n")
        file.write("=" * 42 + "\n\n")

        file.write(f"Source document: {INPUT_FILE.name}\n")
        file.write("Extraction method: Python text-pattern matching\n\n")

        for field, value in requirements.items():
            file.write(f"{field}:\n{value}\n\n")

        file.write("=" * 42 + "\n")

        if missing_fields:
            file.write("INFORMATION REQUIRING REVIEW\n\n")

            for field in missing_fields:
                file.write(f"- {field}\n")
        else:
            file.write(
                "All required fields were extracted.\n"
            )

        file.write(
            "\nIMPORTANT: Extraction does not establish factual accuracy. "
            "Verify the information against the original announcement "
            "before using it in an application.\n"
        )

    print(f"Report saved to: {REPORT_FILE}")


# --------------------------------------------------
# 7. RUN THE COMPLETE WORKFLOW
# --------------------------------------------------

def main():
    """Run extraction, validation, CSV export and report generation."""

    print("\nAI GRANT MANAGEMENT AUTOMATION")
    print("=" * 42)

    text = read_grant_document()

    if text is None:
        return

    requirements = extract_requirements(text)
    missing_fields = validate_requirements(requirements)

    print("\nEXTRACTED REQUIREMENTS")
    print("-" * 42)

    for field, value in requirements.items():
        print(f"{field}: {value}\n")

    if missing_fields:
        print("REVIEW REQUIRED")

        for field in missing_fields:
            print(f"- {field}")
    else:
        print("All required fields were extracted.")

    print("\nSAVING OUTPUTS")
    print("-" * 42)

    save_csv(requirements)
    save_report(requirements, missing_fields)

    print("\nWorkflow finished.")
    print("Please review the output before relying on it.")


if __name__ == "__main__":
    main()
