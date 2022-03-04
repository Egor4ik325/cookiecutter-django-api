"""
With these settings, tests run faster.
"""

from .base import *
from .base import env

# General
#
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="tUOn8YE1173taLRHn2H2JH8D0jHv8JaAjnmV9wf9pIJRukR7aPHQxUzXlY43Nsbq",
)
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# Databases
#
# TODO: change SQLite3 to Postgres for testing
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(ROOT_DIR / "test.sqlite3"),
    }
}


# Passwords
#
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# Templates
#
TEMPLATES[-1]["OPTIONS"]["loaders"] = [
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

# Email
#
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
