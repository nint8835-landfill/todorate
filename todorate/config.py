from pydantic import BaseSettings


class Config(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    sqlalchemy_connection_url: str = "sqlite:///todorate.sqlite"


config = Config()

__all__ = ["config"]
