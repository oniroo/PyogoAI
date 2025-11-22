from hardware.actuator.base_activator import BaseActivator

class FanActivator(BaseActivator):
    is_activated: bool = None
    co2_condition: bool = None # 습도 조건 or AI 판단

    def __init__(self, co2_condition: bool):
        self.co2_condition = co2_condition
        super().__init__(co2_condition)

        if self.co2_condition is not None:
            self.automate()
        else:
            raise ValueError("Fan Activator must have co2_condition")

    def activate(self):
        print(f"Should ventilate: {self.co2_condition}")
        print("Activating ventilating...")
        # 센서 연결하고 실제 로직 추가
        self.is_activated = True

    def deactivate(self):
        print(f"Should ventilate: {self.co2_condition}")
        print("Deactivating ventilating...")
        # 센서 연결하고 실제 로직 추가
        self.is_activated = False