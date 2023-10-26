from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer for user use
    """

    class Meta:
        model = User
        read_only_fields = ["email", "name", "date_joined"]
        fields = read_only_fields
