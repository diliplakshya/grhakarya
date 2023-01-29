from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    log_config:str = None
    log_file_path:str = os.getcwd()

    mysql_host:str = None
    mysql_port:str = None
    mysql_database:str = None
    mysql_user: str = None
    mysql_root_password: str = None

    secret_key: str = None
    algorithm: str = None
    access_token_expire_minutes: int = None

    class Config:
        env_file = ".env"

settings = Settings()
