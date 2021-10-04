from rest_framework.routers import DefaultRouter
from .views import UserViews

router = DefaultRouter()
router.register('', UserViews, basename='user')
urlpatterns = router.urls
