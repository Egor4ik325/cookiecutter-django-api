from allauth.account.adapter import get_adapter
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """User details serializer and deserializer (update)."""

    @staticmethod
    def validate_username(username: str):
        # Call allauth username validator
        return get_adapter().clean_username(username)

    class Meta:
        model = User
        fields = [
            "username",
            "date_joined",
            "last_login",
            # Privileges
            "is_active",
            "is_staff",
            "is_superuser",
            # Additional
            "email",
        ]
        # Not-updatable fields
        read_only_fields = [
            "username",
            "email",
            "is_active",
            "is_staff",
            "is_superuser",
        ]
