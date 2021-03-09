from rest_framework.viewsets import ModelViewSet, mixins, GenericViewSet
from .models import CartItem
from .serializer import CartItemSerializer, CartSerializer, CartItemIdSerializer
from .paginator import CartItemsPagination


class CartView(GenericViewSet, mixins.RetrieveModelMixin):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer


class CartItemsView(ModelViewSet):
    queryset = CartItem.objects.all()
    pagination_class = CartItemsPagination

    def get_serializer_class(self):
        if self.action == 'create' or \
                self.action == 'update' or \
                self.action == 'partial_update':
            return CartItemIdSerializer
        else:
            return CartItemSerializer
