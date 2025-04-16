import pytest
from django.urls import reverse
from rest_framework import status

from board.models import Organization
from board.tests.factories import OrganizationFactory


@pytest.mark.django_db
def test_organization_deleted(authenticated_client):
    organization = OrganizationFactory()
    url = reverse('board:organization-retrieve-update-delete', kwargs={'organization_id': organization.id})

    response = authenticated_client.delete(url)
    with pytest.raises(Organization.DoesNotExist):
        organization.refresh_from_db()

    assert response.status_code == status.HTTP_204_NO_CONTENT

@pytest.mark.django_db
def test_organization_not_found(authenticated_client):
    url = reverse('board:organization-retrieve-update-delete', kwargs={'organization_id': 123456})

    response = authenticated_client.delete(url)
    assert response.json()['errors'][0]['code'] == 'organization_not_found'

    assert response.status_code == status.HTTP_404_NOT_FOUND