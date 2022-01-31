from datetime import datetime
from decimal import Decimal

import pytest
from fastapi import HTTPException

from utils import total_spent_time_calculator

class TotalSpentTimeCalculatorTestCase:
    @staticmethod
    @pytest.mark.asyncio
    async def test_testcase_result():
        start_time = datetime.strptime("2021-04-05T10:04:00Z", "%Y-%m-%dT%H:%M:%SZ")
        stop_time = datetime.strptime("2021-04-05T11:27:00Z", "%Y-%m-%dT%H:%M:%SZ")
        result = await total_spent_time_calculator(
            start_time=start_time, stop_time=stop_time
        )
        test_value = Decimal(((1 * 60) + 23) / 60)
        assert round(test_value, 4) == round(result, 4)
    @staticmethod
    @pytest.mark.asyncio
    async def test_start_time_gt_stop_time():
        with pytest.raises(HTTPException):
            start_time = datetime.strptime("2021-04-05T11:27:00Z", "%Y-%m-%dT%H:%M:%SZ")
            stop_time = datetime.strptime("2021-04-05T10:04:00Z", "%Y-%m-%dT%H:%M:%SZ")
            await total_spent_time_calculator(
                start_time=start_time, stop_time=stop_time
            )
