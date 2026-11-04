# CI/CD Day 22 — Docker Compose Application

## Objective
Deploy a Flask application with Redis using Docker Compose.

## Technologies Used
- Python 3.12
- Flask
- Redis
- Docker
- Docker Compose
- Gunicorn

## Architecture

Flask Web Application → Redis Database

Docker Compose manages both containers and their internal network.

## Application Features
- Flask REST application
- Redis visit counter
- Health check endpoint
- Docker containerization
- Multi-container deployment using Docker Compose

## Deployment

Build and start the application:

```bash
docker compose up --build -d
```

Check running containers:

```bash
docker compose ps
```

## Application Testing

Main endpoint:

```bash
curl http://localhost:5003
```

Health endpoint:

```bash
curl http://localhost:5003/health
```

## Expected Health Response

```json
{"status":"ok"}
```

## Learning Outcomes
- Learned Docker Compose fundamentals.
- Integrated Flask with Redis.
- Configured multi-container networking.
- Built and deployed a Dockerized application.
- Verified application functionality using curl.
- Tested the health endpoint.

## Status

Day 22 — Completed Successfully.
