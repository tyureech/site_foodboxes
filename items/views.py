from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Item
from .serializer import ItemSerializ
from .paginator import ItemsPagination
from .filters import ItemFilter


class Based(ReadOnlyModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializ
    pagination_class = ItemsPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ItemFilter
