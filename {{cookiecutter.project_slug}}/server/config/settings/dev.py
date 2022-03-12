from .base import *
from .base import env

# General
#
DEBUG = True
SECRET_KEY = "c8Gzi5V1SmXruar4hRv0iZvuwF9n10369HnbyL8cSxb6OgbIa17WoqzB2BJjSCdM"
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# Databases
#
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": str(ROOT_DIR / "db.sqlite3"),
#         "ATOMIC_REQUESTS": True,
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "ATOMIC_REQUESTS": True,
    }
}

# Email
#
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.smtp.ConsoleBackend"

# django-extensions
#
INSTALLED_APPS += [
    "django_extensions",
]

# django-cors-headers
#
CORS_ALLOW_ALL_ORIGINS = True

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
