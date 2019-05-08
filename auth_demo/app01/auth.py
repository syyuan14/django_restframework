""" 登陆认证"""
import re
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from .models import Usertoken


class Myauthenticate(BaseAuthentication):
    """ 自定义认证"""

    def authenticate(self, request):
        try:
            str1 = request.META.get("HTTP_COOKIE")
            post_list = re.split(",|=", str1)
        except:
            raise exceptions.NotFound("未携带token")
        print(post_list)
        token = post_list[1]
        username = post_list[-1]
        try:
            token_obj = Usertoken.objects.get(
                user__username=username, token=token)
        except Usertoken.DoesNotExist:
            raise exceptions.NotFound("输入密钥不正确或用户不存在")
        return (token_obj.user, token)
