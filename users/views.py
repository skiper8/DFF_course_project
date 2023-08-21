from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models import User
from users.serializers.serializers import *


class UsersListView(generics.ListAPIView):
    serializer_class = ForAuthUserSerializers
    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]


class UsersDetailView(generics.RetrieveAPIView):
    serializer_class = ForAuthUserSerializers
    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     user = self.request.user
    #     return User.objects.filter(pk=user.id)


class UsersCreateView(generics.CreateAPIView):
    serializer_class = ForCreateUserSerializers
    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     user = self.request.user
    #     return User.objects.filter(pk=user.id)


class UsersUpdateView(generics.UpdateAPIView):
    serializer_class = ForCreateUserSerializers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.id)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
