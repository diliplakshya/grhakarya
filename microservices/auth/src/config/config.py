"""
    Setting Module

    Environment variable based configuration module.
"""

from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    """
    Configuration Class.

    Configuration for auth API.
    All variables in class corresponds to environment variables in CAPITAL CASE.
    example: 'mysql_host' represents an environment variable by name 'MYSQL_HOST'.

    Parameters
    ----------
    BaseSettings : BaseSettings.
        Base Class for Settings
    """
    api_version:str = None
    api_title:str = None
    api_host:str = None
    api_port:int = None
    sphinx_directory:str = None

    log_config:str = "configuration/logging/dev_config.conf"
    log_file_path:str = "/app/logging.log"

    mysql_host:str = "mysql-db"
    mysql_port:str = "3306"
    mysql_database:str = "auth"
    mysql_user: str = "root"
    mysql_root_password: str = "root"

    secret_key: str = None
    algorithm: str = None
    access_token_expire_minutes: int = None

    class Config:
        env_file = ".env"

settings = Settings()
