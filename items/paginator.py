from rest_framework.pagination import PageNumberPagination


class ItemsPagination(PageNumberPagination):
    page_size = 3
