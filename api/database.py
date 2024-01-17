from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from api.config import settings

engine = create_engine(
    f"mariadb+mariadbconnector://{settings.database_username}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}"
    if not settings.database_url
    else settings.database_url
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
