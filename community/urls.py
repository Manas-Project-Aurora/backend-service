from django.urls import path

from community.views import CommunityResourceListApi


app_name = 'community'
urlpatterns = [
    path(r'resources/', CommunityResourceListApi.as_view(), name='resources'),
]
