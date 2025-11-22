r"""
로직
1. 일정 주기로 환경 체크, 데이터 저장: 비동기
2. 실행 조건: 비동기 확인 -> 실행 or 멈추기
"""
from abc import ABC, abstractmethod

class BaseActivator(ABC):
    codition: bool # 실행 조건

    def __init__(self, condition):
        self.condition = condition

    @abstractmethod
    def activate(self):
        raise NotImplementedError

    @abstractmethod
    def deactivate(self):
        raise NotImplementedError

    def automate(self):
        if self.condition:
            self.activate()
        else:
            self.deactivate()