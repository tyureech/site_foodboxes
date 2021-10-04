from rest_framework.routers import DefaultRouter
from .views import Based

router = DefaultRouter()
router.register('', Based, basename='based')
urlpatterns = router.urls
