from src.cart import Cart
from src.chargers import TimeCharger
from src.interfaces.simple_fee import ISimpleFee
import pytest

@pytest.fixture
def cart():
    cart: Cart = Cart()
    cart.attach(TimeCharger())
    yield cart
    cart._reset()


@pytest.fixture
def time_charge_borders():
    # "name": (time, base total , charge multiplier , resulting total)
    return {"no_charge_monday": ("2024-01-15T16:00:00Z", 1000, 0, 1000), "no_charge_friday_1": ("2024-01-19T13:00:00Z", 1000, 0, 1000), 
            "charge_friday_1": ("2024-02-09T15:01:00Z", 800, 1.2, 960), "charge_friday_2": ("2024-02-23T18:59:30Z", 1000, 1.2, 1200),
            "no_charge_saturday": ("2024-01-20T13:00:00Z", 500, 0, 500), "no_charge_friday_2": ("2024-01-19T19:00:00Z", 1000, 0, 1000)}

class TestChargeTime:
    """
    Test if Time affects the total delivery fee correctly
    """

    def test_no_charge_monday(self, cart: Cart, time_charge_borders: dict):
        fee: ISimpleFee = cart.fee
        fee.cumulate_to_fee(time_charge_borders["no_charge_monday"][1])
        cart.setCart(time = time_charge_borders["no_charge_monday"][0]) 
        assert fee.fee == time_charge_borders["no_charge_monday"][3]

    def test_no_charge_friday_1(self, cart: Cart, time_charge_borders: dict):
        fee: ISimpleFee = cart.fee
        fee.fee = time_charge_borders["no_charge_friday_1"][1]
        cart.setCart(time = time_charge_borders["no_charge_friday_1"][0]) 
        assert fee.fee == time_charge_borders["no_charge_friday_1"][3]

    def test_charge_friday_1(self, cart: Cart, time_charge_borders: dict):
        fee: ISimpleFee = cart.fee
        fee.fee = time_charge_borders["charge_friday_1"][1]
        cart.setCart(time = time_charge_borders["charge_friday_1"][0]) 
        assert fee.fee == time_charge_borders["charge_friday_1"][3]

    def test_(self, cart: Cart, time_charge_borders: dict):
        fee: ISimpleFee = cart.fee
        fee.cumulate_to_fee(time_charge_borders["charge_friday_2"][1])
        cart.setCart(time = time_charge_borders["charge_friday_2"][0]) 
        assert fee.fee == time_charge_borders["charge_friday_2"][3]

    def test_no_charge_saturday(self, cart: Cart, time_charge_borders: dict):
        fee: ISimpleFee = cart.fee
        fee.fee = time_charge_borders["no_charge_saturday"][1]
        cart.setCart(time = time_charge_borders["no_charge_saturday"][0]) 
        assert fee.fee == time_charge_borders["no_charge_saturday"][3]

    def test_no_charge_friday_2(self, cart: Cart, time_charge_borders: dict):
        fee: ISimpleFee = cart.fee
        fee.cumulate_to_fee(time_charge_borders["no_charge_friday_2"][1])
        cart.setCart(time = time_charge_borders["no_charge_friday_2"][0]) 
        assert fee.fee == time_charge_borders["no_charge_friday_2"][3]

