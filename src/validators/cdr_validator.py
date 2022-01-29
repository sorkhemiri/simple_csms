from datetime import datetime
from decimal import Decimal

from fastapi import HTTPException
from pydantic import BaseModel, validator
from starlette.status import HTTP_400_BAD_REQUEST


class CDRValidator(BaseModel):
    meterStart: Decimal
    timestampStart: datetime
    meterStop: Decimal
    timestampStop: datetime

    @validator('meterStart', 'meterStop')
    def must_be_non_negative(cls, v):
        if not v >= 0:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="meterStart and meterStop must be non-negative"
                )
        return v

    def __init__(self, *args, **kwargs):
        super(CDRValidator, self).__init__(*args, **kwargs)
        if self.timestampStart > self.timestampStop:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="timestampStart must be less or equal to timestampStop"
            )
        if self.meterStart > self.meterStop:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="meterStart must be less or equal to meterStop"
            )
