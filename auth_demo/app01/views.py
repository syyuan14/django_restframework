""" 书写视图 """

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions


from .models import Userinfo, Usertoken
from .utils.createtoken import md5
from .auth import Myauthenticate
from .serializers import RegisterSerializer


class LoginView(APIView):
    """ 登陆视图 """

    def post(self, request):
        """ 获取登陆数据 """
        result = {"code": 1000, "token": None, "msg": None}
        username = request.data.get("username")
        password = request.data.get("password")

        user = Userinfo.objects.filter(username__exact=username).first()
        if user:
            if user.password == password:
                token = md5(password)
                result["token"] = token
                result["msg"] = "登陆成功"
                Usertoken.objects.update_or_create(
                    user=user, defaults={"token": token})
        return Response(result, status=status.HTTP_200_OK)


class BlogView(APIView):
    """ 查看博客 """
    authentication_classes = (Myauthenticate,)

    def get(self, request):
        """ 获取list"""
        return Response("博客", status=status.HTTP_200_OK)


class RegisterView(APIView):
    """ 注册视图 """

    def post(self, request):
        """ 获取注册数据进行注册"""
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
