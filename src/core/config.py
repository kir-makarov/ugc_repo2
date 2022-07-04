import os
from pydantic import BaseSettings


class Base(BaseSettings):
    class Config:
        env_file = '.env.sample'
        env_file_encoding = 'utf-8'
        arbitrary_types_allowed = True


class Settings(Base):
    PROJECT_NAME: str = os.getenv('PROJECT_NAME', 'UGC')
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    AUTH_VALIDATION_URL: str = os.getenv('AUTH_URL', 'http://auth:83') + "/validate"

    MONGO_USER = os.getenv("MONGO_USER", "team2")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "team2")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "movies")
    MONGO_HOSTS = os.getenv("MONGO_HOSTS", "localhost")
    MONGO_CONNECT_URI_TEMPLATE = os.getenv('MONGO_CONNECT_URI_TEMPLATE',
                                           "mongodb://{user}:{pw}@{hosts}/{db}?retryWrites=true&w=majority")
    MONGO_CONNECT_URI = MONGO_CONNECT_URI_TEMPLATE.format(
        user=f"{MONGO_USER}",
        pw=f"{MONGO_PASSWORD}",
        hosts=MONGO_HOSTS,
        db=MONGO_DB_NAME
    )


settings = Settings()
