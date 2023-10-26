from base.mixins import ToRepresentationMixin
from users.serializers import UserSerializer

from ..models import Task


class TaskSerializer(ToRepresentationMixin):
    """
    Serializer for Task model
    """

    REPRESENTATION_FIELDS = [
        ("author", UserSerializer, False),
    ]

    class Meta:
        model = Task
        read_only_fields = ["random_slug", "author", "created_at"]
        fields = read_only_fields + [
            "title",
            "description",
            "email",
            "due_date",
        ]
