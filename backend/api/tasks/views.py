from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from api.tasks.filters import TaskFilter
from api.tasks.serizliazers import TaskSerializer
from apps.tasks.models import Task


class TaskListCreateView(ListCreateAPIView):
    lookup_url_kwarg = "task_id"
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_class = TaskFilter
    permission_classes = [IsAuthenticated]


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = "task_id"
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
