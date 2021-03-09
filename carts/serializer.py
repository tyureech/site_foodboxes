from rest_framework import serializers
from .models import CartItem, Cart
from items.models import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = [
            'id',
            "title",
            "description",
            "image",
            "weight",
            "price",
        ]


class CartItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = CartItem
        fields = [
            'id',
            'item',
            'quantity',
            'price',
        ]


class CartItemIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = [
            'id',
            'item',
            'quantity',
            'price',
        ]
        read_only_fields = [
            'id',
            'price',
        ]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'items']
