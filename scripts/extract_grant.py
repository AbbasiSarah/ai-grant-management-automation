
from pathlib import Path
import re

PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_DIR / "sample-data" / "sample-rfp.txt"


def read_grant_document():
    """Read the grant announcement from a text file."""

    if not INPUT_FILE.exists():
        print(f"Error: Grant document not found: {INPUT_FILE}")
        return None

    return INPUT_FILE.read_text(encoding="utf-8")


def extract_requirements(text):
    """Extract basic grant information using text patterns."""

    grant_name = re.search(
        r"(?m)^([A-Z][A-Z ]+GRANT)$", text
    )

    funder = re.search(
        r"(?m)^(.+)$", text
    )

    funding = re.search(
        r"Funding Limit:\s*(.+)", text, re.IGNORECASE
    )

    deadline = re.search(
        r"Application Deadline:\s*(.+)", text, re.IGNORECASE
    )

    eligibility = re.search(
        r"Eligibility:\s*\n(.+)", text, re.IGNORECASE
    )

    documents = re.search(
        r"Required Documents:\s*\n(.*?)(?=\n\n|\Z)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    # Find the funder name from the line after the grant title.
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    funder_name = "Not specified"

    if len(lines) >= 2:
        if "FOUNDATION" in lines[1].upper() or "FUND" in lines[1].upper():
            funder_name = lines[1]

    return {
        "Grant Name": (
            grant_name.group(1).strip()
            if grant_name else "Not found"
        ),
        "Funder": funder_name,
        "Maximum Funding": (
            funding.group(1).strip()
            if funding else "Not specified"
        ),
        "Deadline": (
            deadline.group(1).strip()
            if deadline else "Not specified"
        ),
        "Eligibility": (
            eligibility.group(1).strip()
            if eligibility else "Not specified"
        ),
        "Required Documents": (
            documents.group(1).strip()
            if documents else "Not specified"
        ),
    }


def validate_requirements(requirements):
    """Identify fields that are missing or need further review."""

    required_fields = [
        "Grant Name",
        "Funder",
        "Maximum Funding",
        "Deadline",
        "Eligibility",
        "Required Documents",
    ]

    missing_fields = []

    for field in required_fields:
        value = requirements.get(field, "")

        if not value or value in ("Not found", "Not specified"):
            missing_fields.append(field)

    return missing_fields


def save_report(requirements, missing_fields):
    """Save extracted information and validation warnings."""

    report_dir = PROJECT_DIR / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)

    report_file = report_dir / "extracted_grant_requirements.txt"

    with report_file.open("w", encoding="utf-8") as file:
        file.write("GRANT REQUIREMENT EXTRACTION REPORT\n")
        file.write("=" * 40 + "\n\n")

        for field, value in requirements.items():
            file.write(f"{field}:\n{value}\n\n")

        if missing_fields:
            file.write("INFORMATION REQUIRING REVIEW:\n")
            for field in missing_fields:
                file.write(f"- {field}\n")
        else:
            file.write("All required fields were extracted.\n")

        file.write(
            "\nNote: This is rule-based extraction. "
            "Verify all details against the original grant announcement.\n"
        )

    print(f"Report saved to: {report_file}")


def main():
    """Run the grant extraction workflow."""

    text = read_grant_document()

    if text is None:
        return

    requirements = extract_requirements(text)
    missing_fields = validate_requirements(requirements)

    print("GRANT REQUIREMENT EXTRACTION")
    print("=" * 35)

    for field, value in requirements.items():
        print(f"{field}:")
        print(value)
        print()

    if missing_fields:
        print("INFORMATION REQUIRING REVIEW:")
        for field in missing_fields:
            print(f"- {field}")
    else:
        print("All required fields were extracted.")

    print()

    save_report(requirements, missing_fields)


if __name__ == "__main__":
    main()
