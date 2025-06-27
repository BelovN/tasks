from django.contrib.auth.models import User
from django.db.models import Model, DateTimeField, ForeignKey, SET_NULL
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class TimestampedBlankAuthorModel(Model):
    author = ForeignKey(
        User, blank=True, null=True, on_delete=SET_NULL, verbose_name=_("Автор")
    )
    created_at = DateTimeField(
        blank=True, default=timezone.now, verbose_name=_("Создан в")
    )
    modified_at = DateTimeField(auto_now=True, verbose_name=_("Обновлен в"))

    class Meta:
        abstract = True
