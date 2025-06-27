from django.urls import path, include
import api.auth.urls as auth_urls
import api.dev.urls as dev_urls
import api.tasks.urls as tasks_urls


urlpatterns = [
    path("auth/", include(auth_urls)),
    path("dev/", include(dev_urls)),
    path("tasks/", include(tasks_urls)),
]
