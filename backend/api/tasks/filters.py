import django_filters
from apps.tasks.models import Task
from django.utils.timezone import make_aware
from datetime import datetime, timedelta


class TaskFilter(django_filters.FilterSet):
    week = django_filters.DateFilter(method="filter_by_week")

    class Meta:
        model = Task
        fields = ["responsible", "week"]

    def filter_by_week(self, queryset, name, value):
        start = make_aware(datetime.combine(value, datetime.min.time()))
        end = start + timedelta(days=7)
        return queryset.filter(created_at__gte=start, created_at__lt=end)
