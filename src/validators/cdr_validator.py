from datetime import datetime

from pydantic import BaseModel

class CDRValidator(BaseModel):
    meterStart: int
    timestampStart: datetime
    meterStop: int
    timestampStop: datetime
