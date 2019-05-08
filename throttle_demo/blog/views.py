""" 实现各种数据读取视图的编写"""

import hashlib
import time
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework import status

from blog.models import User, UserToken
#from blog.utils.auth import LoginAuthenticate
from blog.utils.permissions import SVIPPermission
from blog.utils.throttles import BlogVisitThrottle

def md5(username):
    """ 生成token"""
    md1 = hashlib.md5()
    md1.update(username.encode("utf-8"))
    c_time = time.time()
    md1.update(str(c_time).encode("utf-8"))
    return md1.hexdigest()


class LoginView(APIView):
    """
      实现用户的登陆视图
    """
    authentication_classes = ()

    def post(self, request):
        """ 登陆请求"""
        #self.dispatch
        result = {"code": "1000", "msg": None, "data": None}
        username = request.data.get("username")
        password = request.data.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            raise exceptions.NotFound("用户名不存在")
        if user.password == password:
            token = md5(username)
            UserToken.objects.update_or_create(
                user=user, defaults={"token": token})
            return Response(result, status=status.HTTP_200_OK)


class BlogView(APIView):
    """
    博客查看视图
    """
    #authentication_classes = (LoginAuthenticate,)
    permission_classes = (SVIPPermission,)
    throttle_classes = (BlogVisitThrottle,)
    def get(self, request):
        """
        获取blog数据
        """
        result = {"code": "1000", "msg": None, "data": None}
        return Response(result, status=status.HTTP_200_OK)
