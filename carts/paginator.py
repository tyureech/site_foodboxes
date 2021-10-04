from rest_framework.pagination import LimitOffsetPagination


class CartItemsPagination(LimitOffsetPagination):
    offset_query_param = 1
    limit_query_param = 3
