import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

pytestmark = pytest.mark.django_db


def test_register_success(client):
    payload = {
        "username": "newuser",
        "password": "newpass123",
        "confirm": "newpass123",
    }
    url = reverse("register_api")
    response = client.post(url, data=payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert "access" in response.data
    assert "refresh" in response.data


def test_register_failed(client):
    payload = {
        "username": "newuser",
        "password": "some",
        "confirm": "other",
    }
    url = reverse("register_api")
    response = client.post(url, data=payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_login_success(client, user, user_password):
    payload = {
        "username": user.username,
        "password": user_password,
    }
    url = reverse("login_api")
    response = client.post(url, data=payload)
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data


def test_login_failed(client):
    url = reverse("login_api")
    response = client.post(url, data={"username": "bad", "password": "wrong"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_token_refresh(client, user):
    refresh = str(RefreshToken.for_user(user))
    url = reverse("token_refresh_api")
    response = client.post(url, data={"refresh": refresh})
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data


def test_token_refresh_failed(client):
    url = reverse("token_refresh_api")
    response = client.post(url, data={"refresh": "some"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
