from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url:str # default value if env variable does not exist
    aws_region: str
    aws_access_key_id: str
    aws_secret_access_key: str

    class Config:
        env_file = ".env"

settings = Settings()