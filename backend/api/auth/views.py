from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from api.auth.serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token_serializer = TokenObtainPairSerializer(
            data={"username": user.username, "password": request.data["password"]}
        )
        token_serializer.is_valid(raise_exception=True)

        return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)
