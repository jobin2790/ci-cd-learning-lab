# Day 12 — CI/CD Deployment Workflow

## Objective
Create a GitHub Actions workflow that runs automated tests
before executing a deployment stage.

## Tools
- GitHub Actions
- Python 3.12
- Python unittest
- Git and GitHub

## Workflow
1. Checkout repository.
2. Set up Python.
3. Run automated tests.
4. Verify required project files.
5. Execute the deployment simulation.

## Job Dependency
The deployment job uses:

    needs: test

This ensures that deployment does not proceed when the
test job fails.

## Troubleshooting Exercise

### Initial Failure
The deployment verification step checked for:

    cicd-day10/app.py

The file was unavailable in the GitHub Actions runner
because the folder was not tracked in Git.

### Resolution
Changed the verification to check tracked project files:

    test -f tests/test_app.py
    test -f requirements.txt

### Verification
The subsequent GitHub Actions run succeeded.

- Run Python Tests: Passed
- Simulate Deployment: Passed

## Key Learning
Files on a developer's local machine are not automatically
available to a CI runner. Required files must be present
in the repository checkout.

## Important Limitation
This exercise simulates deployment. It does not deploy
an application to a live server.

## Status
Completed and verified.
