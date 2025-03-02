from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(f'{settings.ROOT_PATH}admin/', admin.site.urls),
    path(r'{settings.ROOT_PATH}', include('users.urls')),
]
