""" 序列化视图demo"""
import json
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UserRole, User, UserGroup
from .serializers import RolesSerializer, UserSerializer, UserSerializer1, GroupSerializer


class RolesView(APIView):
    """ 序列化基本使用"""

    def get(self, request, *args, **kwargs):
        """ get请求 """
        roles = UserRole.objects.all()
        serializer = RolesSerializer(instance=roles, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserView(APIView):
    """ 自定义序列化字段"""

    def get(self, request, *args, **kwargs):
        """ get 请求"""
        users = User.objects.all().values()
        serializer = UserSerializer(instance=users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        #print(list(users))
        #print(json.dumps(list(users)))
        #return Response(list(users), content_type="application/json")


class UserView1(APIView):
    """ 自定义序列化字段"""

    def get(self, request, *args, **kwargs):
        """ get 请求"""
        users = User.objects.all()
        serializer = UserSerializer1(
            instance=users, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class GroupView(APIView):
    """ 获取分组视图"""

    def get(self, request, *args, **kwargs):
        """ get 请求"""
        pk = kwargs.get("xxx")
        user_group = UserGroup.objects.filter(pk=pk).first()
        serializer = GroupSerializer(instance=user_group)
        return Response(serializer.data, status=status.HTTP_200_OK)
