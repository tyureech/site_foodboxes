from .views import CartView, CartItemsView
from django.urls import path

cart_retrieve = CartView.as_view({'get': 'retrieve'})
cart_items_list = CartItemsView.as_view({'get': 'list', 'post': 'create'})
cart_items_detail = CartItemsView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', cart_retrieve, name='carts'),
    path('items/', cart_items_list, name='cart_items'),
    path('items/<int:pk>', cart_items_detail, name='cart_items_detail')
]
