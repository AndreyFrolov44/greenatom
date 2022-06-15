from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    MINIO_ROOT_USER: str
    MINIO_ROOT_PASSWORD: str
    # ACCESS_KEY: str
    # SECRET_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
