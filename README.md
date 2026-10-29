# CI/CD Learning Lab

A hands-on CI/CD learning project documenting practical experience with Git, GitHub, Python, Flask, automated testing, GitHub Actions, deployment, workflow troubleshooting, and code coverage reporting.

**Repository:** [ci-cd-learning-lab](https://github.com/jobin2790/ci-cd-learning-lab)
**Live Application:** [https://ci-cd-learning-lab.onrender.com](https://ci-cd-learning-lab.onrender.com)

## Project Overview

This project demonstrates a progressive, hands-on learning journey covering version control, continuous integration, automated testing, deployment preparation, application deployment, and CI/CD verification.

### Technologies Used

- **Version Control:** Git, GitHub
- **CI/CD:** GitHub Actions
- **Programming:** Python
- **Web Framework:** Flask
- **Testing:** Python `unittest`
- **Coverage:** Coverage.py
- **Deployment:** Render, Gunicorn
- **Configuration:** YAML
- **Development Environment:** macOS Terminal

---

## Day 1 — Git and GitHub Fundamentals

**Objective:** Understand version control and learn how to manage a Git repository.

**Tasks Completed:**
- Studied Git and version control fundamentals.
- Practised basic Git commands.
- Learned how to track changes and inspect repository history.
- Understood how local repositories connect to GitHub.

**Tools Used:**
- Git
- GitHub
- Terminal

**Result:** Established the foundation for managing project files, tracking changes, and collaborating through GitHub.

**Repository:** [View CI/CD Learning Lab](https://github.com/jobin2790/ci-cd-learning-lab)

---

## Day 2 — Git Branching

**Objective:** Learn how branches support isolated development.

**Tasks Completed:**
- Practised creating and switching branches.
- Learned how branches separate development work.
- Practised committing changes and synchronizing them with GitHub.
- Worked with a dedicated branching exercise.

**Tools Used:**
- Git
- GitHub
- Terminal

**Result:** Practised branch-based development and documented the branching exercise.

**Commit:** [Add Day 2 branching notes](https://github.com/jobin2790/ci-cd-learning-lab/commit/703c3c3)

---

## Day 3 — Continuous Integration with Pull Requests

**Objective:** Understand how pull requests can trigger automated CI checks.

**Tasks Completed:**
- Practised a dedicated feature branch workflow.
- Learned how pull requests support collaborative development.
- Explored automated checks before merging changes.
- Documented the CI pull-request exercise.

**Tools Used:**
- Git
- GitHub
- GitHub Actions

**Result:** Documented the pull-request workflow and learned how automated checks help identify issues before changes reach the main branch.

**Commit:** [Add Day 3 CI pull-request notes](https://github.com/jobin2790/ci-cd-learning-lab/commit/2a994f3)

---

## Day 4 — Automated Testing in CI

**Objective:** Run automated Python unit tests through GitHub Actions.

**Tasks Completed:**
- Created automated tests using Python `unittest`.
- Tested positive numbers, negative numbers, and zero.
- Configured GitHub Actions to execute tests automatically.
- Integrated automated testing into the CI pipeline.
- Verified the workflow execution.

**Tools Used:**
- Python 3.12
- Python `unittest`
- Git
- GitHub Actions
- YAML

**Result:** The CI workflow completed successfully with the automated testing step passing.

**Commit:** [Document Day 4 automated testing](https://github.com/jobin2790/ci-cd-learning-lab/commit/5920765)

---

## Day 5 — CI Failure Testing

**Objective:** Verify that CI detects failing tests before code is merged.

**Tasks Completed:**
- Created a feature branch for failure testing.
- Introduced an intentional assertion failure.
- Verified that local tests detected the problem.
- Investigated CI and pull-request check results.
- Corrected the failing test and validated the fix.
- Practised the pull-request workflow.

**Tools Used:**
- Git
- GitHub
- GitHub Actions
- Python
- Python `unittest`

**Result:** Practised intentional failure testing and learned how automated tests help prevent incorrect changes from being merged.

**Commit:** [Document Day 5 CI failure testing](https://github.com/jobin2790/ci-cd-learning-lab/commit/c42dddd)

---

## Day 6 — CI Workflow Improvements

**Objective:** Improve the reliability and security of the GitHub Actions workflow.

**Tasks Completed:**
- Configured read-only repository permissions.
- Set up Python 3.12 in the CI environment.
- Executed automated tests using Python `unittest`.
- Configured CI triggers for pushes and pull requests targeting `main`.
- Verified the three-test suite locally.
- Reviewed the GitHub Actions workflow results.

**Tools Used:**
- Git
- GitHub
- GitHub Actions
- Python 3.12
- Python `unittest`
- YAML

**Result:** Improved the CI workflow configuration and verified the three automated tests locally and the workflow execution.

**Commit:** [Document Day 6 CI workflow improvements](https://github.com/jobin2790/ci-cd-learning-lab/commit/3b17150)

---

## Day 7 — CI Matrix Testing

**Objective:** Run automated tests across multiple Python versions using a GitHub Actions matrix.

**Tasks Completed:**
- Configured a Python version matrix.
- Tested using Python 3.10, 3.11, and 3.12.
- Used matrix variables to select the Python version.
- Configured `fail-fast: false`.
- Reviewed workflow results and warnings.

**Tools Used:**
- Git
- GitHub
- GitHub Actions
- Python
- Python `unittest`
- YAML

**Result:** All three Python-version matrix jobs completed successfully.

**Commit:** [Document Day 7 CI matrix testing](https://github.com/jobin2790/ci-cd-learning-lab/commit/28325fe)

---

## Day 8 — CI/CD Workflow Practice

**Objective:** Continue hands-on practice with CI workflow configuration and execution.

**Tasks Completed:**
- Continued working with the CI/CD learning repository.
- Practised Git-based change management.
- Continued learning how automated workflows validate project changes.

**Tools Used:**
- Git
- GitHub
- GitHub Actions
- Terminal

**Result:** Continued the CI/CD workflow learning journey, building on the testing and matrix configuration work from earlier days.

**Repository:** [View CI/CD Learning Lab](https://github.com/jobin2790/ci-cd-learning-lab)

---

## Day 9 — CI/CD Workflow Validation

**Objective:** Continue practising workflow execution and troubleshooting.

**Tasks Completed:**
- Continued working with the project’s CI/CD workflows.
- Practised reviewing automated workflow results.
- Continued applying Git and GitHub version-control practices.

**Tools Used:**
- Git
- GitHub
- GitHub Actions
- Terminal

**Result:** Continued developing the ability to inspect workflow execution and investigate CI/CD issues.

**Repository:** [View CI/CD Learning Lab](https://github.com/jobin2790/ci-cd-learning-lab)

---

## Day 10 — Python Application and CI Verification

**Objective:** Practise CI/CD workflow execution alongside Python application development.

**Tasks Completed:**
- Added the Day 10 Python application work.
- Committed and pushed the changes to GitHub.
- Reviewed the associated CI and deployment-practice workflow results.

**Tools Used:**
- Python
- Git
- GitHub
- GitHub Actions

**Verification:**
- CI Pipeline #32: Passed
- CI/CD Deployment Practice #6: Passed

**Result:** The documented application changes were pushed, and both associated workflows passed.

**Commit:** [Day 10 — Add Python application](https://github.com/jobin2790/ci-cd-learning-lab/commit/7bd4b25)

---

## Day 11 — CI Troubleshooting

**Objective:** Improve the ability to investigate automated workflow execution.

**Tasks Completed:**
- Continued CI/CD troubleshooting practice.
- Reviewed workflow execution and error information.
- Practised identifying problems and checking workflow results.

**Tools Used:**
- Git
- GitHub
- GitHub Actions
- Terminal

**Result:** Continued building practical troubleshooting skills for automated CI workflows.

**Repository:** [View CI/CD Learning Lab](https://github.com/jobin2790/ci-cd-learning-lab)

---

## Day 12 — Deployment Workflow Troubleshooting

**Objective:** Practise diagnosing and correcting deployment workflow problems.

**Tasks Completed:**
- Worked on the deployment-practice workflow.
- Investigated an initially failing workflow.
- Applied corrections and reviewed subsequent execution results.

**Tools Used:**
- Git
- GitHub
- GitHub Actions
- YAML
- Terminal

**Result:** Practised a troubleshooting cycle involving failure investigation, correction, and workflow revalidation.

**Repository:** [View CI/CD Learning Lab](https://github.com/jobin2790/ci-cd-learning-lab)

---

## Day 13 — Deployment Verification and Troubleshooting

**Objective:** Continue working on deployment workflow verification.

**Tasks Completed:**
- Continued deployment-practice and troubleshooting exercises.
- Reviewed workflow execution and validation results.
- Practised investigating problems before considering a deployment successful.

**Tools Used:**
- Git
- GitHub
- GitHub Actions
- Terminal

**Result:** Continued developing deployment troubleshooting and verification skills.

**Repository:** [View CI/CD Learning Lab](https://github.com/jobin2790/ci-cd-learning-lab)

---

## Day 14 — Failure Recovery and Workflow Practice

**Objective:** Practise recovering from CI/CD workflow failures.

**Tasks Completed:**
- Worked with the `day14-failure-recovery` branch.
- Continued workflow troubleshooting and failure-recovery practice.
- Reviewed repository history and documented earlier CI/CD exercises.

**Tools Used:**
- Git
- GitHub
- GitHub Actions
- Terminal

**Result:** Practised failure-recovery workflows and maintained a separate branch for the Day 14 exercise.

**Branch:** `day14-failure-recovery`

**Repository:** [View CI/CD Learning Lab](https://github.com/jobin2790/ci-cd-learning-lab)

---

## Day 15 — Flask API and Deployment Workflow Practice

**Objective:** Develop and test a Flask API while practising CI/CD workflow validation.

**Tasks Completed:**
- Added a Flask API and automated tests.
- Executed the local automated test suite.
- Committed and pushed the application changes.
- Reviewed CI and deployment-practice workflow results.
- Investigated a deployment workflow failure caused by Flask not being installed in the deployment job.

**Tools Used:**
- Python
- Flask
- Python `unittest`
- Git
- GitHub
- GitHub Actions
- YAML

**Verification:**
- Local automated tests: 5 passed.
- CI Pipeline #33: Passed.
- Deployment Practice #7: Initially failed because the deployment job could not import Flask.

**Key Learning:** A deployment job must install the application's dependencies independently when its environment does not inherit dependencies from another job.

**Result:** Added the Flask API and automated tests, validated the CI pipeline, and identified a dependency-installation issue in the deployment workflow. The live deployment was completed on Day 16.

**Commit:** [Day 15 — Add Flask API and automated tests](https://github.com/jobin2790/ci-cd-learning-lab/commit/2861514)

---

## Day 16 — Flask Application Deployment on Render

**Objective:** Deploy a Flask API and verify that it works on a public URL.

**Tasks Completed:**
- Added Gunicorn to `requirements.txt`.
- Fixed a Python syntax error.
- Corrected the API test expectation.
- Ran the local automated test suite successfully.
- Connected the GitHub repository to Render.
- Deployed the Flask application using Render's Free plan.
- Verified the home endpoint returns HTTP 200 and a healthy status.
- Verified `/health` returns HTTP 200 and `{"status": "ok"}`.

**Tools Used:**
- Python
- Flask
- Gunicorn
- Python `unittest`
- Git and GitHub
- GitHub Actions
- Render Web Services

**Verification:**
- Local automated tests: 5 passed.
- Home endpoint: HTTP 200.
- Health endpoint: HTTP 200.
- Health response: `{"status": "ok"}`.

**Result:** Successfully deployed the Flask application to Render and verified both API endpoints.

**Live Application:** [https://ci-cd-learning-lab.onrender.com](https://ci-cd-learning-lab.onrender.com)

**Commit:** [Day 16 — Render deployment](https://github.com/jobin2790/ci-cd-learning-lab/commit/8928410)

---

## Day 17 — Deployment Verification and Test Synchronization

**Objective:** Update a Flask application, synchronize automated tests, and verify the deployed application.

**Tasks Completed:**
- Updated the Flask API response to identify the Day 17 deployment.
- Updated the API test to match the new response.
- Executed the automated test suite.
- Verified that all five tests passed.
- Committed and pushed changes to GitHub.
- Verified the live application response on Render.

**Tools Used:**
- Python
- Flask
- Python `unittest`
- Git and GitHub
- GitHub Actions
- Render

**Verification:**
- Automated tests: 5 passed.
- Live endpoint: `https://ci-cd-learning-lab.onrender.com/`
- Expected status: `healthy`.
- Expected message: `My CI/CD application is running - Day 17 deployment verified`.

**Key Learning:** Automated tests must be updated when the expected application response changes. A successful local test run and a verified live response provide evidence that an application change works.

**Result:** Updated the application and its tests, passed all five tests, and verified the deployed response.

**Commit:** [Day 17 — Deployment verification](https://github.com/jobin2790/ci-cd-learning-lab/commit/cd4fce1)

---

## Day 18 — Automated Test Coverage Reporting in CI/CD

**Objective:** Integrate automated test execution and code coverage reporting into the GitHub Actions CI pipeline.

**Tasks Completed:**
- Installed Coverage.py for Python code coverage measurement.
- Updated `requirements.txt` to include the coverage dependency.
- Configured GitHub Actions to run automated tests with coverage measurement.
- Generated a terminal coverage report.
- Generated an XML coverage report for CI integration.
- Configured test and coverage reports to be uploaded as GitHub Actions artifacts.
- Configured the workflow to run against Python 3.10, 3.11, and 3.12.
- Fixed a YAML syntax error in the GitHub Actions workflow.
- Verified successful GitHub Actions workflow execution.

**Tools Used:**
- Python
- Flask
- Python `unittest`
- Coverage.py
- Git and GitHub
- GitHub Actions
- YAML
- GitHub Actions Artifact Upload

**Test Results:**
- Automated tests passed: 5.
- Code coverage: 90%.
- GitHub Actions workflow: Successful.

**Coverage Reports:**
- Text reports: `test-reports/test-report-python-<version>.txt`
- XML reports: `test-reports/coverage-python-<version>.xml`

**Key Learning:** Code coverage measures how much application code is executed during automated tests. Integrating coverage reporting into CI helps identify untested code and provides visibility into test quality.

**Result:** Successfully integrated automated test coverage reporting into the CI pipeline and verified that the updated GitHub Actions workflow runs successfully.

**Commit:** [Day 18 — Test coverage reporting](https://github.com/jobin2790/ci-cd-learning-lab/commit/54cccb5)

---

## Learning Summary

### Days 1–3: Git and Version Control
- Git fundamentals and repository management.
- Branching and pull-request workflows.
- Introduction to CI checks.

### Days 4–7: Automated Testing and CI
- Python unit testing.
- Intentional failure testing.
- GitHub Actions workflow configuration.
- Multi-version Python matrix testing.

### Days 8–15: CI/CD Workflow Development
- Continued workflow practice and troubleshooting.
- Python application development and CI verification.
- Deployment workflow exercises.
- Flask API and automated test development.
- Dependency troubleshooting in deployment jobs.

### Days 16–18: Deployment and Coverage
- Flask application deployment on Render.
- Live API verification and test synchronization.
- Automated test coverage reporting in GitHub Actions.

---

## Future Learning Goals

- Configure automatic deployment after a Git push.
- Practise deployment health checks and application logs.
- Learn rollback strategies and deployment recovery.
- Continue with Docker, CI/CD pipeline improvements, and cloud deployment concepts.

---

## Repository

**GitHub:** [https://github.com/jobin2790/ci-cd-learning-lab](https://github.com/jobin2790/ci-cd-learning-lab)

**Live Flask Application:** [https://ci-cd-learning-lab.onrender.com](https://ci-cd-learning-lab.onrender.com)
