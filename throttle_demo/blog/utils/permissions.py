""" 自定义权限认证"""

from rest_framework.permissions import BasePermission
from rest_framework import exceptions


class SVIPPermission(BasePermission):
    """ SVIP权限认证"""

    def has_permission(self, request, view):
        try:
            user = request.user
            if user.user_type == 3:
                return True
            else:
                return False
        except:
            raise exceptions.NotFound("未认证")
