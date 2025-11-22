from hardware.actuator.base_activator import BaseActivator

class WaterPumpActivator(BaseActivator):
    is_activated: bool = False
    waterable_condition: bool = None # 습도 조건 or AI 판단

    def __init__(self, waterable_condition: bool):
        self.waterable_condition = waterable_condition
        super().__init__(waterable_condition)

        if self.waterable_condition is not None:
            self.automate()
        else:
            raise ValueError("The Water Pump Activator must have waterable_condition")

    def activate(self):
        print(f"Should activate water pump: {self.waterable_condition}")
        print("Activating water pump...")
        # 센서 연결하고 실제 로직 추가
        self.is_activated = True

    def deactivate(self):
        print(f"Should activate water pump: {self.waterable_condition}")
        print("Deactivating water pump...")
        # 센서 연결하고 실제 로직 추가
        self.is_activated = False