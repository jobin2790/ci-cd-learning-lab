# Day 11 — CI/CD Troubleshooting

## Objective
Learn to identify, diagnose, and fix a failing automated test
and verify the CI pipeline using GitHub Actions.

## Environment
- Python
- unittest
- Git and GitHub
- GitHub Actions
- Python versions: 3.10, 3.11, 3.12

## Exercise 1: Reproduce a Test Failure

Changed the expected result in the positive-number test:

    self.assertEqual(add(2, 3), 6)

The test failed with:

    AssertionError: 5 != 6

## Root Cause
The addition function correctly returned 5.
The expected value in the test was incorrect.

## Resolution
Restored the correct assertion:

    self.assertEqual(add(2, 3), 5)

## Local Verification
Executed:

    python3 -m unittest discover -s tests -v

Result: All three tests passed.

Tests covered:
- Positive numbers
- Negative numbers
- Zero

## GitHub Actions Verification
Workflow run: CI Pipeline #24

- Python 3.10 Tests: Passed
- Python 3.11 Tests: Passed
- Python 3.12 Tests: Passed
- Test report upload: Successful

## Lessons Learned
- Read the traceback before changing application code.
- Distinguish an application defect from an incorrect test.
- Reproduce failures locally before applying a fix.
- Verify CI results across the Python version matrix.

## Status
Completed the local troubleshooting exercise and verified
the successful GitHub Actions workflow.
