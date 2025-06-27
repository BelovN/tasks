import pytest
from django.urls import reverse
from apps.tasks.comments.fabrics import TaskCommentFabric
from apps.tasks.fabrics import TaskFabric


@pytest.fixture
def task(user):
    return TaskFabric(author=user)


@pytest.fixture
def task_detail_url(task):
    return reverse("task_detail_api", kwargs={"task_id": task.id})


@pytest.fixture
def task_list_url():
    return reverse("task_list_create_api")


@pytest.fixture
def comment(task, user):
    return TaskCommentFabric(task=task, author=user)


@pytest.fixture
def task_comment_list_url(task):
    return reverse("task_comment_list_create_api", kwargs={"task_id": task.id})


@pytest.fixture
def task_comment_detail_url(task, comment):
    return reverse(
        "task_comment_detail_api",
        kwargs={
            "task_id": task.id,
            "comment_id": comment.id,
        },
    )
