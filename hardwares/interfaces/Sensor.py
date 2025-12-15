from abc import ABC, abstractmethod


class Sensor(ABC):
    @abstractmethod
    async def read(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def save(self, data: dict):
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