from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(f'{settings.ROOT_PATH}admin/', admin.site.urls),
    path(f'{settings.ROOT_PATH}v1/', include('users.urls')),
    path(f'{settings.ROOT_PATH}v1/', include('board.urls')),
    path(f'{settings.ROOT_PATH}v1/community/', include('community.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('silk/', include('silk.urls', namespace='silk'))
    ]
