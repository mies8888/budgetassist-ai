Alembic scaffolding (minimal)

Usage:
1. Update backend models and ensure `target_metadata` in env.py points to your Base.metadata
2. Create revision:
   alembic -c backend/alembic.ini revision --autogenerate -m "create tables"
3. Apply migrations:
   alembic -c backend/alembic.ini upgrade head

This env is configured for async SQLAlchemy (asyncpg). Adjust as project models are added.
