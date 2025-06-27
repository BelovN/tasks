from django.db.models import ForeignKey, TextField, CASCADE
from django.utils.translation import gettext_lazy as _
from apps.tasks.models import Task
from libs.models import TimestampedBlankAuthorModel


class TaskComment(TimestampedBlankAuthorModel):
    task = ForeignKey(
        Task, verbose_name=_("Задача"), on_delete=CASCADE, related_name="comments"
    )
    text = TextField(verbose_name=_("Текст комментария"))

    class Meta:
        app_label = "tasks"
        db_table = "task_comments"
        verbose_name = _("Комментарий к задаче")
        verbose_name_plural = _("Комментарии к задачам")
