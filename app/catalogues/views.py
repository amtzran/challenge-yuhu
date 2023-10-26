from rest_framework.viewsets import ModelViewSet

from .serializers import *


class ExampleViewSet(ModelViewSet):
    serializer_class = ExampleSerializer
    queryset = ExampleCatalog.objects.order_by("-created_at").filter(is_deleted=False)
    filterset_fields = ["is_active"]
    search_fields = ["name"]
