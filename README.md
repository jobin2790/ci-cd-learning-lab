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

### Day 17: CI/CD Deployment Verification and Test Synchronization

**Objective:** Update a Flask application, synchronize automated tests, and verify the deployed application.

**Tasks completed:**
- Updated the Flask API response to identify the Day 17 deployment.
- Updated the API test to match the new response.
- Executed the automated test suite.
- Verified that all 5 tests passed.
- Committed and pushed changes to GitHub.
- Verified the live application response on Render.

**Tools used:**
- Python and Flask
- Python unittest
- Git and GitHub
- GitHub Actions
- Render

**Verification:**
- Automated tests: 5 passed.
- Git commit: `Day 17: update deployment verification tests`
- Live endpoint: `https://ci-cd-learning-lab.onrender.com/`
- Expected status: `healthy`
- Expected message: `My CI/CD application is running - Day 17 deployment verified`

**Key learning:** Automated tests must be updated when the expected application response changes. A successful local test run and a verified live response provide evidence that the application change works.

### Day 18: Automated Test Coverage Reporting in CI/CD

**Objective:** Integrate automated test execution and code coverage reporting into the GitHub Actions CI pipeline.

**Tools Used:**
- Python
- Flask
- Python `unittest`
- Coverage.py
- Git and GitHub
- GitHub Actions
- GitHub Actions Artifact Upload

**Tasks Completed:**
- Installed Coverage.py for Python code coverage measurement.
- Updated `requirements.txt` to include the coverage dependency.
- Configured the GitHub Actions workflow to run automated tests with coverage measurement.
- Generated a terminal coverage report.
- Generated an XML coverage report for CI integration.
- Configured test and coverage reports to be uploaded as GitHub Actions artifacts.
- Configured the workflow to run against Python 3.10, 3.11, and 3.12.
- Fixed a YAML syntax error in the GitHub Actions workflow.
- Verified successful GitHub Actions workflow execution.

**Test Results:**
- Automated tests passed: 5
- Code coverage: 90%
- GitHub Actions workflow: Successful

**Coverage Reports:**
- Text reports: `test-reports/test-report-python-<version>.txt`
- XML reports: `test-reports/coverage-python-<version>.xml`

**Key Learning:**
Code coverage measures how much of the application code is executed during automated tests. Integrating coverage reporting into CI helps identify untested code and provides visibility into test quality.

**Outcome:**
Successfully integrated automated test coverage reporting into the CI pipeline and verified that the updated GitHub Actions workflow runs successfully.

**GitHub Repository:** https://github.com/jobin2790/ci-cd-learning-lab
