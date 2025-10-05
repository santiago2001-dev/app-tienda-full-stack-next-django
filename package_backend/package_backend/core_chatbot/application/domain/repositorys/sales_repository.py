from abc import ABC, abstractmethod

class SaleRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create_sale(self, product_id: int, quantity: int):
        pass