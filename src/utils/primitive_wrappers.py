from src.interfaces.simple_fee import Iint

class IntWrapper(Iint):
    def __init__(self, value: int = 0,) -> None:
        self._value = value
    
    @property
    def value(self) -> int:
        return self._value
        
    @value.setter
    def value(self, value: int) -> None:
        self._value = value
