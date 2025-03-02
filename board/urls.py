from django.urls import path

from board.views import (
    OrganizationListCreateApi,
    OrganizationRetrieveUpdateDeleteApi,
)


app_name = 'board'
urlpatterns = [
    path(
        r'organizations/',
        OrganizationListCreateApi.as_view(),
        name='organization-list-create'
    ),
    path(
        r'organizations/<int:pk>/',
        OrganizationRetrieveUpdateDeleteApi.as_view(),
        name='organization-retrieve-update-delete',
    )
]
