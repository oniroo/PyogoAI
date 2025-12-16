from abc import ABC, abstractmethod

from Jetson import GPIO


# noinspection PyTypeChecker
class Actuator(ABC):
    def __init__(self, pin: int, active_high: bool = True, initial_state: bool = False):
        self.pin = pin
        self.active_high = active_high

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

        self._state = initial_state
        GPIO.output(self.pin, self._convert_state(initial_state))

    def _convert_state(self, state: bool):
        """논리 상태 -> 실제 GPIO 출력"""
        return GPIO.HIGH if (state == self.active_high) else GPIO.LOW

    def activate(self):
        self._state = True
        GPIO.output(self.pin, self._convert_state(self._state))
        self.on_activate()

    def deactivate(self):
        self._state = False
        GPIO.output(self.pin, self._convert_state(self._state))
        self.on_deactivate()

    @abstractmethod
    def on_activate(self):
        raise NotImplementedError

    @abstractmethod
    def on_deactivate(self):
        raise NotImplementedError

    def cleanup(self):
        GPIO.cleanup(self.pin)