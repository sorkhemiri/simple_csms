from pydantic import BaseModel

from .cdr_validator import CDRValidator
from .rate_validator import RateValidator


class RateEndpointValidator(BaseModel):
    """
    takes values of cdr coming to the endpoint
    and validates them based on the logic
    """
    cdr: CDRValidator
    rate: RateValidator
