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
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/auth/login")


class UserOperations:
    @staticmethod
    # Get request user if available in the database
    def get_request_user(username: str, db: Session = next(get_db())):
        db_user = crud.access_user.get_user_by_username(db, username=username)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user

    @staticmethod
    # Verify if given password is equal to the hashed password given
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    # Hash the given plain password
    def get_password_hash(plain_password):
        return pwd_context.hash(plain_password)

    # Checks the given password and username if it is registered in the database
    def authenticate_user(self, username: str, password: str):
        user = self.get_request_user(username)
        if not user:
            return False
        if not self.verify_password(password, user["hashed_password"]):
            return False
        return user

    @staticmethod
    # Create JWT token with an expiry based on the given data
    def create_access_token(data: dict, expires_delta: timedelta or None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + timedelta(minutes=expires_delta)
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm="HS256")
        return encoded_jwt

    # Check the given token if the details are matched in the database
    def get_current_user(self, token: str = Depends(oauth2_scheme)):
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

    @staticmethod
    # Check if the user token is expired or not
    def get_current_active_user(current_user: schemas.User = get_request_user):
        if not current_user.enabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return


user_operations = UserOperations()
