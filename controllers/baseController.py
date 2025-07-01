from abc import ABC, abstractmethod

class baseController(ABC):
    @abstractmethod
    def run(self):
        pass
