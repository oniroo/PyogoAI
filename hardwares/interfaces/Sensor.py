from abc import ABC, abstractmethod


class Sensor(ABC):
    @abstractmethod
    def read(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def save(self):
        raise NotImplementedError

    @abstractmethod
    def load(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def enable(self):
        raise NotImplementedError

    @abstractmethod
    def disable(self):
        raise NotImplementedError