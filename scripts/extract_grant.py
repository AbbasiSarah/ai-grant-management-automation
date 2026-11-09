from pathlib import Path
import re

PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_DIR / "sample-data" / "sample-rfp.txt"


def read_grant_document():
    if not INPUT_FILE.exists():
        print(f"Error: Grant document not found: {INPUT_FILE}")
        return None

    return INPUT_FILE.read_text(encoding="utf-8")


def extract_requirements(text):
    """Extract basic fields using simple text patterns."""

    grant_name = re.search(
        r"(?m)^([A-Z][A-Z ]+GRANT)$", text
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

    return {
        "Grant Name": grant_name.group(1).strip() if grant_name else "Not found",
        "Maximum Funding": funding.group(1).strip() if funding else "Not specified",
        "Deadline": deadline.group(1).strip() if deadline else "Not specified",
        "Eligibility": eligibility.group(1).strip() if eligibility else "Not specified",
        "Required Documents": (
            documents.group(1).strip() if documents else "Not specified"
        ),
    }
def validate_requirements(requirements):
    """Identify grant requirements that need further checking."""

    required_fields = [
        "Grant Name",
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


def main():
    text = read_grant_document()

    if text is None:
        return

    requirements = extract_requirements(text)

    print("GRANT REQUIREMENT EXTRACTION")
    print("=" * 35)

    for field, value in requirements.items():
        print(f"{field}:")
        print(value)
        print()


if __name__ == "__main__":
    main()


