from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    project_name: str = 'dawits-buchi-app34'
    admin_email: str = 'admin@dawits-buchi-app34.com'
    secret_key: str

    class Config:
        env_file = '.env'
        case_sensitive = True


@lru_cache()
def get_settings():
    return Settings()
