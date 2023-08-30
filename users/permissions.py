from rest_framework.permissions import BasePermission


class IsStaffOrSuperuser(BasePermission):
    message = "Вы не можете работать с объектами CustomUser!"

    def has_permission(self, request, view):
        if request.user.is_staff or request.user.is_superuser:
            return True
        return False