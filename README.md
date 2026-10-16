# CI/CD Learning Lab
# Day 2 - Git Branching
#Day 3 -CI on Pull Requests
## Day 4 - Automated Testing in CI

### What I practiced
- Created automated tests using Python unittest.
- Tested positive numbers, negative numbers, and zero.
- Configured GitHub Actions to run tests automatically.
- Integrated automated testing into the CI pipeline.
- Verified that the CI workflow completed successfully.

### Tools used
- Python 3.12
- Python unittest
- Git
- GitHub Actions

### Result
The CI workflow completed successfully with the automated testing step passing.

## Day 5 — CI Failure Testing

### Objective
Verify that automated tests detect failures before code is merged.

### What I practiced
- Created a feature branch for failure testing.
- Intentionally modified a test to trigger an assertion failure.
- Verified that local tests detected the failure.
- Confirmed that GitHub Actions failed the pull request check.
- Fixed the failing test.
- Verified that GitHub Actions passed after the fix.
- Merged the pull request after successful validation.

### Tools used
- Git
- GitHub
- GitHub Actions
- Python
- Python unittest

### Result
Successfully demonstrated how CI detects failing tests and validates fixes before merging code.


## Day 6 — Improve CI Workflow

### Objective
Improve the reliability and security of the GitHub Actions CI workflow.

### What I Practiced
- Configured read-only repository permissions.
- Set up Python 3.12 in the CI environment.
- Executed automated tests using Python unittest.
- Configured CI to run on pushes and pull requests targeting main.
- Verified all three tests passed locally.
- Confirmed the GitHub Actions workflow completed successfully.

### Tools Used
- Git
- GitHub
- GitHub Actions
- Python 3.12
- Python unittest
- YAML

### Result
Improved the CI workflow and successfully verified all three automated tests in GitHub Actions.
