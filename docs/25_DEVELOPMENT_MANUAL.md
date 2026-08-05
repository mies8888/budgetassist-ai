Development Manual (Document 25)

Purpose

This manual describes how to get the development environment running, common workflows, and how to work with the monorepo.

Prerequisites

- Docker & Docker Compose
- Node 18+ / npm or pnpm
- Python 3.10+

Local development (quickstart)

1. Copy .env.example to .env and update secrets as needed (local dev credentials are fine).
2. Start services via docker-compose (development file provided):

   docker compose up --build

3. Backend will be reachable at http://localhost:8000 by default (uvicorn)
4. Frontend dev server runs at http://localhost:3000 (Vite)

Backend dev

- The backend is a FastAPI skeleton. Run locally without Docker:

  python -m venv .venv
  . .venv\Scripts\Activate.ps1  # PowerShell on Windows
  pip install -r backend/requirements.txt
  uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

- Database migrations: Alembic configuration will be added under backend/alembic/ (not included in scaffold). Use asyncpg URL from .env.

Frontend dev

- Install and run frontend in development:

  cd frontend
  npm install
  npm run dev

- Tailwind is configured; styles are included in src/index.css

Testing

- Backend tests should be placed under tests/ and executed with pytest or unittest. CI runs `python -m unittest discover`.

Docker Compose services

- backend: FastAPI app (uvicorn)
- frontend: Vite dev server for developer UX
- db: Postgres
- redis: Redis for Celery and caching
- qdrant: Vector DB for embeddings
- minio: S3-compatible object storage for artifacts
- ollama: Local LLM hosting (optional)

Contributing

- Follow the conventional commit style for commit messages (optional).
- Run the included unit tests and linting before opening a PR.

Security

- Never commit secrets. Use .env and .env.example patterns.

This manual is intentionally concise. Add project-specific developer notes and runbooks into docs/ as the project matures.
