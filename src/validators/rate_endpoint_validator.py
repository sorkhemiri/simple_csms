from pydantic import BaseModel

from .cdr_validator import CDRValidator
from .rate_validator import RateValidator

class RateEndpointValidator(BaseModel):
    cdr: CDRValidator
    rate: RateValidator
