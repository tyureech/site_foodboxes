from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import Based
from django.urls import path

router = DefaultRouter()
router.register('based', Based, basename='based')
urlpatterns = router.urls
# urlpatterns = [
#     path('/login/', obtain_auth_token),
#     router.urls
# ]
