from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from items.models import Item
from items.serializer import ItemSerializ


class Based(ViewSet):

    def list(self, request):
        queryset = Item.objects.all()
        serializer = ItemSerializ(queryset, many=True)
        return Response(
            serializer.data
        )

    def retrieve(self, request, pk=None):
        queryset = Item.objects.all()
        item = get_object_or_404(queryset, id=pk)
        serializer = ItemSerializ(item)
        return Response(serializer.data)


# @api_view(http_method_names=['GET'])
# def function_based(request, id):
#     item = Item.objects.filter(id=id)
#     if item:
#         return Response({
#             'id': item[0].id,
#             'title': item[0].title,
#             'description': item[0].description,
#             'image': str(item[0].image),
#             'weight': item[0].weight,
#             'price': item[0].price,
#         })
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
