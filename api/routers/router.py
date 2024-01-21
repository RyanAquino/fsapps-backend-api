from fastapi import APIRouter

from api.routers import user_token
from api.routers.dts_tables import dts_tables_all
from api.routers.dts_tables import dts_tables_fyear

api_router = APIRouter()

api_router.include_router(user_token.router, prefix="/auth")
api_router.include_router(dts_tables_all.router, prefix="/dts_tables_all")
api_router.include_router(dts_tables_fyear.router, prefix="/dts_tables_fyear")
