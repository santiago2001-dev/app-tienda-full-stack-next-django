from django_filters import rest_framework as filters
from core_chatbot.application.domain.models import Product

class productModelFilter(filters.FilterSet):
    min_price_product = filters.NumberFilter(label="Precio mínimo", method='filter_min_price_product')
    name = filters.CharFilter(label="Nombre", method='filter_name')

    class Meta:
        model = Product
        fields = ['min_price_product', 'name']

    def filter_min_price_product(self, queryset, name, value):
        if value is not None:
            queryset = queryset.filter(price__gte=value).order_by('-price')
        return queryset

    def filter_name(self, queryset, name, value):
        if value:
            queryset = queryset.filter(name__icontains=value).distinct().order_by('price')
        return queryset
