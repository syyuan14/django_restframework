""" 对模型数据序列化 """
from rest_framework import serializers
from .models import Userinfo


class RegisterSerializer(serializers.ModelSerializer):
    """ 注册用户序列化"""
    class Meta:
        model = Userinfo
        fields = "__all__"

