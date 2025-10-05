from itertools import product

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core_chatbot.application.infraestructure.product.gateway.products_gateway_dataBase import ProductsGatewayDataBase
from core_chatbot.application.infraestructure.serializers import ProductSerializer, StockSerializer
from core_chatbot.application.use_cases.product.create_product_use_case import CreateProductUseCase
from core_chatbot.application.use_cases.product.list_all_product import GetAllProductUseCase
from core_chatbot.application.use_cases.product.list_all_stock_product import GetAllProductStockUseCase
from core_chatbot.application.use_cases.product.list_by_id_product import ListByIdUseCaseProduct
from core_chatbot.application.use_cases.product.list_by_name import ListByNameUseCase


class ProductViewSet(viewsets.ViewSet):
    repository = ProductsGatewayDataBase()
    use_case_list_all =  GetAllProductUseCase(repository)
    use_case_list_by_id  =  ListByIdUseCaseProduct(repository)
    use_case_list_by_name = ListByNameUseCase(repository)
    use_case_list_all_stock  = GetAllProductStockUseCase(repository)
    use_case_create = CreateProductUseCase(repository)

    def list(self, request):
        try:
            products = self.use_case_list_all.execute()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=['post'])
    def create_product(self, request):
        try:
            name = request.data.get("name")
            description = request.data.get("description")
            price = request.data.get("price")
            quantity = request.data.get("quantity", 0)  # opcional

            product = self.use_case_create.execute(name, description, price, quantity)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, url_path='stock', methods=['get'])
    def stock_all(self, request):
            try:
                products = self.use_case_list_all_stock.execute()
                serializer = StockSerializer(products, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response(
                    {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )


    @action(detail=False, methods=['get'])
    def list_by_id(self, request):
        try:
            name = request.query_params.get('id')
            products = self.use_case_list_by_id.execute(name)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=['get'])
    def list_by_name(self, request):
      try:
        name = request.query_params.get('name')
        products = self.use_case_list_by_name.execute(name)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
      except Exception as e:
          return Response(
              {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
          )