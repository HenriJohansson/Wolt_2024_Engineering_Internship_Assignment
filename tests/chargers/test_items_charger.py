from src.cart import Cart
from src.chargers import ItemCharger
from src.utils import IntWrapper
from src.interfaces import ISimpleFee
import pytest

@pytest.fixture
def cart():
    IntWrapper(0)
    cart: Cart = Cart()
    cart.attach(ItemCharger())
    yield cart
    cart._reset()


@pytest.fixture
def item_charge_borders():
    # "name": (items, correct_charge)
    return {"no_sur_charge": (4, 0), "5_or_more_1": (5, 50), "5_or_more_2": (6, 50*2), "5_or_more_3": (9, 50*5),
            "10_or_more_1": (10, 50*6), "10_or_more_2": (11, 50*7), "10_or_more_3": (12, 50*8),
            "13_exactly": (13, 50*9 + 120), "14_exactly": (14, 50*10 + 120)}

class TestChargeItems:

    def test_no_sur_charge(self, cart: Cart, item_charge_borders: dict):
        cart.setCart(number_of_items = item_charge_borders["no_sur_charge"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == item_charge_borders["no_sur_charge"][1]

    def test_5_or_more_1(self, cart: Cart, item_charge_borders: dict):
        cart.setCart(number_of_items = item_charge_borders["5_or_more_1"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == item_charge_borders["5_or_more_1"][1]

    def test_5_or_more_2(self, cart: Cart, item_charge_borders: dict):
        cart.setCart(number_of_items = item_charge_borders["5_or_more_2"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == item_charge_borders["5_or_more_2"][1]

    def test_5_or_more_3(self, cart: Cart, item_charge_borders: dict):
        cart.setCart(number_of_items = item_charge_borders["5_or_more_3"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == item_charge_borders["5_or_more_3"][1]

    def test_10_or_more_1(self, cart: Cart, item_charge_borders: dict):
        cart.setCart(number_of_items = item_charge_borders["10_or_more_1"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == item_charge_borders["10_or_more_1"][1]

    def test_10_or_more_2(self, cart: Cart, item_charge_borders: dict):
        cart.setCart(number_of_items = item_charge_borders["10_or_more_2"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == item_charge_borders["10_or_more_2"][1]

    def test_10_or_more_3(self, cart: Cart, item_charge_borders: dict):
        cart.setCart(number_of_items = item_charge_borders["10_or_more_3"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == item_charge_borders["10_or_more_3"][1]

    def test_13_exactly(self, cart: Cart, item_charge_borders: dict):
        cart.setCart(number_of_items = item_charge_borders["13_exactly"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == item_charge_borders["13_exactly"][1]

    def test_14_exactly(self, cart: Cart, item_charge_borders: dict):
        cart.setCart(number_of_items = item_charge_borders["14_exactly"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == item_charge_borders["14_exactly"][1]

