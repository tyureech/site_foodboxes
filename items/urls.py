from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import Based
from django.urls import path, include

router = DefaultRouter()
router.register('', Based, basename='based')
urlpatterns = router.urls

# urlpatterns = [
#     path('auth/', include('rest_framework.urls')),
#     path('auth/login/', obtain_auth_token),
#     router.urls,
# ]
