from abc import ABC, abstractmethod

class Iint(ABC):

    def __init__(self, value: int = 0,) -> None:
        ...
    
    @property
    @abstractmethod
    def value(self) -> int:
        ...
    @value.setter
    @abstractmethod
    def value(self, value: int) -> None:
        ...
