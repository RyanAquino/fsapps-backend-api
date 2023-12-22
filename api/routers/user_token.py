from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from api.schemas import schemas
from api.config import settings
from api.user_dependencies import user_operations

router1 = APIRouter()


# Path used in creating the access token of the logged-in user
@router1.post("/v1/auth/login", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_operations.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password",
                            headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = user_operations.create_access_token(user, access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
