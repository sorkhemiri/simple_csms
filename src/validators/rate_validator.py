from decimal import Decimal

from fastapi import HTTPException
from pydantic import BaseModel, validator
from starlette.status import HTTP_400_BAD_REQUEST


class RateValidator(BaseModel):
    """
    RATE validator takes rate values coming to the end
    point and validates the rating values
    """
    energy: Decimal
    time: Decimal
    transaction: Decimal

    @validator('energy', 'time', 'transaction')
    def must_be_non_negative(cls, v):
        """
        checks if field value is non-negative
        :param v: field value
        :return:
        """
        if not v >= 0:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="meterStart and meterStop must be non-negative"
            )
        return v
