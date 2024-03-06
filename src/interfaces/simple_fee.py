from src.interfaces.primitive_wrapper import Iint
from abc import ABC, abstractmethod

class ISimpleFee(ABC):

    @abstractmethod
    def __init__(self, value: Iint) -> None:
        ...

    @property
    @abstractmethod
    def multiplier(self) -> float:
        ...

    @property
    @abstractmethod
    def fee(self) -> int:
        ...

    @multiplier.setter
    @abstractmethod
    def multiplier(self, arg: float) -> None:
        ...

    @fee.setter
    @abstractmethod
    def fee(self, arg: int) -> None:
        ...
    
    @abstractmethod
    def cumulate_to_fee(self, arg: int) -> None:
        ...