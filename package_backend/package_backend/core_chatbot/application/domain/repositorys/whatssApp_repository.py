from core_chatbot.application.infraestructure.whatssap_service.whatssApp_service_gateway import ExternalGateway


class ExternalRepository:
    def __init__(self):
        self.gateway =   ExternalGateway   ("https://qa.citofonia.devinovate.online")

    def enviar_datos(self, data):
        endpoint = "/api/wha/send"
        return self.gateway.send_post(endpoint, data)
