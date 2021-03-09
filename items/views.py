from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .models import Item
from .serializer import ItemSerializ
from .paginator import ItemsPagination


class Based(ReadOnlyModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializ
    pagination_class = ItemsPagination
