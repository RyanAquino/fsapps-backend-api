from sqlalchemy.orm import Session
from api.models import models
from api.schemas import schemas


class AccessUser:
    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    @staticmethod
    def get_user_by_username(db: Session, username: str):
        return db.query(models.User).filter(models.User.username == username).first()

    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.User).offset(skip).limit(limit).all()

    @staticmethod
    def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
        db_user = models.User(email=user.email, hashed_password=hashed_password, is_enabled=True)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


access_user = AccessUser()
