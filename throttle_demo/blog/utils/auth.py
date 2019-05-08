""" 实现对登陆用户进行认证"""
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from blog.models import UserToken


class LoginAuthenticate(BaseAuthentication):
    """
    自定义的登陆认证
    """
    def authenticate(self, request):
        # 取出携带的token
        #token = request.META.Cookie.split("=")[1]
        try:
            token = request.META.get("HTTP_COOKIE").split("=")[1]
        except:
            raise exceptions.NotFound("未携带Cookie")
        # print(request.META.get("HTTP_COOKIE").split("=")[1])
        if not token:
            raise exceptions.AuthenticationFailed("未携带token")
        try:
            user_token_obj = UserToken.objects.get(token=token)
        except:
            raise exceptions.NotFound("token不正确")
        user = user_token_obj.user
        return (user, token)
