from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MY_ENV_VAR: str

settings = Settings()
