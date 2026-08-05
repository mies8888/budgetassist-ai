BudgetAssist AI

Development scaffold for BudgetAssist AI. This repository contains a minimal skeleton for:

- backend: FastAPI (Python) skeleton
- frontend: Vite + React + TypeScript + Tailwind skeleton
- docker-compose.yml for local development with supporting services (Postgres, Redis, Qdrant, MinIO, Ollama)

Quickstart

1. Copy `.env.example` to `.env` and update values.
2. Start everything for development:

   docker compose up --build

3. Backend: http://localhost:8000
4. Frontend: http://localhost:3000

Notes

This scaffold implements structural files only; no business logic is included. Add application code under backend/ and frontend/src/.
