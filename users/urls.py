from django.urls import path

from users.views.refresh import RefreshTokenApi
from users.views.register import UserRegisterApi
from users.views.login import UserLoginApi
from users.views.logout import UserLogoutApi
from users.views.me import UserApi


app_name = 'users'
urlpatterns = [
    path(
        r'auth/me/',
        UserApi.as_view(),
        name='me',
    ),
    path(
        r'auth/logout/',
        UserLogoutApi.as_view(),
        name='logout',
    ),
    path(
        r'auth/login/',
        UserLoginApi.as_view(),
        name='login',
    ),
    path(
        r'auth/token/refresh/',
        RefreshTokenApi.as_view(),
        name='refresh-token',
    ),
    path(
        r'auth/register/',
        UserRegisterApi.as_view(),
        name='register',
    )
]
