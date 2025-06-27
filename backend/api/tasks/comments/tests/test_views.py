import pytest
from rest_framework import status
from apps.tasks.comments.models import TaskComment

pytestmark = pytest.mark.django_db


def test_comment_list_requires_auth(client, task_comment_list_url):
    response = client.get(task_comment_list_url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_comment_list_returns_comments_for_task(
    auth_client, task_comment_list_url, comment
):
    response = auth_client.get(task_comment_list_url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]["id"] == comment.id


def test_comment_create(auth_client, task_comment_list_url, task):
    payload = {
        "text": "new comment",
    }
    response = auth_client.post(task_comment_list_url, data=payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert TaskComment.objects.filter(text="new comment", task=task).exists()


def test_comment_detail_requires_auth(client, task_comment_detail_url):
    response = client.get(task_comment_detail_url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_comment_retrieve(auth_client, task_comment_detail_url, comment):
    response = auth_client.get(task_comment_detail_url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == comment.id


def test_comment_update_by_author(auth_client, task_comment_detail_url, comment):
    payload = {"text": "updated"}
    response = auth_client.patch(task_comment_detail_url, data=payload)
    assert response.status_code == status.HTTP_200_OK
    comment.refresh_from_db()
    assert comment.text == "updated"


def test_comment_delete_by_author(auth_client, task_comment_detail_url, comment):
    response = auth_client.delete(task_comment_detail_url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not TaskComment.objects.filter(id=comment.id).exists()


def test_comment_edit_forbidden_for_non_author(
    client, another_user, task_comment_detail_url
):
    client.force_authenticate(user=another_user)
    response = client.patch(task_comment_detail_url, data={"text": "hack"})
    assert response.status_code == status.HTTP_403_FORBIDDEN
