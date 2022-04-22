"""
Base settings to build other settings files upon.
"""
from pathlib import Path

from environ import Env

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
APPS_DIR = ROOT_DIR / "apps"
env = Env()

# DJANGO_READ_DOT_ENV_DEV=false can be set by Docker (production)
if env.bool("DJANGO_READ_DOT_ENV_DEV", True):
    # OS environment variables take precedence over variables from .env.xxx
    env.read_env(str(ROOT_DIR / ".env.dev"))

# General
#
TIME_ZONE = "Europe/Moscow"
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = False
USE_L10N = False
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# URLs
#
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# Apps
#
DJANGO_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.messages",  # used only by `django.contrib.admin`
    "django.contrib.sessions",  # used only by `django.contrib.admin`
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.auth",  # used only by `django.contrib.admin`
    "django.contrib.admin",
    "django.contrib.postgres",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
    "drf_spectacular",
    "django_filters",
    "allauth",
    "allauth.account",
    # "allauth.socialaccount",
    # "rest_framework.authtoken",
    # "dj_rest_auth",
    # "dj_rest_auth.registration",
]
LOCAL_APPS = [
    "apps.users",
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Authentication
#
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",  # used only by `django.contrib.admin`
    "allauth.account.auth_backends.AuthenticationBackend",  # django-allauth
]
AUTH_USER_MODEL = "users.User"

# Passwords
#
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",  # argon2-cffi
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Middleware (used only by `django.contrib.admin`)
#
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # django-cors-headers
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Static
#
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(APPS_DIR / "static")]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Media
#
MEDIA_ROOT = str(APPS_DIR / "media")
MEDIA_URL = "/media/"

# Templates
#
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

# Security
#
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# Admin
#
ADMIN_URL = "admin/"
ADMINS = [("Egor Zorin", "nezort11@gmail.com")]
MANAGERS = ADMINS

# Logging
#
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
}

# django-rest-framework
#
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        # "rest_framework.renderers.BrowsableAPIRenderer",  # use Swagger UI docs
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.MultiPartParser",  # or use base64
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",  # drf-spectacular
    "EXCEPTION_HANDLER": "apps.handlers.exception_handler",
    "DEFAULT_CONTENT_NEGOTIATION_CLASS": "rest_framework.negotiation.DefaultContentNegotiation",
    "UNAUTHENTICATED_USER": "django.contrib.auth.models.AnonymousUser",
    "UNAUTHENTICATED_TOKEN": None,
    # Throttling
    "DEFAULT_THROTTLE_CLASSES": ["rest_framework.throttling.UserRateThrottle"],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "100/minute",
        "user": "100/minute",
    },
    # Pagination and filtering
    "DEFAULT_PAGINATION_CLASS": None,
    "DEFAULT_FILTER_BACKENDS": [],
    "PAGE_PARAM": "page",
    "PAGE_SIZE_PARAM": "page_size",
    "SEARCH_PARAM": "search",
    "ORDERING_PARAM": "ordering",
    "PAGE_SIZE": 10,
    "MAX_PAGE_SIZE": 30,
}

# django-allauth
#
ACCOUNT_ADAPTER = "apps.users.adapters.AccountAdapter"
SOCIALACCOUNT_ADAPTER = "apps.users.adapters.SocialAccountAdapter"
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # to disable set to "none"

# dj-rest-auth
#
REST_AUTH_SERIALIZERS = {
    # Serializer for retrieving and updating user
    "USER_DETAILS_SERIALIZER": "apps.users.auth.serializers.UserSerializer",
}

# django-cors-headers
#
CORS_URLS_REGEX = r"^/api/.*$"

# drf-spectacular
#
SPECTACULAR_SETTINGS = {
    "TITLE": "{{ cookiecutter.project_name }} API",
    "DESCRIPTION": "Documentation of API endpoints of {{ cookiecutter.project_name }}",
    "VERSION": "1.0.0",
    "SCHEMA_PATH_PREFIX": "/api",
}
