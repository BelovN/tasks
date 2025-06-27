import pytest
from rest_framework import status
from apps.tasks.models import Task

pytestmark = pytest.mark.django_db


def test_list_permissions(client, task_list_url):
    response = client.get(task_list_url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_list_api(auth_client, task_list_url, task):
    response = auth_client.get(task_list_url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]["id"] == task.id


def test_create_task(auth_client, task_list_url):
    payload = {
        "title": "New Task",
        "description": "Some text",
        "on_date": "2025-06-27",  # или лучше timezone.now().date().isoformat()
    }
    response = auth_client.post(task_list_url, data=payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.filter(title="New Task").exists()


def test_retrieve_requires_auth(client, task_detail_url):
    response = client.get(task_detail_url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_retrieve_task(auth_client, task_detail_url, task):
    response = auth_client.get(task_detail_url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == task.id


def test_update_task(auth_client, task_detail_url, task):
    payload = {"title": "Updated"}
    response = auth_client.patch(task_detail_url, data=payload)
    assert response.status_code == status.HTTP_200_OK
    task.refresh_from_db()
    assert task.title == "Updated"


def test_delete_task(auth_client, task_detail_url, task):
    response = auth_client.delete(task_detail_url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Task.objects.filter(id=task.id).exists()
