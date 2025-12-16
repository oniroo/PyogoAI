from hardwares.enums import ActuatorType
from hardwares.interfaces.Actuator import Actuator


class Fan(Actuator):
    def __init__(self, pin: int=35):
        super().__init__(pin)
        self._type = ActuatorType.FAN

    def on_activate(self):
        print("Fan ON")

    def on_deactivate(self):
        print("Fan OFF")
