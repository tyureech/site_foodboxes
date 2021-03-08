from django.shortcuts import render
from drf_yasg.openapi import Response
from rest_framework.generics import get_object_or_404

from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import status
from .models import CartItem
from .serializer import CartItemSerializer
from rest_framework.permissions import IsAuthenticated


class Carts(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    # def create(self, request):
    #     queryset = CartItem.objects.all()
    #     serializer = CartItemSerializer(queryset)
    #     return Response(serializer)
    #
    # def retrieve(self, request, pk):
    #     queryset = CartItem.objects.all()
    #     cart = get_object_or_404(queryset, pk=pk)
    #     serializer = CartItemSerializer(cart)
    #     return Response(serializer)




