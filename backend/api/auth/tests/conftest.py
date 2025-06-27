import pytest
from apps.users.fabrics import UserFabric


@pytest.fixture
def user_password():
    return "sdfghskdfgpierjgior"


@pytest.fixture
def user(user_password):
    return UserFabric(username="test_user", password="sdfghskdfgpierjgior")
