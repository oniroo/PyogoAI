import time
import asyncio
from smbus2 import SMBus

from hardwares.interfaces.Sensor import Sensor
from hardwares.enums import SensorType
from hardwares.sensors.utils.json_save_load import save_json, load_json

I2C_BUS = 1
SHT31_ADDRESS = 0x44


class TemperatureAndHumidity(Sensor):
    def __init__(self):
        self.type = SensorType.TEMPERATURE_HUMIDITY
        self.enabled = False
        self.bus = None

    def enable(self):
        if self.bus is None:
            self.bus = SMBus(I2C_BUS)
        self.enabled = True

    def disable(self):
        if self.bus is not None:
            self.bus.close()
            self.bus = None
        self.enabled = False

    async def read(self) -> dict:
        """
        Reads temperature and humidity from SHT31 sensor via I2C.
        Blocking I2C operations are offloaded to a thread executor.
        """
        if not self.enabled:
            self.enable()

        loop = asyncio.get_running_loop()

        await loop.run_in_executor(
            None,
            self.bus.write_i2c_block_data,
            SHT31_ADDRESS,
            0x24,
            [0x00]
        )

        await asyncio.sleep(0.015)

        data = await loop.run_in_executor(
            None,
            self.bus.read_i2c_block_data,
            SHT31_ADDRESS,
            0x00,
            6
        )

        raw_temperature = (data[0] << 8) | data[1]
        raw_humidity = (data[3] << 8) | data[4]

        temperature = -45 + 175 * (raw_temperature / 65535.0)
        humidity = 100 * (raw_humidity / 65535.0)

        return {
            "temperature": round(temperature, 2),
            "humidity_percent": round(humidity, 2),
            "timestamp": time.time()
        }

    async def save(self):
        data = await self.read()
        save_json(sensor_type=self.type, sensor_data=data)

    def load(self) -> dict:
        return load_json(sensor_type=self.type)