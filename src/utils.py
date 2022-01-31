from datetime import datetime
from decimal import Decimal

from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

async def total_energy_calculator(meter_start: Decimal, meter_stop: Decimal) -> Decimal:
    """
    takes start and stop of energy meter and calculates
    the total energy used in kwh
    :param meter_start: energy meter start
    :type meter_start: Decimal
    :param meter_stop: energy meter stop
    :type meter_stop: Decimal
    :return: total used energy in kwh
    """
    if meter_stop < meter_start:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="meterStart must be less or equal to meterStop",
        )
    if meter_stop < 0 or meter_start < 0:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="meterStart and meterStop must be non-negative",
        )
    return (meter_stop - meter_start) / Decimal(1000)

async def total_spent_time_calculator(start_time: datetime, stop_time: datetime):
    """
    takes start and stop time of charge and calculates
    total time spent in hours.
    :param start_time: start of charge time
    :type start_time: datetime
    :param stop_time: stop of charge time
    :type stop_time: datetime
    :return:
    """
    if start_time > stop_time:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="timestampStart must be less or equal to timestampStop",
        )
    total_time = stop_time - start_time
    return Decimal(total_time.total_seconds()) / Decimal(3600)
