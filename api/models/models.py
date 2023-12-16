from sqlalchemy import Boolean, Column, Integer, String

from api.database import Base, engine


class User(Base):
    __tablename__ = "registered_users"

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100), nullable=False)
    is_enabled = Column(Boolean, default=True)


Base.metadata.create_all(engine, checkfirst=True)
