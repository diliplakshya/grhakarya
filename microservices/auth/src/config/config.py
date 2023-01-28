from pydantic import BaseSettings


class Settings(BaseSettings):
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
