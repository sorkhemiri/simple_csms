from fastapi import APIRouter

from api.endpoints.rate_endpoint import router as rate_router

main_router = APIRouter()
main_router.include_router(rate_router)
