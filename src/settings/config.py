import os

from pydantic import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Config(BaseSettings):
    debug: bool = True
    app_title: str = "CORE"

    class Config:
        case_sensitive = False
        env_file = os.path.join(BASE_DIR, ".env")
        env_file_encoding = "utf-8"


env_config = Config()
