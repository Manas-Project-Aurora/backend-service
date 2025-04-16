import pytest
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient

from users.tests.factories import UserFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def authenticated_client(user):
    refresh_token = RefreshToken.for_user(user)
    access_token = str(refresh_token.access_token)
    client = APIClient()
    client.cookies['access_token'] = access_token
    client.cookies['refresh_token'] = str(refresh_token)
    return client
