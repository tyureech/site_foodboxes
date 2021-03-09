from rest_framework import serializers
from .models import Item


class ItemSerializ(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id',
            'title',
            'description',
            'image',
            'weight',
            'price',
        ]
