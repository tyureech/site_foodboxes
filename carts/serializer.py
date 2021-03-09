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
            # 'item_id',
            # 'total_price',
        ]

    # def create(self, validated_data):
    #     cart_items = CartItem(
    #         item=Item.objects.create(
    #             title=validated_data['item']['title'],
    #             description=validated_data['item']['description'],
    #             image=validated_data['item']['image'],
    #             weight=validated_data['item']['weight'],
    #             price=validated_data['item']['price'],
    #         ),
    #         # cart=Cart(items=Item.objects.create(
    #         #     title=validated_data['item']['title'],
    #         #     description=validated_data['item']['description'],
    #         #     image=validated_data['item']['image'],
    #         #     weight=validated_data['item']['weight'],
    #         #     price=validated_data['item']['price'],
    #         # )),
    #         quantity=validated_data['quantity'],
    #         price=validated_data['price'],
    #     )
    #
    #     # print(validated_data['item']['title'])
    #     # cart_items = CartItem(**validated_data)
    #     cart_items.save()
    #
    #     return cart_items


class CartItemIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = [
            'id',
            'item',
            'quantity',
            'price',
            # 'item_id',
            # 'total_price',
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

