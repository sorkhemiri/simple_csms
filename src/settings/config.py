import os

from pydantic import BaseSettings

SOURCE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(SOURCE_DIR)


class Config(BaseSettings):
    debug: bool = True
    # SWAGGER CONFIG
    app_title: str = "CSMS"
    app_description: str = "simple rating API for CSMS system"
    app_version: str = "0.1.0"

    exposed_port: int = 8000

    class Config:
        case_sensitive = False
        env_file = os.path.join(BASE_DIR, ".env")
        env_file_encoding = "utf-8"


env_config = Config()
