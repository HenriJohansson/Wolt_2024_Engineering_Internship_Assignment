from src.cart import Cart
from src.interfaces.simple_fee import ISimpleFee
from src.chargers import ValueCharger, ItemCharger , DistanceCharger ,TimeCharger
import pytest

@pytest.fixture
def cart():
    cart: Cart = Cart()
    cart.attach(ValueCharger())
    cart.attach(ItemCharger())
    cart.attach(DistanceCharger())
    cart.attach(TimeCharger())
    yield cart
    cart._reset()

@pytest.fixture
def free_delivery():
    return {"cart_value": 20000, "total_delivery_fee": 0 }
    
def test_item_free_delivery(free_delivery: dict, cart: Cart):
    cart.setCart(value= free_delivery["cart_value"] ,number_of_items=14)
    fee: ISimpleFee = cart.fee
    assert fee.fee == free_delivery["total_delivery_fee"]

def test__fully_integration_free_delivery(free_delivery: dict, cart: Cart):
    cart.setCart(
        free_delivery["cart_value"], 2499, 14, "2024-02-23T18:59:30Z"
    )
    fee: ISimpleFee = cart.fee
    assert fee.fee == free_delivery["total_delivery_fee"]


def test__time_free_delivery(free_delivery: dict, cart: Cart):
    fee: ISimpleFee = cart.fee
    fee.cumulate_to_fee(1000) # Artificially stimulate fee to test time multiplier
    cart.setCart(value = free_delivery["cart_value"],
                 time = "2024-02-23T18:59:30Z")# It's friday rush hour * 1,2 fee
    assert fee.fee == free_delivery["total_delivery_fee"]

def test_distance_free_delivery(free_delivery: dict, cart: Cart):
    cart.setCart(value = free_delivery["cart_value"], 
                 delivery_distance= 2499) #(2499 = 700 in fee)
    fee: ISimpleFee = cart.fee
    assert fee.fee == free_delivery["total_delivery_fee"]

def example_integration_test(cart: Cart):
    cart.setCart(790,2235,4,"2024-01-15T13:00:00Z")
    fee: ISimpleFee = cart.fee
    assert fee.fee == 710