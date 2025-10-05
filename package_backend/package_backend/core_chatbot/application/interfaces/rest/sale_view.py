from rest_framework import viewsets, status
from rest_framework.response import Response

from core_chatbot.application.infraestructure.Deeep_seek_integration.deep_seek_gateway import DeppSeekIntegration
from core_chatbot.application.infraestructure.Sales.gateway.sales_gateway_data_base import SalesGatewayDataBase
from core_chatbot.application.infraestructure.serializers import VentaSerializer
from core_chatbot.application.use_cases.sale.create_sale_use_case import CreateSaleUseCase
from core_chatbot.application.use_cases.sale.use_case_get_all_sales import UseCaseGetAllSales
from rest_framework.decorators import action


class SaleViewSet(viewsets.ViewSet):
    repository = SalesGatewayDataBase()
    use_case_list_all = UseCaseGetAllSales(repository)
    use_case_create = CreateSaleUseCase(repository)
    deep_seek = DeppSeekIntegration()

    def list(self, request):
        try:
            sales = self.use_case_list_all.execute()
            serializer = VentaSerializer(sales, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=['post'], url_path='create')

    def create_sale(self, request):
        try:
            product_id = request.data.get('product_id')
            quantity = int(request.data.get('quantity'))
            numero = request.data.get('numero')
            venta = self.use_case_create.execute(product_id, quantity,numero)
            serializer = VentaSerializer(venta)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def integration(self, request):
        try:
            prompt = request.data.get('prompt')
            if not prompt:
                return Response({"error": "El campo 'prompt' es requerido."}, status=status.HTTP_400_BAD_REQUEST)

            response =  self.deep_seek.StartChat(prompt)
            return Response({"mensaje": f"Recibido: {response}"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)