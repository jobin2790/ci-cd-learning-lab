# Day 23 — Docker Compose CI Integration

## Objective
Integrate Docker Compose into a GitHub Actions CI pipeline to automatically build, start, and test a Flask application with Redis.

The goal is to verify that both application services work correctly in an automated CI environment.

## Technologies Used
- Docker
- Docker Compose
- GitHub Actions
- Flask
- Redis
- Git & GitHub
- YAML
- Ubuntu Latest

## Project Structure

```text
ci-cd-learning-lab/
├── cicd-day22/
│   ├── app/
│   ├── tests/
│   ├── Dockerfile
│   └── docker-compose.yml
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── deploy.yml
│       └── docker-compose-ci.yml
└── README.md
```

## Implementation

### 1. Created GitHub Actions Workflow

File:

`.github/workflows/docker-compose-ci.yml`

Configured the workflow to trigger automatically on:
- Push to the `main` branch
- Pull requests targeting the `main` branch

### 2. Docker Compose Configuration Validation

Validated the Docker Compose configuration using:

```bash
docker compose -f cicd-day22/docker-compose.yml config
```

This checks whether the Compose configuration is valid.

### 3. Build Docker Compose Services

Built the Flask and Redis services:

```bash
docker compose -f cicd-day22/docker-compose.yml build
```

### 4. Start Flask and Redis Containers

Started the application services:

```bash
docker compose -f cicd-day22/docker-compose.yml up -d
```

### 5. Flask Application Health Check

Configured an automated health check loop to wait for the Flask application to become available.

```bash
for i in {1..30}; do
  if curl -fsS http://localhost:5003/health; then
    echo "Flask application is healthy"
    exit 0
  fi
  sleep 2
done

echo "Application failed to start"
exit 1
```

### 6. Verify Flask Application

Verified the application using:

```bash
curl -f http://localhost:5003/
```

### 7. Verify Redis Service

Tested Redis connectivity:

```bash
docker compose -f cicd-day22/docker-compose.yml exec -T redis redis-cli ping
```

Expected output:

```text
PONG
```

### 8. Container Logs on Failure

Configured GitHub Actions to display container logs if the workflow fails.

```bash
docker compose -f cicd-day22/docker-compose.yml logs
```

### 9. Stop and Clean Up Containers

Stopped the containers after testing:

```bash
docker compose -f cicd-day22/docker-compose.yml down
```

## GitHub Actions Workflow

The workflow automatically performs the following tasks:

1. Checkout repository
2. Validate Docker Compose configuration
3. Build Docker Compose services
4. Start Flask and Redis containers
5. Wait for Flask health check
6. Verify Flask application
7. Verify Redis connectivity
8. Display logs if failure occurs
9. Stop containers and clean up

## Testing Results

| Test | Result |
|---|---|
| Docker Compose configuration validation | PASSED |
| Docker Compose service build | PASSED |
| Flask container startup | PASSED |
| Flask health check | PASSED |
| Flask application verification | PASSED |
| Redis connectivity | PASSED |
| GitHub Actions CI workflow | PASSED |
| GitHub repository push | PASSED |

## Git Commands

```bash
git add .github/workflows/docker-compose-ci.yml

git commit -m "Complete CI/CD Day 23 Docker Compose CI integration"

git push origin main
```

## GitHub Actions Verification

The workflow was successfully executed in GitHub Actions.

- Workflow: Docker Compose CI
- Branch: main
- Commit: be43adb
- Status: SUCCESS

## Key Learnings

- Integrating Docker Compose with GitHub Actions.
- Automating multi-container application testing.
- Validating Docker Compose configurations.
- Building and running Flask and Redis services in CI.
- Implementing application health checks.
- Testing Redis connectivity in an automated pipeline.
- Collecting container logs during failures.
- Automating container cleanup after testing.

## Conclusion

Successfully completed Day 23 of the 24-day CI/CD learning roadmap.

Integrated Docker Compose with GitHub Actions to automate the build, startup, and testing of a Flask application and Redis service.

The CI workflow passed successfully, confirming that the application and its supporting service can be tested automatically.

**Next: Day 24 — Final End-to-End CI/CD Pipeline Project**
