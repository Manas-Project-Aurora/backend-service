import pytest
from django.urls import reverse
from rest_framework import status

from board.tests.factories import VacancyFactory

@pytest.mark.django_db
def test_vacancy_retrieve(authenticated_client, user):
    vacancy = VacancyFactory(user=user)
    url = reverse('board:vacancy-retrieve-update-delete', kwargs={'vacancy_id': vacancy.id})

    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert data['id'] == vacancy.id
    assert data['title'] == vacancy.title
    assert data['description'] == vacancy.description
    assert data['salary_from'] == vacancy.salary_from
    assert data['salary_to'] == vacancy.salary_to
    assert data['status'] == vacancy.status
    assert data['type'] == vacancy.type
    assert data['salary_type'] == vacancy.salary_type

@pytest.mark.django_db
def test_vacancy_not_found(authenticated_client):
    url = reverse('board:vacancy-retrieve-update-delete', kwargs={'vacancy_id': 123456})

    response = authenticated_client.delete(url)
    assert response.json()['errors'][0]['code'] == 'vacancy_not_found'

    assert response.status_code == status.HTTP_404_NOT_FOUND