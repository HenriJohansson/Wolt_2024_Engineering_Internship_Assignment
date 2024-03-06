from src.cart import Cart
from src.chargers import ValueCharger
from src.interfaces.simple_fee import ISimpleFee
import pytest

@pytest.fixture
def cart():
    cart = Cart()
    cart.attach(ValueCharger())
    yield cart
    cart._reset()

@pytest.fixture
def value_charge_borders():
    # "name": (cart_value, correct_charge)
    return {"less_than_10e_1": (999, 1), "less_than_10e_2": (1, 999), "less_than_10e_3": (510, 490),
             "exactly_10e":(1000, 0), "more_than_10e": (1430, 0)}

class TestChargeValue:
    def test_less_than_10e_1(self, cart: Cart ,value_charge_borders: dict):
        cart.setCart(value = value_charge_borders["less_than_10e_1"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == value_charge_borders["less_than_10e_1"][1]
        
    def test_less_than_10e_2(self, cart: Cart ,value_charge_borders: dict):
        cart.setCart(value = value_charge_borders["less_than_10e_2"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == value_charge_borders["less_than_10e_2"][1]

    def test_less_than_10e_3(self, cart: Cart ,value_charge_borders: dict):
        cart.setCart(value = value_charge_borders["less_than_10e_3"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == value_charge_borders["less_than_10e_3"][1]

    def test_exactly_10e(self, cart: Cart ,value_charge_borders: dict):
        cart.setCart(value = value_charge_borders["exactly_10e"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == value_charge_borders["exactly_10e"][1]
    
    def test_more_than_10e(self, cart: Cart ,value_charge_borders: dict):
        cart.setCart(value = value_charge_borders["more_than_10e"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == value_charge_borders["more_than_10e"][1]