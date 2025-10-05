from core_chatbot.application.domain.models import Product, Stock
from core_chatbot.application.domain.repositorys.prodcuts_repository import ProductRepository


class ProductsGatewayDataBase(ProductRepository):
    def get_by_id(self, product_id):
        product = Product.objects.get(id=product_id)
        products = [product]
        return products

    def get_by_name(self, name):
        product =  Product.objects.get(name=name)
        products = [product]
        return products

    def get_all(self):
        return Product.objects.all()

    def  get_all_with_stock(self):
        return Stock.objects.select_related("product").all()

    def create_product(self, name, description, price):
        product = Product.objects.create(
            name=name,
            description=description,
            price=price
        )
        return product

    def create_stock(self, product, quantity):
        return Stock.objects.create(product=product, quantity=quantity)