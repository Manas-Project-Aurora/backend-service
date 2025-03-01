from django.conf import settings
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path(f'{settings.ROOT_PATH}/admin/', admin.site.urls),
    path(
        f'{settings.ROOT_PATH}/api/token/',
        TokenObtainPairView.as_view(),
        name='access-token',
    ),
    path(
        f'{settings.ROOT_PATH}/token/refresh/',
        TokenRefreshView.as_view(),
        name='refresh-token',
    ),
]
