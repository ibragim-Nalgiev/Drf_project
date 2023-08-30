from django.urls import path
from users.apps import UsersConfig
from users.views import CustomUserListAPIView, CustomUserCreateAPIView, CustomUserUpdateAPIView, \
    CustomUserDestroyAPIView, CustomUserRetrieveAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', CustomUserListAPIView.as_view(), name='users_list'),
    path('users/detail/<int:pk>/', CustomUserRetrieveAPIView.as_view(), name='users_detail'),
    path('users/create/', CustomUserCreateAPIView.as_view(), name='users_create'),
    path('users/update/<int:pk>/', CustomUserUpdateAPIView.as_view(), name='users_update'),
    path('users/delete/<int:pk>/', CustomUserDestroyAPIView.as_view(), name='users_delete'),
]