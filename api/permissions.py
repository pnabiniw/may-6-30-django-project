from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_superuser)
        # if bool(request.user.is_authenticated and request.user.is_superuser):
        #     return True
        # return False


class IsCreatorUser(BasePermission):
    def has_permission(self, request, view):
        groups = request.user.groups.all().values_list("name", flat=True) # [Reviewer, User]
        if request.user.is_authenticated and "Reviewer" in groups:
            return True
        return False
