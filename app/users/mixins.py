from .permissions import AdminPanel


class AdminMixin:
    permission_classes = [AdminPanel]

    @property
    def model(self):
        """
        Retrieve model used in serializer
        """
        return self.serializer_class.Meta.model

    def get_queryset(self):
        """
        Get Only Organization Related objects
        """
        if self.queryset:
            return self.queryset
        return self.model.objects.all()
