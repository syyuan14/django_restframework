""" 序列化 """
from rest_framework import serializers
from .models import Server


class ServerSerializer(serializers.ModelSerializer):
    """ server 序列化类 """
    class Meta:
        model = Server
        fields = "__all__"

        def validate_status(self, value):
            """ 自定义验证status字段 """
            if value not in ('online', 'offline', 'normal', 'abnormal'):
                raise ValueError("数据格式错误")
            else:
                return value
