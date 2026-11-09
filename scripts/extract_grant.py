from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_DIR / "sample-data" / "sample-rfp.txt"


def read_grant_document():
    """Read and display the contents of a grant announcement."""

    if not INPUT_FILE.exists():
        print(f"Error: Grant document not found: {INPUT_FILE}")
        return

    content = INPUT_FILE.read_text(encoding="utf-8")

    print("GRANT DOCUMENT")
    print("=" * 40)
    print(content)


if __name__ == "__main__":
    read_grant_document()
