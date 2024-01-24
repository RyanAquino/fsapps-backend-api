from fastapi import APIRouter

from api.routers import (user_token,
                         dts_tables)


api_router = APIRouter()

api_router.include_router(user_token.router, prefix="/auth")
api_router.include_router(dts_tables.router, prefix="/dts_tables")
