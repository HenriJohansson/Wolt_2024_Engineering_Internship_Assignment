from src.interfaces.simple_fee import ISimpleFee, Iint

class DeliveryFeeCalculator(ISimpleFee):

    def __init__(self, value: Iint):
        self._cart_value: Iint = value
        self._multiplier: float = 1.0
        self._fee: int = 0

    @property
    def multiplier(self) -> float:
        return self._multiplier

    @property
    def fee(self) -> int:
        """
        A getter for fee
        value over 20000 of the cart makes the fee 0 (free delivery)

        if limit is hit returns only the limited amount (max fee)
        """
        
        value_for_free_delivery = 20000
        limit = 1500

        if self._cart_value.value >= value_for_free_delivery:
            return 0
        
        if int(self._fee * self._multiplier) > limit:
            return limit
        
        return int(self._fee * self._multiplier)
    
    @multiplier.setter
    def multiplier(self, value: float) -> None:
        self._multiplier = value
    
    @fee.setter
    def fee(self, fee: int) -> None:
        self._fee = fee

    def cumulate_to_fee(self, new_fee: int) -> None:
        self._fee += new_fee