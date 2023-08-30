from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import CustomUser
from users.permissions import IsStaffOrSuperuser
from users.serializers import CustomUserSerializer, CustomUserDetailSerializer, CustomUserCreateSerializer


class CustomUserCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomUserCreateSerializer
    permission_classes = [IsAuthenticated, IsStaffOrSuperuser]


class CustomUserListAPIView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsStaffOrSuperuser]


class CustomUserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CustomUserDetailSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsStaffOrSuperuser]


class CustomUserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsStaffOrSuperuser]


class CustomUserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsStaffOrSuperuser]