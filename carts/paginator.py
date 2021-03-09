from rest_framework.pagination import PageNumberPagination


class CartItemsPagination(PageNumberPagination):
    page_size = 3
