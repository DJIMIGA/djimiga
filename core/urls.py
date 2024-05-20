
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

from .views import project_index


urlpatterns = [
    path("", project_index, name="core-index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)