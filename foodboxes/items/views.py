from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from items.models import Item


@api_view(http_method_names=['GET'])
def function_based(request, id):
    item = Item.objects.filter(id=id)
    if item:
        return Response({
            'id': item[0].id,
            'title': item[0].title,
            'description': item[0].description,
            'image': str(item[0].image),
            'weight': item[0].weight,
            'price': item[0].price,
        })
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
