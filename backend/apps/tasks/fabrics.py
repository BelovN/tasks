import factory
from factory.django import DjangoModelFactory
from faker import Faker
from apps.tasks.models import Task
from datetime import timezone
from apps.users.fabrics import UserFabric

fake = Faker()


class TaskFabric(DjangoModelFactory):
    class Meta:
        model = Task

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=3))
    description = factory.LazyAttribute(lambda _: fake.text(max_nb_chars=100))
    on_date = factory.LazyFunction(lambda: fake.date_object())
    created_at = factory.LazyFunction(lambda: fake.date_time(tzinfo=timezone.utc))
    modified_at = factory.LazyFunction(lambda: fake.date_time(tzinfo=timezone.utc))
    author = factory.SubFactory(UserFabric)
    responsible = factory.SubFactory(UserFabric)
