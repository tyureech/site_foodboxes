from django.shortcuts import render
from drf_yasg.openapi import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404

from rest_framework.viewsets import ViewSet, ModelViewSet, mixins, GenericViewSet
from rest_framework import status, serializers
from drf_yasg.utils import swagger_auto_schema
from .models import CartItem, Cart
from .serializer import CartItemSerializer, CartSerializer, CartItemIdSerializer
from .paginator import CartItemsPagination
from rest_framework.permissions import IsAuthenticated


class CartView(GenericViewSet, mixins.RetrieveModelMixin):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer


class CartItemsView(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    pagination_class = CartItemsPagination

    def get_serializer_class(self):
        if self.action == 'create' or \
                self.action == 'update' or \
                self.action == 'partial_update':
            return CartItemIdSerializer
