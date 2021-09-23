from rest_framework import serializers
from .models import User, Abonent


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("roleId", "login", "displayName", "pictureId", "phoneNumber", "description", "created")


class AbonentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonent
        fields = ("displayName", "description", "pictureId", "perimeterId", "is_admin", "pacsCode", "address",
                  "phoneNumber", "floor", "room", "cars", "isRegistered", "modified")
