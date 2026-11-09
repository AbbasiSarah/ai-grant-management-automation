
import sys
import unittest
from pathlib import Path
from datetime import date, timedelta

# Make the scripts folder available for importing
PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_DIR / "scripts"))

from grant_tracker import get_deadline_status


class TestGrantDeadlineStatus(unittest.TestCase):

    def test_overdue_deadline(self):
        yesterday = (date.today() - timedelta(days=1)).isoformat()
        result = get_deadline_status(yesterday)
        self.assertTrue(result.startswith("OVERDUE"))

    def test_deadline_due_soon(self):
        soon = (date.today() + timedelta(days=10)).isoformat()
        result = get_deadline_status(soon)
        self.assertTrue(result.startswith("DUE SOON"))

    def test_upcoming_deadline(self):
        later = (date.today() + timedelta(days=45)).isoformat()
        result = get_deadline_status(later)
        self.assertTrue(result.startswith("UPCOMING"))

    def test_invalid_deadline(self):
        result = get_deadline_status("not-a-date")
        self.assertEqual(result, "INVALID DEADLINE")


if __name__ == "__main__":
    unittest.main()
