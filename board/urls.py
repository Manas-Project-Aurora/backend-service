from django.urls import path

from board.views import (
    OrganizationListCreateApi,
    OrganizationRetrieveUpdateDeleteApi,
    VacancyListCreateApi,
    VacancyRetrieveUpdateDeleteApi,
)


app_name = 'board'
urlpatterns = [
    path(
        r'organizations/',
        OrganizationListCreateApi.as_view(),
        name='organization-list-create',
    ),
    path(
        r'vacancies/',
        VacancyListCreateApi.as_view(),
        name='vacancy-list-create',
    ),
    path(
        r'vacancies/<int:pk>/',
        VacancyRetrieveUpdateDeleteApi.as_view(),
        name='vacancy-retrieve-update-delete',
    ),
    path(
        r'organizations/',
        OrganizationListCreateApi.as_view(),
        name='organization-list-create'
    ),
    path(
        r'organizations/<int:pk>/',
        OrganizationRetrieveUpdateDeleteApi.as_view(),
        name='organization-retrieve-update-delete',
    ),
]
