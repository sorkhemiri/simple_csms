from fastapi import APIRouter

from api.v1 import api_v1_router


main_router = APIRouter()
main_router.include_router(api_v1_router, prefix="/api/v1.0")
