from core_chatbot.application.domain.models import Product, Stock

class CreateProductUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, name, description, price, quantity=0):
        product = self.repository.create_product(name, description, price)
        self.repository.create_stock(product, quantity)
        return product
