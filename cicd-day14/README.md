# Day 14 – CI/CD Failure Recovery

## Objective
Understand how automated tests detect failures
and verify that the application recovers after
the incorrect test is removed.

## Tasks Completed
- Ran the original Python unit tests.
- Introduced an intentional test failure.
- Observed the AssertionError: 4 != 5.
- Removed the intentional failing test.
- Reran the test suite.
- Confirmed all three remaining tests passed.

## Tools Used
- Git
- GitHub Actions
- Python 3
- Python unittest
- Terminal

## Results
- Initial test run: 3 passed, 1 failed.
- Recovery test run: 3 passed, 0 failed.
- Final local test status: OK.

## Key Learning
Automated tests help detect application problems.
A failed test should be investigated, corrected when
appropriate, and rerun before changes are committed.

## Limitation
Local test success does not automatically prove
that the GitHub Actions workflow succeeds.
