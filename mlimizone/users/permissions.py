from rest_framework import permissions
from django.conf import settings

class IsWhitelistedAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        whitelist = getattr(settings, 'ADMIN_EMAIL_WHITELIST', [])
        return (
            user.is_authenticated and
            getattr(user, "role", None) == "admin" and
            getattr(user, "email", None) in whitelist
        )