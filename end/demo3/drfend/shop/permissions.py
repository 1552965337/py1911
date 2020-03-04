# author sqz
# date 2020/3/3 14:12
# file_name permissions
"""
可以自定义权限
"""
from rest_framework import permissions
class CategoryPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return False
class OrderPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user==request.user