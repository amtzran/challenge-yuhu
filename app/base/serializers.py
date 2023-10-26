from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserToken(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        return data
