from src.cart import Cart
from tests.example_observer import ExampleObserver
from src.interfaces.simple_fee import ISimpleFee
from src.utils.time import Time
import pytest

#Define test requirements and classes before test class

@pytest.fixture(scope="function")
def cart():
    cart = Cart()
    return cart
    
@pytest.fixture(scope="session")
def used_observers():
    return [ExampleObserver(), ExampleObserver(), ExampleObserver(), ExampleObserver(), ExampleObserver(), ExampleObserver()]
@pytest.fixture(scope="function")
def cart_with_observer(cart: Cart, used_observers):
    cart.attach(used_observers[0])
    yield cart
    cart._reset()

class TestCart:
    
    def test_basic_init(self, cart):
        c: Cart = cart
        expected_output = {"value": 2000, "items": 20, "delivery_distance": 4000,
                           "time": str(Time('2024-01-19T13:00:00')), "total_delivery_fee": 0}
        c.setCart(expected_output["value"],
                  expected_output["delivery_distance"],
                  expected_output["items"],
                  expected_output["time"])
        cart_output = {"value": c._value.value, "items": c._items, "delivery_distance": c._delivery_distance,
                        "time": str(c._time), "total_delivery_fee": c.fee.fee}
        assert cart_output == expected_output
    
    def test_observers_get_added(self, cart_with_observer):
        c = cart_with_observer
        assert len(c._observers) == 1

    def test_more_get_added(self, cart_with_observer, used_observers):
        c: Cart = cart_with_observer

        c.attach(used_observers[2])
        c.attach(used_observers[3])
        c.attach(used_observers[4])
        assert len(c._observers) == 4

    def test_observers_get_removed(self, cart_with_observer , used_observers):
        c: Cart = cart_with_observer
        c.detach(used_observers[0])
        assert len(c._observers) == 0
    
    def test_cart_notifies_observer(self, cart_with_observer, used_observers):
        c: Cart = cart_with_observer
        c.setCart(value = 1000) 
        assert used_observers[0].test_collect_value == 1000
