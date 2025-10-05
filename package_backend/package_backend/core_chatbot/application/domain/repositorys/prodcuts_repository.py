from abc import ABC, abstractmethod

class ProductRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, product_id):
        pass
    @abstractmethod
    def get_by_name(self, name):
        pass

    @abstractmethod
    def get_all_with_stock(self):
        pass

    @abstractmethod
    def create_product(self, name, description, price):
        pass

    @abstractmethod
    def create_stock(self, product, quantity):
        pass