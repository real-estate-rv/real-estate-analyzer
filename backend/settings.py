from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://invest_user:secure_password@postgres:5432/real_estate"
    REDIS_URL: str = "redis://redis:6379/0"
    TIMEZONE: str = "Asia/Jerusalem"
    DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
