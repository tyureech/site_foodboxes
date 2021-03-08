from rest_framework.routers import DefaultRouter
from .views import Carts

router = DefaultRouter()
router.register('items', Carts, basename='carts')
urlpatterns = router.urls
