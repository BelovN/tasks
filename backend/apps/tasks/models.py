from django.contrib.auth.models import User
from django.db.models import CharField, TextField, ForeignKey, BooleanField, CASCADE
from django.db.models.fields import DateField

from libs.models import TimestampedBlankAuthorModel
from django.utils.translation import gettext_lazy as _


class Task(TimestampedBlankAuthorModel):
    title = CharField(verbose_name=_("Заголовок"), max_length=255)
    description = TextField(verbose_name=_("Описание"), blank=True, default="")
    is_done = BooleanField(verbose_name=_("Выполнено"), blank=True, default=False)
    on_date = DateField(verbose_name=_("Дата"))
    responsible = ForeignKey(
        User,
        verbose_name=_("Ответственный"),
        on_delete=CASCADE,
        related_name="tasks",
        blank=True,
        null=True,
    )

    class Meta:
        app_label = "tasks"
        db_table = "tasks"
        verbose_name = _("Задача")
        verbose_name_plural = _("Задачи")
