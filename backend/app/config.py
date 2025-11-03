from pydantic_settings import BaseSettings

from dataclasses import dataclass

@dataclass
class Settings:
    title: str


class Config(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int

    @property
    def DATABASE_URL(self,) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
config = Config()