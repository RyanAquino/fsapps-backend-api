from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from functools import lru_cache
from api import config


@lru_cache
def get_settings():
    return config.Settings()


settings = get_settings()

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = settings.database_url

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(engine, checkfirst=True)
