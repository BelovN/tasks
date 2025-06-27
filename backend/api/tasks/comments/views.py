from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from api.tasks.comments.serializers import TaskCommentSerializer
from apps.tasks.comments.models import TaskComment
from apps.tasks.models import Task
from libs.permissions import IsAuthorOrReadOnly


class TaskCommentListCreateView(ListCreateAPIView):
    lookup_url_kwarg = "comment_id"
    serializer_class = TaskCommentSerializer
    ordering = ["created_at"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return TaskComment.objects.none()

        task_id = self.kwargs["task_id"]
        return TaskComment.objects.filter(task_id=task_id).order_by("created_at")

    def perform_create(self, serializer):
        task = Task.objects.get(id=self.kwargs["task_id"])
        serializer.save(task=task, author=self.request.user)


class TaskCommentDetailView(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = "comment_id"
    serializer_class = TaskCommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        task_id = self.kwargs["task_id"]
        return TaskComment.objects.filter(task_id=task_id).order_by("created_at")
