from rest_framework import permissions

class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
        if request.method != 'GET':
            return obj.author == request.user
        return True