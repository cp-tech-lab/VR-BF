
from abc import ABC, abstractmethod


class IUnityClient(ABC):
    @abstractmethod
    def connect(self, host: str, port: int):
        pass