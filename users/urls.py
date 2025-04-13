from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from users.views.register import UserRegisterApi
from users.views.login import UserLoginApi


app_name = 'users'
urlpatterns = [
    path(
        r'auth/login/',
        UserLoginApi.as_view(),
        name='login',
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
