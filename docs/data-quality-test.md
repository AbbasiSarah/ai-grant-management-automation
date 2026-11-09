# Grant Data Quality Test

## Objective
To verify that the grant data validation program identifies complete and incomplete grant records.

## Test Cases

| Test Case | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| 1 | Complete grant record | All required fields present | All required fields present | PASS |
| 2 | Grant missing deadline and funding amount | Identify missing fields | Deadline and Funding Amount identified | PASS |

## Test Summary

- Total records tested: 2
- Complete records: 1
- Incomplete records: 1
- Missing fields detected: Deadline and Funding Amount
- Overall result: Both test cases passed.

## Conclusion
The test demonstrates that the validation logic can identify missing required information in fictional grant records. This can help flag records for review before they move to the next stage of a grant management workflow.

**Note:** This is a learning portfolio project using fictional data. The test was performed using sample data embedded in the Python code; it does not yet demonstrate automatic validation of the repository's CSV file.
