from src.cart import Cart
from src.chargers import DistanceCharger
from src.interfaces import ISimpleFee
import pytest

@pytest.fixture
def cart():
    cart: Cart = Cart()
    cart.attach(DistanceCharger())
    yield cart
    cart._reset()


@pytest.fixture
def delivery_charge_borders():
    # "name": (delivery_distance, correct_charge)
    return {"minimum_fee": (300, 100), "first_1000m": (1000, 200), "distance_1499m": (1499, 300),
            "distance_1500m": (1500, 300), "distance_1501m": (1501, 400), "distance_1999m": (1999, 400),
            "distance_2000m": (2000, 400),"distance_2001m": (2001, 500), "distance_2499m": (2499, 500)}

class TestChargeDistance:
    
    def test_minimum_fee(self, cart: Cart, delivery_charge_borders: dict):
        cart.setCart(delivery_distance = delivery_charge_borders["minimum_fee"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == delivery_charge_borders["minimum_fee"][1]
    
    def test_first_1000m(self, cart: Cart, delivery_charge_borders: dict):
        cart.setCart(delivery_distance = delivery_charge_borders["first_1000m"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == delivery_charge_borders["first_1000m"][1]
    
    def test_distance_1499m(self, cart: Cart, delivery_charge_borders: dict):
        cart.setCart(delivery_distance = delivery_charge_borders["distance_1499m"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == delivery_charge_borders["distance_1499m"][1]
    
    def test_distance_1500m(self, cart: Cart, delivery_charge_borders: dict):
        cart.setCart(delivery_distance = delivery_charge_borders["distance_1500m"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == delivery_charge_borders["distance_1500m"][1]
    
    def test_distance_1501m(self, cart: Cart, delivery_charge_borders: dict):
        cart.setCart(delivery_distance = delivery_charge_borders["distance_1501m"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == delivery_charge_borders["distance_1501m"][1]
    
    def test_distance_1999m(self, cart: Cart, delivery_charge_borders: dict):
        cart.setCart(delivery_distance = delivery_charge_borders["distance_1999m"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == delivery_charge_borders["distance_1999m"][1]
    
    def test_distance_2000m(self, cart: Cart, delivery_charge_borders: dict):
        cart.setCart(delivery_distance = delivery_charge_borders["distance_2000m"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == delivery_charge_borders["distance_2000m"][1]

    def test_distance_2001m(self, cart: Cart, delivery_charge_borders: dict):
        cart.setCart(delivery_distance = delivery_charge_borders["distance_2001m"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == delivery_charge_borders["distance_2001m"][1]
    
    # I expect the 1 eur per 500 meters requirement to continue
    def test_distance_2499m(self, cart: Cart, delivery_charge_borders: dict):
        cart.setCart(delivery_distance = delivery_charge_borders["distance_2499m"][0])
        fee: ISimpleFee = cart.fee
        assert fee.fee == delivery_charge_borders["distance_2499m"][1]
