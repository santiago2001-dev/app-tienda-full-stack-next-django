from django.apps import AppConfig



class CoreChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_chatbot'

    def ready(self):
        from core_chatbot.application.interfaces.rest.product.signals import ProductSignalManager

        ProductSignalManager()