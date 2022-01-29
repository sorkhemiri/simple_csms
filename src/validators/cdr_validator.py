from datetime import datetime
from decimal import Decimal

from fastapi import HTTPException
from pydantic import BaseModel, validator
from starlette.status import HTTP_400_BAD_REQUEST


class CDRValidator(BaseModel):
    """
    CDR validator takes values of cdr coming to the end
    point and validates the values of the CDR
    """
    meterStart: Decimal
    timestampStart: datetime
    meterStop: Decimal
    timestampStop: datetime

    @validator('meterStart', 'meterStop')
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

    def __init__(self, *args, **kwargs):
        super(CDRValidator, self).__init__(*args, **kwargs)
        # checking if stop time is after the start time
        if self.timestampStart > self.timestampStop:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="timestampStart must be less or equal to timestampStop"
            )
        # checking is meter stop value is more than meter start value
        if self.meterStart > self.meterStop:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="meterStart must be less or equal to meterStop"
            )
