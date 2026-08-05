from pydantic import BaseSettings

class Settings(BaseSettings):
    # Database
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "budgetassist"
    POSTGRES_USER: str = "app"
    POSTGRES_PASSWORD: str = "change_me"

    # Security
    SECRET_KEY: str = "replace-this-with-a-secret"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 30

    # Redis
    REDIS_URL: str = "redis://redis:6379/0"

    # Qdrant
    QDRANT_URL: str = "http://qdrant:6333"

    class Config:
        env_file = ".env"

settings = Settings()
