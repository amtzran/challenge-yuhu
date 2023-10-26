from rest_framework.mixins import CreateModelMixin as Create
from rest_framework.mixins import DestroyModelMixin as Delete
from rest_framework.mixins import ListModelMixin as List
from rest_framework.mixins import RetrieveModelMixin as Detail
from rest_framework.mixins import UpdateModelMixin as Update
from rest_framework.viewsets import GenericViewSet

from .mixins import TaskMixin
from .serializers import TaskSerializer


class ApiTaskViewSet(TaskMixin, GenericViewSet, List, Detail, Create, Update, Delete):
    """
    Api Task ViewSet
    """

    serializer_class = TaskSerializer
    search_fields = ["title"]
