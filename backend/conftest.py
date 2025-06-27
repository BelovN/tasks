import pytest
from rest_framework.test import APIClient
from apps.users.fabrics import UserFabric


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user(db):
    return UserFabric(password="testpass")


@pytest.fixture
def another_user(db):
    return UserFabric(password="otherpass")


@pytest.fixture
def auth_client(client, user):
    client.force_authenticate(user=user)
    return client
