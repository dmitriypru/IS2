from pydantic import BaseSettings


class AppSettings(BaseSettings):
    # POSTGRES
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @property
    def postgres_url(self) -> str:
        return f"postgres://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"  # noqa pylint: disable=line-too-long

    class Config:
        env_file = ".env"


SETTINGS = AppSettings()
