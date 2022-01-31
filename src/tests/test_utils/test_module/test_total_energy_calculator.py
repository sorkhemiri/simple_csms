from decimal import Decimal

import pytest
from fastapi import HTTPException

from utils import total_energy_calculator

class TotalEnergyCalculatorTestCase:
    @staticmethod
    @pytest.mark.asyncio
    async def test_testcase_result():
        result = await total_energy_calculator(
            meter_start=Decimal(1204307), meter_stop=Decimal(1215230)
        )
        assert 10.923 == float(result)
    @staticmethod
    @pytest.mark.asyncio
    async def test_start_meter_gt_stop_meter():
        with pytest.raises(HTTPException):
            await total_energy_calculator(
                meter_start=Decimal(1215230), meter_stop=Decimal(1204307)
            )
    @staticmethod
    @pytest.mark.asyncio
    async def test_negative_values():
        with pytest.raises(HTTPException):
            await total_energy_calculator(
                meter_start=Decimal(-1215230), meter_stop=Decimal(1204307)
            )
        with pytest.raises(HTTPException):
            await total_energy_calculator(
                meter_start=Decimal(1215230), meter_stop=Decimal(-1204307)
            )
