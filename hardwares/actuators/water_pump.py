from hardwares.enums import ActuatorType
from hardwares.interfaces.Actuator import Actuator


class WaterPump(Actuator):
    def __init__(self, pin: int=35):
        super().__init__(pin)
        self._type = ActuatorType.WATER_PUMP

    def on_activate(self):
        print("Pump ON")

    def on_deactivate(self):
        print("Pump OFF")