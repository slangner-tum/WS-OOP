from enum import Enum


class _CarStatus(Enum):
    STOPPED = 0
    STARTED = 1
    DRIVING = 2


class _Weather(Enum):
    CLEAR = 0
    RAIN = 1
    SNOW = 2
