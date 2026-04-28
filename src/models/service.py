from abc import ABC, abstractmethod


class Service(ABC):
    """
    Abstract base class for services.
    """

    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    @abstractmethod
    def calculate_cost(self):
        pass

    @abstractmethod
    def description(self):
        pass