from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from items.models import Item
from items.serializer import ItemSerializ


class Based(ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializ
