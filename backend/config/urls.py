from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
import api.urls as api_urls


urlpatterns = [path("api/v1/", include(api_urls))]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
