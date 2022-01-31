import os

from pydantic import BaseSettings

# path to src directory
SOURCE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path to base directory
BASE_DIR = os.path.dirname(SOURCE_DIR)


class Config(BaseSettings):
    """
    config is used for project's general configurations
    the values of the variables will overwrite from .env
    file in the base directory if present and will set the
    the default values if not present.
    note: this functionality is NOT case sensitive
    """
    debug: bool = True
    # SWAGGER CONFIG
    app_title: str = "CSMS"
    app_description: str = "simple rating API for CSMS system"
    app_version: str = "0.1.0"

    # AUTHORIZATION
    api_key_secret: str = \
        "e5720f7032fed2478c57b3f6a87a175a250806e3afba74fa15e5bc84032176d1"
    api_key_name: str = "X_ACCESS_KEY"

    # EXPOSED PORT
    exposed_port: int = 8000

    class Config:
        case_sensitive = False
        # WHERE TO FIND PROJECT .env File
        env_file = os.path.join(BASE_DIR, ".env")
        env_file_encoding = "utf-8"


env_config = Config()
