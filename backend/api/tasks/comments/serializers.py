from apps.tasks.comments.models import TaskComment
from libs.serializers import BaseAuthorSerializer


class TaskCommentSerializer(BaseAuthorSerializer):
    class Meta:
        model = TaskComment
        fields = "__all__"
        read_only_fields = ("created_at", "modified_at", "author", "task")
