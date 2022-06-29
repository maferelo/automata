import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field(..., env="DATABASE_URL")


settings = Settings()
settings.db_url = settings.db_url.replace("postgres://", "postgresql://", 1)
for _ in range(500):
    print(settings.db_url)
