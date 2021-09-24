from .views import UserModelViewSet, AbonentModelViewSet, DeviceModelViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r"users", UserModelViewSet, basename='user')
router.register(r"abonents", AbonentModelViewSet, basename='abonent')
router.register(r"devices", DeviceModelViewSet, basename='device')

urlpatterns = router.urls

