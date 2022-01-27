from fastapi import APIRouter
from api.v1.endpoints.rate_endpoint import router as rate_router

router = APIRouter()
router.include_router(rate_router)
