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
def charge_limit() -> dict:
    # "name": (total_delivery_fee, correct returned total_delivery_fee)
    return {"over_limit": (1501, 1500), "on_limit": (1500, 1500), "under_limit": (1, 1),}

@pytest.fixture(scope="session")
def add_till_limit() -> dict:
    return {"add_step_1": (300, 300), "add_step_2": (500, 800),
            "add_step_3": (500, 1300), "limit_over_step_4": (500, 1500)}

class TestFee:
    def test_under_limit(self, cart, charge_limit):
        fee: ISimpleFee = cart.fee
        fee.cumulate_to_fee(charge_limit["under_limit"][0])
        assert fee.fee == charge_limit["under_limit"][1]
    
    def test_on_limit(self, cart, charge_limit):
        fee: ISimpleFee = cart.fee
        fee.cumulate_to_fee(charge_limit["on_limit"][0])
        assert fee.fee == charge_limit["on_limit"][1]
    
    def test_over_limit(self, cart, charge_limit):
        fee: ISimpleFee = cart.fee
        fee.cumulate_to_fee(charge_limit["over_limit"][0])
        assert fee.fee == charge_limit["over_limit"][1]

    def test_over_limit_in_steps(self, cart, add_till_limit):
        fee: ISimpleFee = cart.fee
        fee.cumulate_to_fee(add_till_limit["add_step_1"][0])
        fee.cumulate_to_fee(add_till_limit["add_step_2"][0])
        fee.cumulate_to_fee(add_till_limit["add_step_3"][0])
        fee.cumulate_to_fee(add_till_limit["limit_over_step_4"][0])
        assert fee.fee == add_till_limit["limit_over_step_4"][1]

    def test_over_limit_in_steps_with_multiplier(self, cart, add_till_limit):
        fee: ISimpleFee = cart.fee
        fee.multiplier = 1.5
        fee.cumulate_to_fee(add_till_limit["add_step_1"][0])
        fee.cumulate_to_fee(add_till_limit["add_step_2"][0])
        fee.cumulate_to_fee(add_till_limit["add_step_3"][0])
        fee.cumulate_to_fee(add_till_limit["limit_over_step_4"][0])
        assert fee.fee == add_till_limit["limit_over_step_4"][1]