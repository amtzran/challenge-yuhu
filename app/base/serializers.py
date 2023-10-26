from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_polymorphic.serializers import PolymorphicSerializer
from schema import And, Schema


class UserToken(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        return data


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
