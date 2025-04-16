import pytest
from django.urls import reverse
from rest_framework import status

from board.models import Vacancy
from board.tests.factories import VacancyFactory


@pytest.mark.django_db
def test_vacancy_deleted(user, authenticated_client):
    vacancy = VacancyFactory(user=user)
    url = reverse('board:vacancy-retrieve-update-delete', kwargs={'vacancy_id': vacancy.id})

    response = authenticated_client.delete(url)
    with pytest.raises(Vacancy.DoesNotExist):
        vacancy.refresh_from_db()

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_vacancy_does_not_belong_user(authenticated_client):
    vacancy = VacancyFactory()
    url = reverse('board:vacancy-retrieve-update-delete', kwargs={'vacancy_id': vacancy.id})

    response = authenticated_client.delete(url)
    assert response.json()['errors'][0]['code'] == 'vacancy_access_denied'

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_vacancy_not_found(authenticated_client):
    url = reverse('board:vacancy-retrieve-update-delete', kwargs={'vacancy_id': 123456})

    response = authenticated_client.delete(url)
    assert response.json()['errors'][0]['code'] == 'vacancy_not_found'

    assert response.status_code == status.HTTP_404_NOT_FOUND