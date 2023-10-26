from rest_framework.permissions import BasePermission


class AdminPanel(BasePermission):
    """
    Allows access only to authenticated users that are users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
