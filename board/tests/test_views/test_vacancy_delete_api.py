import pytest
from django.urls import reverse
from rest_framework import status

from board.models import Vacancy
from board.tests.factories import OrganizationFactory


@pytest.mark.django_db
def test_vacancy_delete_api(user, authenticated_client):
    url = reverse('board:vacancy-list-create')
    organization = OrganizationFactory()

    response = authenticated_client.post(
        url,
        format='json',
        data={
            'title': 'Test Vacancy',
            'description': 'Test Description',
            'organization_id': organization.id,
            'type': Vacancy.Type.REMOTE,
            'salary_type': Vacancy.SalaryType.HOURLY,
            'salary_from': 1000,
            'salary_to': 1000,
        },
    )

    assert response.status_code == status.HTTP_201_CREATED
