"""
With these settings, tests run faster.
"""

from .base import *

# General
#
SECRET_KEY = "tUOn8YE1173taLRHn2H2JH8D0jHv8JaAjnmV9wf9pIJRukR7aPHQxUzXlY43Nsbq"
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# Databases
#
# TODO: change to Postgres
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(ROOT_DIR / "test.sqlite3"),
    }
}


# Passwords
#
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# Email
#
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
