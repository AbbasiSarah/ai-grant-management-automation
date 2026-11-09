# Testing Checklist

## 1. Grant Data Validation

- [ ] Confirm that complete grant records are accepted.
- [ ] Confirm that missing grant names are detected.
- [ ] Confirm that missing deadlines are detected.
- [ ] Confirm that missing funding amounts are detected.
- [ ] Confirm that empty CSV fields are handled correctly.

## 2. Deadline Monitoring

- [ ] Test a deadline in the past.
- [ ] Test a deadline occurring today.
- [ ] Test a deadline within the next 30 days.
- [ ] Test a deadline more than 30 days away.
- [ ] Test an invalid deadline format.

## 3. Report Generation

- [ ] Confirm that the report includes every grant.
- [ ] Confirm that incomplete records are identified.
- [ ] Confirm that deadline statuses are displayed.
- [ ] Confirm that summary counts are correct.
- [ ] Confirm that the report is saved to the expected location.

## 4. Test Evidence

Record the following for each test:

| Test | Expected result | Actual result | Status |
|---|---|---|---|
| Complete grant record | Accepted | Not tested | Pending |
| Missing required field | Reported as incomplete | Not tested | Pending |
| Past deadline | Marked overdue | Not tested | Pending |
| Invalid deadline | Marked invalid | Not tested | Pending |
| Report generation | Report file created | Not tested | Pending |

## 5. Testing Policy

Do not mark a test as passed until it has actually been executed and the result verified.

This checklist is part of a learning project using fictional grant records.
