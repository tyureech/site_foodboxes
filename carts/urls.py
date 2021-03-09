from rest_framework.routers import DefaultRouter
from .views import CartView, CartItemsView

# router = DefaultRouter()
# router.register('', CartView, basename='cart')
# router.register('items', CartItemsView, basename='cart_items')
# urlpatterns = router.urls

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
    # path('api/v1/', include('items.urls')),
    # path('auth/', include('rest_framework.urls')),
    # path('auth/login/', obtain_auth_token),
    # path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    # path('carts/', include('carts.urls')),
    # path('review/', include('reviews.urls')),
]
