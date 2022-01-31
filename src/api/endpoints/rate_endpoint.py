from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKey
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK

from authorizarion import check_authorization
from utils import total_energy_calculator, total_spent_time_calculator
from validators import RateEndpointValidator

router = APIRouter()


@router.post("/rate", tags=["rating"])
async def rate_endpoint(
    request: Request,
    request_data: RateEndpointValidator,
    api_key: APIKey = Depends(check_authorization),
):
    rate = request_data.rate
    cdr = request_data.cdr
    total_consumed_energy = await total_energy_calculator(
        meter_start=cdr.meterStart, meter_stop=cdr.meterStop
    )
    total_time_hours = await total_spent_time_calculator(
        start_time=cdr.timestampStart, stop_time=cdr.timestampStop
    )
    total_time_cost = round(total_time_hours * rate.time, 3)
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
