from datetime import datetime
from core_chatbot.application.use_cases.sale.notification_wha_use_case import ExecuteExternalUseCase


class CreateSaleUseCase:
    def __init__(self, repository):
        self.repository = repository
        self.use_case_notification = ExecuteExternalUseCase()

    def execute(self, product_id: int, quantity: int, numero: str):
        # 1️⃣ Crear la venta en la base de datos
        sale = self.repository.create_sale(product_id, quantity)

        # 2️⃣ Obtener información del producto (según tu repo devuelve el objeto o diccionario)
        product = sale.get("product") if isinstance(sale, dict) else getattr(sale, "product", None)
        descripcion = getattr(product, "name", None) if product else "Producto sin nombre"

        # 3️⃣ Construir el payload para enviar por WhatsApp
        payload = {
            "numero": numero,
            "Descripcion": f"Compra del producto: {descripcion}, cantidad: {quantity}",
            "FechaRecepcion": datetime.now().strftime("%Y-%m-%d")
        }

        self.use_case_notification.execute(payload)

        # 5️⃣ Retornar tanto la venta como el estado de la notificación
        return sale
