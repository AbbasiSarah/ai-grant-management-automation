# Grant Requirement Extraction — Test Results

## Test Objective

Evaluate whether the grant requirement extraction prompt identifies key requirements and distinguishes confirmed information from missing information.

## Test Input

A fictional Community Learning Grant announcement from Fictional Education Foundation.

## Expected Results

- Grant name: Community Learning Grant
- Funder: Fictional Education Foundation
- Maximum funding: $10,000
- Deadline: February 15, 2027
- Eligibility: Registered nonprofit organisations delivering educational programmes
- Required documents: Project proposal, detailed budget, and proof of registration

## Observed Results

The AI identified the main grant requirements, listed questions for the applicant, and highlighted information requiring verification.

One discrepancy was identified: the AI incorrectly marked the funder as unspecified, even though the announcement named Fictional Education Foundation.

## Improvements Required

- Improve extraction accuracy for funder names.
- Verify all extracted fields against the source announcement.
- Distinguish information explicitly stated in the source from assumptions.
- Retest the prompt after making improvements.

## Test Status

**Result: Partially successful.**

The output captured the main requirements, but the funder discrepancy needs correction. This was a manual prompt test, not an automated software test.

## Limitations

The grant announcement is fictional. These results do not establish that the prompt works reliably across real grant documents.
