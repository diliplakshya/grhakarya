from pydantic import BaseSettings


class Settings(BaseSettings):
    host = None

    class Config:
        env_file = ".env"

settings = Settings()
