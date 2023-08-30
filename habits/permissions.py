from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = 'You are not the habit\'s owner!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False


class IsMainHabitOwner(permissions.BasePermission):
    message = 'You are not the main habit\'s owner!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.main_habit.user:
            return True
        return False