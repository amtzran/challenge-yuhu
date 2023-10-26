from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import User


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            return User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("No existe un usuario con ese email")

    def save(self, validated_data):
        email = validated_data.get("email")
        user = User.objects.get(email=email)
        token = PasswordResetTokenGenerator().make_token(user)

        return f"{settings.FRONTEND_DOMAIN}{settings.FRONTEND_RESET_PASSWORD_PATH}/{token}?u={user.pk}", user


class SetPasswordSerializer(serializers.Serializer):
    """Serializer to set password"""

    user_id = serializers.CharField()
    token = serializers.CharField()
    password = serializers.CharField()

    def validate_password(self, value):
        validate_password(value)
        return value

    def validate(self, attrs):
        token = attrs.get("token")
        user_id = attrs.get("user_id")
        user = User.objects.get(pk=user_id)
        verified_token = PasswordResetTokenGenerator().check_token(user, token)
        if verified_token:
            return attrs
        else:
            raise ValidationError({"token": "The token is not valid"})

    def save(self, validated_data):
        data = validated_data
        user_id = data.get("user_id")
        user = User.objects.get(pk=user_id)
        user.set_password(data.get("password"))
        user.save()
