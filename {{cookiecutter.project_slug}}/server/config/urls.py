"""config URL Configuration."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

# Template/server URLs
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLs
urlpatterns += [
    path("api/", include("config.api_urls")),
    # Authentication, registration, profile/account management
    path("api/auth/", include("config.auth_urls")),
    # OpenAPI schema, Swagger UI
    path("api/", include("config.doc_urls")),
]
