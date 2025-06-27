from django.urls import path
from api.tasks.comments.views import TaskCommentListCreateView, TaskCommentDetailView

urlpatterns = [
    path("", TaskCommentListCreateView.as_view(), name="task_comment_list_create_api"),
    path(
        "<int:comment_id>/",
        TaskCommentDetailView.as_view(),
        name="task_comment_detail_api",
    ),
]
