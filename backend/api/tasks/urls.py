from django.urls import path, include
from api.tasks.views import TaskListCreateView, TaskDetailView
import api.tasks.comments.urls as task_comments_urls


urlpatterns = [
    path("", TaskListCreateView.as_view(), name="task_list_create_api"),
    path("<int:task_id>/", TaskDetailView.as_view(), name="task_detail_api"),
    path("<int:task_id>/comments/", include(task_comments_urls)),
]
