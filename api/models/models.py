from sqlalchemy import Boolean, Column, Integer, String

from api.database import Base


class User(Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = "registered_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100), nullable=False)
    is_enabled = Column(Boolean, default=True)
