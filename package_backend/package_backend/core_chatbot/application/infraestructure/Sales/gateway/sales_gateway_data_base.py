from decimal import Decimal

from django.db import transaction

from core_chatbot.application.domain.models import Venta, Stock, Product
from core_chatbot.application.domain.repositorys.sales_repository import SaleRepository


class SalesGatewayDataBase(SaleRepository):


    def get_all(self):
        return Venta.objects.select_related("product").all()

    @transaction.atomic
    def create_sale(self, product_id: int, quantity: int):
        product = Product.objects.filter(id=product_id).first()
        if not product:
            raise ValueError("Producto no encontrado")

        stock = Stock.objects.filter(product=product).first()
        if not stock or stock.quantity < quantity:
            raise ValueError("Stock insuficiente")

        total_price = Decimal(product.price) * Decimal(quantity)

        venta = Venta.objects.create(
            product=product,
            quantity=quantity,
            total_price=total_price
        )

        stock.quantity -= quantity
        stock.save()

        return venta