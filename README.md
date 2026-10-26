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


## Day 7 — CI Matrix Testing

### Objective
Run automated tests across multiple Python versions using GitHub Actions matrix testing.

### What I Practiced
- Configured a Python version matrix in GitHub Actions.
- Tested the application using Python 3.10, 3.11, and 3.12.
- Used matrix variables to select the Python version dynamically.
- Configured fail-fast: false so other jobs continue if one fails.
- Verified all three matrix jobs completed successfully.
- Reviewed GitHub Actions results and workflow warnings.

### Tools Used
- Git
- GitHub
- GitHub Actions
- Python
- Python unittest
- YAML

### Result
Successfully implemented matrix testing and verified that all three Python-version jobs passed in GitHub Actions.


---

## CI/CD Learning Roadmap — Progress Summary

### Days 1–6: Git, GitHub and CI Fundamentals
- Practised Git basics, branching and pull requests.
- Created automated Python unit tests.
- Configured GitHub Actions to run tests.
- Practised failure detection and fixing failing tests.
- Improved CI workflow permissions and reliability.

### Days 7–14: CI/CD Pipeline Development
- Continued hands-on CI/CD workflow practice.
- Practised automated testing and GitHub-based version control.
- Worked on deployment workflow configuration and troubleshooting.
- Refer to individual commits and workflow runs for the exact exercises completed on each day.

### Day 15: Deployment Workflow Practice
- Configured a GitHub Actions deployment-practice workflow.
- Added automated test and application validation steps.
- Validated workflow YAML and corrected syntax errors.
- Verified successful GitHub Actions runs.
- Note: This workflow initially simulated deployment; the actual live deployment was completed on Day 16.

### Day 16: Flask Application Deployment on Render

**Objective:** Deploy a Flask API and verify that it works on a public URL.

**Tools**
- Python and Flask
- Gunicorn
- Git and GitHub
- GitHub Actions
- Render Web Services

**Work completed**
- Added Gunicorn to `requirements.txt`.
- Fixed a Python syntax error and corrected the API test expectation.
- Ran the local automated test suite successfully: 5 tests passed.
- Connected the GitHub repository to Render.
- Deployed the Flask application using Render's Free plan.
- Verified the home endpoint returns HTTP 200 and a healthy status.
- Verified `/health` returns HTTP 200 and `{"status": "ok"}`.

**Live application:** https://ci-cd-learning-lab.onrender.com

**GitHub repository:** https://github.com/jobin2790/ci-cd-learning-lab

**Result:** The Flask application is live and both API endpoints have been verified.

### Next Steps
- Verify GitHub Actions after the README update.
- Practise automatic deployment after a Git push.
- Learn deployment health checks, logs and rollback concepts.
- Continue with the remaining CI/CD roadmap topics.
