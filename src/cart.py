from src.interfaces import ICartObserver, ICartSubject, ISimpleFee
from src.utils.primitive_wrappers import IntWrapper
from src.utils.time import Time
from src.delivery_fee import DeliveryFeeCalculator
from typing import List

class Cart(ICartSubject):

    def __init__(self):
        self._value = IntWrapper(0)
        self._fee = DeliveryFeeCalculator(self._value)
        self._items: int = 0
        self._delivery_distance: int = 0
        self._time: Time = Time()

    @property
    def value(self) -> int:
        return self._value.value

    @property
    def items(self) -> int:
        return self._items

    @property
    def delivery_distance(self) -> int:
        return self._delivery_distance

    @property
    def time(self) -> Time:
        return self._time
    
    @property
    def fee(self) -> ISimpleFee:
        return self._fee
    
    def setCart(self, value: int = 0, delivery_distance: int = 0, number_of_items: int = 0, time: str = Time().get_default_time()) -> None:
        self._value.value = value
        self._delivery_distance = delivery_distance
        self._items = number_of_items
        self._time = Time(time)
        self.notify()

    _observers: List[ICartObserver] = []
    
    """
    Subject Interface filled functions
    """
    def attach(self, observer: ICartObserver) -> None:
        self._observers.append(observer)

    def detach(self, observer: ICartObserver) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def _reset(self):
        """
        Brings Cart back to its innitial state
        handy for testing
        """
        self._items = 0
        self._value = IntWrapper(0)
        self._delivery_distance = 0
        self._time = Time()
        self._observers.clear()
        self._fee = DeliveryFeeCalculator(self._value)