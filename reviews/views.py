from rest_framework.viewsets import ModelViewSet
from .models import Review
from .serializer import ReviewSerializ


class Reviews(ModelViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializ
