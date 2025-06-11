import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    mysql_user: str
    mysql_password: str
    mysql_host: str
    mysql_port: int
    mysql_db: str
    app_host: str = "0.0.0.0"
    app_port: int = 8003

    class Config:
        env_file = ".env"

settings = Settings()