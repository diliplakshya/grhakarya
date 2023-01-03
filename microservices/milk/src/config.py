from pydantic import BaseSettings


class Settings(BaseSettings):
    aws_dynamo_db:bool = True # default value if env variable does not exist
    db_url:str = None
    aws_region: str = None
    aws_access_key_id: str = None
    aws_secret_access_key: str = None
    secret_key: str = None
    algorithm: str = None
    access_token_expire_minutes: int = None
    hashed_password: str = None

    class Config:
        env_file = ".env"

settings = Settings()