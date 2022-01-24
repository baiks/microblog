from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            raise AuthenticationFailed("Unauthorized request")
        if request.user.is_authenticated:
            return True
        return False
