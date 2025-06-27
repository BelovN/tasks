import factory
from faker import Faker
from apps.tasks.fabrics import TaskFabric
from apps.tasks.comments.models import TaskComment
from apps.users.fabrics import UserFabric

fake = Faker()


class TaskCommentFabric(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskComment

    task = factory.SubFactory(TaskFabric)
    author = factory.SubFactory(UserFabric)
    text = factory.LazyAttribute(lambda _: fake.sentence(nb_words=10))
