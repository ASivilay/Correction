# projects.permission.py

from rest_framework.permissions import BasePermission
from rest_framework import request
from rest_framework import permissions

class IsAuthorOrContributor(permissions.BasePermission):
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
        elif obj.contributor == request.user:
            return True
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user 
    
        

