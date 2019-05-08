""" 视图 """
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


from .models import Userinfo


class UserSerializer(serializers.ModelSerializer):
    """ 用户序列化类"""
    class Meta:
        model = Userinfo
        fields = "__all__"


class MyPagination(PageNumberPagination):
    """ 自定义分页类 """
    page_size = 1
    page_query_param = 'p'

    page_size_query_param = "size"

    max_page_size = 4


class UserView(GenericAPIView):
    """ 用户视图类 """
    queryset = Userinfo.objects.all()
    serializer_class = UserSerializer

    permission_classes = ()
    pagination_class = MyPagination

    def get(self, *args, **kwargs):
        roles = self.get_queryset()  # 获取本视图前边查询的queryset
        page_res = self.paginate_queryset(queryset=roles)  # 获取分页结果
        res = self.get_serializer(instance=page_res, many=True)  # 序列化
        return Response(res.data, status=status.HTTP_200_OK)


class UserViewSet(GenericViewSet):
    """ 继承视图集类"""
    queryset = Userinfo.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()
    pagination_class = MyPagination

    def show(self, *args, **kwargs):
        roles = self.get_queryset()  # 获取queryset
        page_res = self.paginate_queryset(queryset=roles)  # 获取分页后的结果

        res = self.get_serializer(instance=page_res, many=True)  # 序列化

        return Response(res.data, status=status.HTTP_200_OK)

    def create(self, *args, **kwargs):
        pass

class UserModelViewSet(ModelViewSet):
  queryset = Userinfo.objects.all()
  serializer_class = UserSerializer
  permission_classes = ()
  pagination_class = MyPagination
