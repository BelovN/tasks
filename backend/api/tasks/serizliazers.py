from apps.tasks.models import Task
from libs.serializers import BaseAuthorSerializer


class TaskSerializer(BaseAuthorSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ("created_at", "modified_at", "author")
