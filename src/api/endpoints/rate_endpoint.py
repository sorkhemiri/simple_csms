from decimal import Decimal

from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK

from validators import RateEndpointValidator

router = APIRouter()


@router.post("/rate", tags=["rating"])
async def rate_endpoint(request: Request, request_data: RateEndpointValidator):
    rate = request_data.rate
    cdr = request_data.cdr
    total_consumed_energy = (cdr.meterStop - cdr.meterStart) / Decimal(1000)
    total_time = cdr.timestampStop - cdr.timestampStart
    total_time_seconds = Decimal(total_time.total_seconds()) / Decimal(3600)
    total_time_cost = round(total_time_seconds * rate.time, 3)
    total_energy_cost = round(total_consumed_energy * rate.energy, 3)
    total_cost = round(total_energy_cost + total_time_cost + rate.transaction, 2)
    response_data = {
        "overall": float(total_cost),
        "components": {
            "energy": float(total_energy_cost),
            "time": float(total_time_cost),
            "transaction": float(rate.transaction),
        },
    }
    return JSONResponse(content=response_data, status_code=HTTP_200_OK)
