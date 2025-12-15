from enum import Enum

class SensorType(str, Enum):
    TEMPERATURE_HUMIDITY = "SHT31"
    CO2 = "MH-Z19C"