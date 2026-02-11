# Dockerized Multi-Service Web Application

A production-style multi-container web application built using Docker and Docker Compose.

## Architecture

Client → Nginx (Port 8080) → Flask (Gunicorn) → PostgreSQL

- **Flask** application served via Gunicorn
- **PostgreSQL** database container
- **Nginx** reverse proxy
- Internal Docker networking
- Health checks for service reliability
- One-command deployment

## Tech Stack

- Docker
- Docker Compose
- Python (Flask)
- Gunicorn
- PostgreSQL
- Nginx




