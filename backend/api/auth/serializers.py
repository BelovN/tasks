from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import CharField, ModelSerializer, ValidationError
from rest_framework.validators import UniqueValidator


class RegisterSerializer(ModelSerializer):
    password = CharField(write_only=True, min_length=6, label=_("Пароль"))
    confirm = CharField(write_only=True, label=_("Подтверждение пароля"))
    username = CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        label=_("Имя пользователя"),
    )

    class Meta:
        model = User
        fields = ("username", "password", "confirm")

    def validate(self, data):
        if data["password"] != data["confirm"]:
            raise ValidationError("Пароли не совпадают")
        return data

    def create(self, validated_data):
        validated_data.pop("confirm")
        return User.objects.create_user(**validated_data)
