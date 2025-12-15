import asyncio

from hardwares.sensors import TemperatureAndHumidity


async def main():
    temp_hum_sensor = TemperatureAndHumidity()

    try:
        while True:
            data = await temp_hum_sensor.read
            print(data)
            await asyncio.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping sensor loop...")

    finally:
        temp_hum_sensor.disable()
        print("Sensor disabled and I2C bus closed.")


if __name__ == "__main__":
    asyncio.run(main())