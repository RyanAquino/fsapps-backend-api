from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from config import settings
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from api.crud import crud
from schemas import schemas

from api.database import SessionLocal


# Dependency
def init_db():
    """Initialize the db generator"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserOperations:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/auth/login")
        self.db = next(init_db())

    def get_request_user(self, username: str):
        """Get the user information from the database using username"""
        db_user = crud.access_user.get_user_by_username(self.db, username=username)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user

    def verify_password(self, plain_password, hashed_password):
        """Check if the given password for the user is correct"""
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, plain_password):
        """Hash the given plain password"""
        return self.pwd_context.hash(plain_password)

    def authenticate_user(self, username: str, password: str):
        """Check if the user is registered in the database"""
        user = self.get_request_user(username)
        user = dict(username=user.username,
                    hashed_password=user.hashed_password,
                    is_enabled=user.is_enabled)
        if not user:
            return False
        if not self.verify_password(password, user["hashed_password"]):
            return False
        return user

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta or None = None):
        """Create a JWT token with expiry"""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm="HS256")
        return encoded_jwt

    def get_current_user(self):
        """Get the current logged-in user and check if it is authenticated"""
        token: str = Depends(self.oauth2_scheme)
        credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                             detail="Could not validate credentials",
                                             headers={"WWW-Authenticate": "Bearer"})
        try:
            payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
            username: str = payload.get("username")
            if username is None:
                raise credential_exception

            token_data = schemas.TokenData(username=username)
        except JWTError:
            raise credential_exception

        user = self.get_request_user(username=token_data.username)
        if user is None:
            raise credential_exception

        return user

    def get_current_active_user(self):
        """Check if the token of the logged-in user is still active"""
        current_user: schemas.User = self.get_current_user()
        if not current_user.enabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return


