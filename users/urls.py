from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views.register import UserRegisterApi


app_name = 'users'
urlpatterns = [
    path(
        r'auth/token/',
        TokenObtainPairView.as_view(),
        name='access-token',
    ),
    path(
        r'auth/token/refresh/',
        TokenRefreshView.as_view(),
        name='refresh-token',
    ),
    path(
        r'auth/register/',
        UserRegisterApi.as_view(),
        name='register',
    )
]
