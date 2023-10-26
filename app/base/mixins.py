from rest_framework.serializers import ModelSerializer
from rest_polymorphic.serializers import PolymorphicSerializer
from schema import And, Schema

from users.permissions import AdminPanel


class BaseMixin:
    """
    Base mixin for api tasks
    """

    permission_classes = [AdminPanel]

    @property
    def user(self):
        """
        Retrieve user
        """

        return self.request.user if self.request else None

    @property
    def model(self):
        """
        Retrieve model used in serializer
        """

        return self.serializer_class.Meta.model

    def get_queryset(self):
        """
        Get all objects
        """

        if self.queryset:
            return self.queryset

        return self.model.objects.all()


class ToRepresentationMixin(ModelSerializer):
    """
    Mixin to simplify to_representation for fields with a REPRESENTATION_FIELDS that
    has the following structure:
        REPRESENTATION_FIELDS = [
            (field_name, model_name, serializer_name, many),
        ]
    """

    schema = Schema(
        [
            And(
                (
                    str,
                    lambda serializer: issubclass(serializer, ModelSerializer)
                    or issubclass(serializer, PolymorphicSerializer),
                    bool,
                ),
                lambda s: len(s) == 3,
            )
        ]
    )

    REPRESENTATION_FIELDS = []

    def to_representation(self, instance):
        assert len(self.REPRESENTATION_FIELDS) > 0
        representation = super().to_representation(instance)
        assert self.schema.validate(self.REPRESENTATION_FIELDS) == self.REPRESENTATION_FIELDS
        for field, serializer, many in self.REPRESENTATION_FIELDS:
            representation[field] = (
                serializer(instance=getattr(instance, field), context=self.context)
                if not many
                else serializer(getattr(instance, field), many=many, context=self.context)
            ).data
        return representation
