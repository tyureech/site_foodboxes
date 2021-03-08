from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import Reviews
from django.urls import path, include

router = DefaultRouter()
router.register('', Reviews, basename='review')
urlpatterns = router.urls
