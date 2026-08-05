GitHub Repository Structure (Document 24)

This document describes the canonical repository layout for the BudgetAssist-AI project. Keep this structure minimal and focused on separation between services, docs and infra configuration.

Repository root

- .github/                 -> CI/CD workflows
- docs/                    -> Architecture and development documentation (25 docs)
- backend/                 -> Python backend (FastAPI)
  - core/                  -> configuration, DB, security and shared utilities
  - app/ or api/           -> application modules (not included in scaffold)
  - Dockerfile
  - requirements.txt
- frontend/                -> Vite + React + TypeScript frontend
  - src/
  - index.html
  - package.json
  - Dockerfile
- infra/                   -> optional IaC, deployment manifests (k8s, helm)
- docker-compose.yml       -> developer docker-compose to run all services locally
- .env.example             -> example environment variables
- README.md                -> Overview and quickstart
- tests/                   -> integration/unit tests

Notes

- Keep each service self-contained and avoid cross-service imports.
- CI workflows live in .github/workflows and should include linting, tests and build steps.
- docs/ must contain architecture blueprints and the development manual.

Refer to Document 25 for development and run instructions.
