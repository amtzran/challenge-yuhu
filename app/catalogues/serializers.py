from rest_framework.serializers import ModelSerializer

from .models import *


class ExampleSerializer(ModelSerializer):
    class Meta:
        model = ExampleCatalog
        exclude = ["is_deleted", "deleted_at"]
