import uvicorn
from fastapi import FastAPI
from routers.user_token import router1
from config import settings

app = FastAPI()

app.include_router(router1, prefix="/v1/auth/login", tags=["User Token Router"])


if __name__ == "__main__":
    uvicorn.run("api.main:app",
                host=settings.host,
                port=settings.port,
                reload=settings.reload)
