from django.urls import path

from board.views import (
    OrganizationListCreateApi,
    OrganizationRetrieveUpdateDeleteApi,
    VacancyListCreateApi,
    VacancyRetrieveUpdateDeleteApi,
)
from board.views.vacancies.approve import VacancyApproveApi
from board.views.vacancies.reject import VacancyRejectApi

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
        r'vacancies/<int:vacancy_id>/',
        VacancyRetrieveUpdateDeleteApi.as_view(),
        name='vacancy-retrieve-update-delete',
    ),
    path(
        r'organizations/',
        OrganizationListCreateApi.as_view(),
        name='organization-list-create'
    ),
    path(
        r'organizations/<int:organization_id>/',
        OrganizationRetrieveUpdateDeleteApi.as_view(),
        name='organization-retrieve-update-delete',
    ),
    path(
        r'vacancies/<int:vacancy_id>/approve/',
        VacancyApproveApi.as_view(),
        name='vacancy-approve',
    ),
    path(
        r'vacancies/<int:vacancy_id>/reject/',
        VacancyRejectApi.as_view(),
        name='vacancy-reject',
    ),
]