from datetime import datetime
from decimal import Decimal


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
    total_time = stop_time - start_time
    return Decimal(total_time.total_seconds()) / Decimal(3600)
