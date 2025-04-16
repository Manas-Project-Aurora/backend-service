import pytest
from django.urls import reverse
from rest_framework import status

from board.models import OrganizationContact
from board.tests.factories import OrganizationFactory, OrganizationContactFactory


@pytest.mark.django_db
def test_organization_retrieve(authenticated_client):
    organization = OrganizationFactory()
    url = reverse('board:organization-retrieve-update-delete', kwargs={'organization_id': organization.id})

    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert data == {
        'id': organization.id,
        'name': organization.name,
        'description': organization.description,
        'logo_url': organization.logo_url,
        'contacts': [],
        'event_count': 0,
        'vacancy_count': 0,
        'video_count': 0,
        'created_at': f'{organization.created_at:%Y-%m-%dT%H:%M:%S.%fZ}',
        'updated_at': f'{organization.updated_at:%Y-%m-%dT%H:%M:%S.%fZ}',
    }

@pytest.mark.django_db
def test_organization_not_found(authenticated_client):
    url = reverse('board:organization-retrieve-update-delete', kwargs={'organization_id': 123456})

    response = authenticated_client.delete(url)
    assert response.json()['errors'][0]['code'] == 'organization_not_found'

    assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
def test_organization_have_contacts(authenticated_client):
    organization = OrganizationFactory()

    email_contact = OrganizationContactFactory(
        organization=organization,
        type=OrganizationContact.Type.EMAIL,
        value='test@example.com'
    )

    phone_contact = OrganizationContactFactory(
        organization=organization,
        type=OrganizationContact.Type.PHONE_NUMBER,
        value='+1234567890'
    )

    telegram_contact = OrganizationContactFactory(
        organization=organization,
        type=OrganizationContact.Type.TELEGRAM,
        value='@org_telegram'
    )

    url = reverse('board:organization-retrieve-update-delete', kwargs={'organization_id': organization.id})

    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    expected_contacts = [
        {
            'type': email_contact.type.value,
            'value': email_contact.value,
            'created_at': f'{email_contact.created_at:%Y-%m-%dT%H:%M:%S.%fZ}',
            'updated_at': f'{email_contact.updated_at:%Y-%m-%dT%H:%M:%S.%fZ}'
        },
        {
            'type': phone_contact.type.value,
            'value': phone_contact.value,
            'created_at': f'{phone_contact.created_at:%Y-%m-%dT%H:%M:%S.%fZ}',
            'updated_at': f'{phone_contact.updated_at:%Y-%m-%dT%H:%M:%S.%fZ}'
        },
        {
            'type': telegram_contact.type.value,
            'value': telegram_contact.value,
            'created_at': f'{telegram_contact.created_at:%Y-%m-%dT%H:%M:%S.%fZ}',
            'updated_at': f'{telegram_contact.updated_at:%Y-%m-%dT%H:%M:%S.%fZ}'
        }
    ]

    assert data == {
        'id': organization.id,
        'name': organization.name,
        'description': organization.description,
        'logo_url': organization.logo_url,
        'contacts': expected_contacts,
        'event_count': 0,
        'vacancy_count': 0,
        'video_count': 0,
        'created_at': f'{organization.created_at:%Y-%m-%dT%H:%M:%S.%fZ}',
        'updated_at': f'{organization.updated_at:%Y-%m-%dT%H:%M:%S.%fZ}',
    }

    assert len(data['contacts']) == 3