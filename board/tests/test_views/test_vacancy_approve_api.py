import pytest
from django.urls import reverse
from rest_framework import status

from board.models import Vacancy
from board.tests.factories import VacancyFactory

@pytest.mark.django_db
def test_vacancy_approve_api(user, authenticated_client):
    vacancy = VacancyFactory(status=Vacancy.Status.PENDING, user=user)
    url = reverse('board:vacancy-approve', kwargs={'vacancy_id': vacancy.id})

    response = authenticated_client.post(url)

    vacancy.refresh_from_db()
    assert vacancy.status == Vacancy.Status.APPROVED
    assert response.status_code == status.HTTP_204_NO_CONTENT

@pytest.mark.django_db
def test_vacancy_approve_if_not_admin(authenticated_not_admin):
    vacancy = VacancyFactory(status=Vacancy.Status.PENDING)
    url = reverse('board:vacancy-approve', kwargs={'vacancy_id': vacancy.id})

    response = authenticated_not_admin.post(url)

    assert response.json()['errors'][0]['code'] == 'vacancy_access_denied'
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_vacancy_approve_if_status_not_pending(user, authenticated_client):
    vacancy = VacancyFactory(status=Vacancy.Status.ACTIVE, user=user)
    url = reverse('board:vacancy-approve', kwargs={'vacancy_id': vacancy.id})

    response = authenticated_client.post(url)

    assert response.json()['errors'][0]['code'] == 'vacancy_is_not_pending'
    assert response.status_code == status.HTTP_400_BAD_REQUEST