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

    def create(self, validated_data):
        cart_items = CartItem(
            item=Item.objects.create(
                title=validated_data['item']['title'],
                description=validated_data['item']['description'],
                image=validated_data['item']['image'],
                weight=validated_data['item']['weight'],
                price=validated_data['item']['price'],
            ),
            # cart=Cart(items=Item.objects.create(
            #     title=validated_data['item']['title'],
            #     description=validated_data['item']['description'],
            #     image=validated_data['item']['image'],
            #     weight=validated_data['item']['weight'],
            #     price=validated_data['item']['price'],
            # )),
            quantity=validated_data['quantity'],
            price=validated_data['price'],
        )

        # print(validated_data['item']['title'])
        # cart_items = CartItem(**validated_data)
        cart_items.save()

        return cart_items


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'items']
        # read_only_fields = ['total_cost']


# class CartItemSerializer(serializers.Serializer):
#     item = serializers.CharField(source='item.id')
#     price = serializers.DecimalField(decimal_places=2, max_digits=6)
