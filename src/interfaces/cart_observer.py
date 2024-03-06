from src.interfaces.observer_pattern import Observer
from src.interfaces.cart_subject import ICartSubject
from abc import abstractmethod

class ICartObserver(Observer):
    """
    The ICartObserver interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: ICartSubject) -> None:
        """
        Receive update from ISubjectCart.
        """
        ...