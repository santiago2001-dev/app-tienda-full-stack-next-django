from datetime import datetime
from django.db.models.signals import post_save
from core_chatbot.application.domain.models import Product
from core_chatbot.application.use_cases.sale.notification_wha_use_case import ExecuteExternalUseCase

class ProductSignalManager:
    """Maneja los signals del modelo Product."""

    use_case_notification = ExecuteExternalUseCase()

    @staticmethod
    def on_product_created(sender, instance, created, **kwargs):
        """Signal que se ejecuta cuando se crea un producto."""
        print("🧩 Entró al signal on_product_created (versión estática)")
        if created:

            payload = {
                "numero": "573222354356",
                "Descripcion": f"Se creó el siguiente producto: {instance.name} con valor {instance.price}",
                "FechaRecepcion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            ProductSignalManager.use_case_notification.execute(payload)
            print("✅ Use case ejecutado desde signal",instance)



# 👇 Conectamos el método estático (no depende de ninguna instancia)
post_save.connect(ProductSignalManager.on_product_created, sender=Product)
print("✅ ProductSignalManager conectado al post_save de Product")
