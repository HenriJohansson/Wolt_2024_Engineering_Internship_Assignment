from src.interfaces.observer_pattern import Subject
from src.interfaces.simple_fee import ISimpleFee
from src.utils.time import Time
from abc import abstractmethod

class ICartSubject(Subject):

    @property
    @abstractmethod
    def value(self) -> int:
        ...

    @property
    @abstractmethod
    def items(self) -> int:
        ...

    @property
    @abstractmethod
    def delivery_distance(self) -> int:
        ...

    @property
    @abstractmethod
    def time(self) -> Time:
        ...

    @property
    @abstractmethod
    def fee(self) -> ISimpleFee:
        "Return the fee calculator"
        ...
    
    @abstractmethod
    def setCart(self, value: int = 0, delivery_distance: int = 0, number_of_items: int = 0, time: Time = Time()) -> None:
        "Fill the cart with all the information at ones"
        ...