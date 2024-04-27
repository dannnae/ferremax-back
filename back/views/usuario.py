from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer, CharField
from back.models import CustomUser


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'type'] 

    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = make_password(password)
        user = CustomUser.objects.create(password=hashed_password, **validated_data)

        return user

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer