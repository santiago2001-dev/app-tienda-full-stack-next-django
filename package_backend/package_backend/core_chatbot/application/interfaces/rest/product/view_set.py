from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core_chatbot.application.domain.models import Product
from core_chatbot.application.infraestructure.serializers import ProductSerializer
from core_chatbot.application.interfaces.rest.product.filters import productModelFilter


class productViewSetRest(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = productModelFilter
