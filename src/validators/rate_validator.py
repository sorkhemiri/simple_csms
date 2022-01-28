from decimal import Decimal

from pydantic import BaseModel


class RateValidator(BaseModel):
    energy: Decimal
    time: Decimal
    transaction: Decimal
