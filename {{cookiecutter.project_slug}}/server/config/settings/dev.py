from .base import *
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="c8Gzi5V1SmXruar4hRv0iZvuwF9n10369HnbyL8cSxb6OgbIa17WoqzB2BJjSCdM",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# Caches
#
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
# INSTALLED_APPS += ["debug_toolbar"]
# MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
# DEBUG_TOOLBAR_CONFIG = {
#     "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
#     "SHOW_TEMPLATE_CONTEXT": True,
# }
# INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
# import socket

# hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
# INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
# try:
#     _, _, ips = socket.gethostbyname_ex("node")
#     INTERNAL_IPS.extend(ips)
# except socket.gaierror:
#     pass

# django-extensions
#
INSTALLED_APPS += ["django_extensions"]

# django-cors-headers
#
CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]
