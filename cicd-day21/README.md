# CI/CD Learning Lab — Day 21
## Dockerizing a Flask Application

### Objective
Containerize a Flask application using Docker and verify its deployment using HTTP endpoints.

### Technologies Used
- Python 3.12
- Flask
- Gunicorn
- Docker
- Docker Desktop
- macOS

### Project Structure

```text
ci-cd-learning-lab/
├── app/
│   └── main.py
├── Dockerfile
├── requirements.txt
└── cicd-day21/
    └── README.md
```

### Docker Image Build

```bash
docker build -t cicd-learning-app:day21 .
```

### Docker Container Deployment

The original deployment encountered a port conflict because port 5001 was already occupied by the Day 114 Docker container.

The issue was resolved by using port 5002.

```bash
docker run -d -p 5002:5000 \
--name cicd-day21-app \
cicd-learning-app:day21
```

### Container Verification

```bash
docker ps
```

### Application Testing

Test the main endpoint:

```bash
curl http://localhost:5002
```

Expected response:

```json
{
  "message": "My CI/CD application is running - Day 17 deployment verified",
  "status": "healthy"
}
```

### Health Check

```bash
curl http://localhost:5002/health
```

Expected response:

```json
{"status":"ok"}
```

### Troubleshooting

Problem:
Port 5001 was already allocated.

Solution:
Used port 5002 for the Day 21 application while preserving the existing Day 114 container.

### Learning Outcomes

- Built a Docker image for a Flask application.
- Deployed a Flask application inside a Docker container.
- Configured host-to-container port mapping.
- Resolved a Docker port allocation conflict.
- Verified application functionality using curl.
- Tested the application's health endpoint.

### Status

Day 21 — Completed Successfully.
