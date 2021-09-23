from rest_framework import viewsets
from rest_framework.response import Response

from .models import User
from .models import Abonent
from .serializers import UserSerializer
from .serializers import AbonentSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    print("Status code: " + str(Response.status_code))


class AbonentModelViewSet(viewsets.ModelViewSet):
    serializer_class = AbonentSerializer
    queryset = Abonent.objects.all()

    print("Status code: " + str(Response.status_code))
