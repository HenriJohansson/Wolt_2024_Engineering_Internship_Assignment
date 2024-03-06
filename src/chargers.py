#IMPORTANT this is a multiclass file.

#Imports defined infront of the class they are used in.

from src.interfaces import ICartSubject, ICartObserver

class ValueCharger(ICartObserver):
    """
    Charges for the cart value
    """
    def __init__(self) -> None:
        self._done: bool = False

    def update(self, cart: ICartSubject) -> None:
        if self._done == False:
            cart.fee.cumulate_to_fee(self._is_cart_too_cheap(cart.value))
            self._done = True

    def _is_cart_too_cheap(self, value: int) -> int:
        if value <= 1000:
            return 1000 - value
        return 0

class ItemCharger(ICartObserver):
    """
    Charges for the items on the cart
    """
    def __init__(self) -> None:
        self._done: bool = False

    def update(self, cart: ICartSubject) -> None:
        if self._done == False:
            cart.fee.cumulate_to_fee(self.charge_for_number_of_items(cart.items))
            self._done = True

    def charge_for_number_of_items(self, items: int) -> int:
        fee = 0
        if items > 4:
            #Remove 4 to include only additional items
            fee += (items - 4) * 50
            #Bulk surcharge
            if items > 12:
                fee += 120
        return fee

from math import ceil

class DistanceCharger(ICartObserver):
    """
    Charges for the distance the cart has been delivered.
    """
    def __init__(self) -> None:
        self._done: bool = False

    def update(self, cart: ICartSubject) -> None:
        if self._done == False:
            cart.fee.cumulate_to_fee(self.charge_for_distance(cart.delivery_distance))
            self._done = True

    def charge_for_distance(self, dist: int) -> int:
        fee = 100 #Minimum fee 1€

        #prevent divided by 0 error
        if dist == 0:
            return fee

        if dist >= 1000:
            #fee from first 1km
            fee = 200
        
        if dist > 1000:
            #remove the handled 1000m before iteration based on dist
            dist -= 1000
            #ceil to include barely under 500m distances
            dist_in_500m_intervals = ceil(dist / 500)
            for _ in range(dist_in_500m_intervals):
                fee += 100 #For each 500m add fee of 1€
                
        return fee

from datetime import datetime

class TimeCharger(ICartObserver):
    """
    Charges for the time the cart gets delivered.
    """
    def __init__(self) -> None:
        self._done: bool = False
    
    def update(self, cart: ICartSubject) -> None:
        if self._done == False:
            cart.fee.multiplier = self._calculate_rush_hour(cart.time.time)
            self._done = True

    def _calculate_rush_hour(self, time: datetime) -> float:
        if time.weekday() == 4:
            #Rush hour starts 15:00:00 and ends 19:00:00
            if time.hour >= 15 and time.hour < 19 :
                return 1.2
        return 1
