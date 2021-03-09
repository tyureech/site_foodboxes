from rest_framework import serializers
from .models import Review
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "middle_name",
            "phone",
            "address",
        ]


class ReviewSerializ(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Review
        fields = [
            'id',
            'author',
            'text',
            'created_at',
            'published_at',
            'status',
        ]


