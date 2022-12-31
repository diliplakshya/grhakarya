from pydantic import BaseSettings


class Settings(BaseSettings):
    aws_dynamo_db:bool = True # default value if env variable does not exist
    db_url:str
    aws_region: str
    aws_access_key_id: str
    aws_secret_access_key: str

    class Config:
        env_file = ".env"

settings = Settings()