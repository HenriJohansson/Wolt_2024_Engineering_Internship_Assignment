from __future__ import annotations
from abc import ABC, abstractmethod
#Source for the base https://refactoring.guru/design-patterns/observer/python/example

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        ...

class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        ...

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        ...

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers subscribed to specific enum about an event.
        """
        ...