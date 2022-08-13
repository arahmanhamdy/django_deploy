from rest_framework import permissions


class OwnStudentPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.create_by == request.user:
            return True
        return False
