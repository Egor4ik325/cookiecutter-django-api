from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }
