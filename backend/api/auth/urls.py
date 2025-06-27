from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.auth.views import RegisterView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register_api"),
    path("login/", TokenObtainPairView.as_view(), name="login_api"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh_api"),
]
