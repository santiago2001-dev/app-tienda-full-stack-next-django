from core_chatbot.application.domain.repositorys.whatssApp_repository import ExternalRepository


class ExecuteExternalUseCase:
    def __init__(self):
        self.repository = ExternalRepository()

    def execute(self, payload):
        # Puedes agregar validaciones o lógica adicional aquí
        if not payload:
            return {"error": "No se recibió ningún dato"}

        response = self.repository.enviar_datos(payload)
        return response
