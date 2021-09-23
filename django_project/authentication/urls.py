from .views import UserModelViewSet
from .views import AbonentModelViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r"users", UserModelViewSet, basename='user')
router.register(r"abonents", AbonentModelViewSet, basename='abonent')

urlpatterns = router.urls

