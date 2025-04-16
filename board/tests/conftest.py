import pytest
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient

from users.tests.factories import UserFactory


@pytest.fixture
def user():
    return UserFactory(is_admin=True)


@pytest.fixture
def authenticated_client(user):
    refresh_token = RefreshToken.for_user(user)
    access_token = str(refresh_token.access_token)
    client = APIClient()
    client.cookies['access_token'] = access_token
    client.cookies['refresh_token'] = str(refresh_token)
    return client


@pytest.fixture
def not_admin():
    return UserFactory(is_admin=False)


@pytest.fixture
def authenticated_not_admin(not_admin):
    refresh_token = RefreshToken.for_user(not_admin)
    access_token = str(refresh_token.access_token)
    client = APIClient()
    client.cookies['access_token'] = access_token
    client.cookies['refresh_token'] = str(refresh_token)
    return client