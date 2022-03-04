from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    """Model representing user."""

    id = models.BigAutoField(verbose_name="ID", primary_key=True)

    username_validator = UnicodeUsernameValidator()
    email = models.EmailField("email address", unique=True)
    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        validators=[username_validator],
        help_text=(
            "Required. "
            "150 characters or fewer. "
            "Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
    )
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    # Specify user's unique identifier field (used for login)
    USERNAME_FIELD = "email"
    # Describe the name of email field (used in get_email_field)
    EMAIL_FIELD = "email"
    # Fields required when using `createsuperuser` command
    REQUIRED_FIELDS = ["username"]  # + `email` + `password`

    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["username"]

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def __str__(self):
        return self.username
