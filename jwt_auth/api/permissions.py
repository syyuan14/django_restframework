""" 定义权限"""
from rest_framework.permissions import BasePermission


class SuperUserPermission(BasePermission):
    """ 设置管理员权限 """

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if not request.user:
            return False
        if request.user.user_type == 2:
            return True
