from django_filters.rest_framework import FilterSet
from .models import Item


class ItemFilter(FilterSet):
    class Meta:
        model = Item
        fields = {
            'price': ['gt', 'gte', 'lt', 'lte'],
            'weight': ['gt', 'gte', 'lt', 'lte'],
        }
