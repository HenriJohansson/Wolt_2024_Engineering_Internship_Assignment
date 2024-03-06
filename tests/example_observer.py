from src.interfaces.cart_observer import ICartObserver
from src.interfaces.cart_subject import ICartSubject

class ExampleObserver(ICartObserver):
    """
    Class is an example of a Observer
    """

    test_collect_value: int = 0

    def update(self, cart: ICartSubject) -> None:
        self.test_collect_value = cart.value
