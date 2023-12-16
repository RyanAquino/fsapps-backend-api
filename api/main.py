from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from functools import lru_cache

from database import SessionLocal, engine
from crud import crud
from models import models
from schemas import schemas
from . import config


@lru_cache
def get_settings():
    return config.Settings()


settings = get_settings()
SECRET_KEY = settings.secret_key
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_minutes

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Verify if given password is equal to the hashed password given
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# Hash the given plain password
def get_password_hash(password):
    return pwd_context.hash(password)


# # Get user in database using the username
# def get_user(username: str):
#     user_db_data = get_registered_user(init_db(), username)
#     if user_db_data is not None:
#         return UserInDB(username=user_db_data["username"],
#                         hashed_password=user_db_data["hashed_password"],
#                         enabled=user_db_data["enabled"])


# # Checks the given password and username if it is registered in the database
# def authenticate_user(username: str, password: str):
#     user = get_user(username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user
#
#
# # Create JWT token with an expiry based on the given data
# def create_access_token(data: dict, expires_delta: timedelta or None = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
#     return encoded_jwt
#
#
# # Check the given token if the details are matched in the database
# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                                          detail="Could not validate credentials",
#                                          headers={"WWW-Authenticate": "Bearer"})
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credential_exception
#
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credential_exception
#
#     user = get_user(username=token_data.username)
#     if user is None:
#         raise credential_exception
#
#     return user
#
#
# # Check if the user token is expired or not
# async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
#     if not current_user.enabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user
#
#
# # Path used in creating the access token of the logged-in user
# @app.post("/v1/auth/login", response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                             detail="Incorrect username or password",
#                             headers={"WWW-Authenticate": "Bearer"})
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(data={"sub": user.username},
#                                        expires_delta=access_token_expires)
#     return {"access_token": access_token, "token_type": "bearer"}
#
#
# # Sample path in checking if the token works
# @app.get("/users/me/")
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user
#
#
# # Sample path in returning json format data
# @app.get("/user/me/items")
# async def read_own_items(current_user: User = Depends(get_current_active_user)):
#     return [{"item_id": 1, "owner": current_user}]


# Creating a user
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    return crud.create_user(db=db, user=user, hashed_password=hashed_password)


# Get all users
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# Get a user using their username
@app.get("/users/{user_name}", response_model=schemas.User)
def read_user(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# starting code in registering user import register user from schema
# @app.post("/registering_user"):
# async def registering_user():
#     register_user(init_db(), username, hashed_password)
#     return "Registered"
