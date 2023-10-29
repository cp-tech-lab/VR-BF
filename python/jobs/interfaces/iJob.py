from abc import ABC, abstractmethod

class IJob(ABC):

    @abstractmethod
    def run(self, *args):
        pass
    