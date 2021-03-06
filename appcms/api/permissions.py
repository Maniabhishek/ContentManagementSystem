from rest_framework import permissions
from rest_framework.permissions import BasePermission

# this class will findout if the user has permission to delete or update the post , to check if logged in user and post owner is same or not


class IsOwnerOrReadOnly(BasePermission):
    message = "you must be the owner of this post "

    def has_object_permission(self, request, view, obj):
        my_safe_method = ['PUT']
        print(request.user.is_staff)
        print(request.user.is_superuser)
        if request.method in my_safe_method:
            return True
        return request.user.is_superuser or obj.author == request.user
