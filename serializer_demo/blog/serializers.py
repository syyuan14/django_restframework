""" 序列化模型"""
from rest_framework import serializers
from .models import User, UserGroup, UserRole


class RolesSerializer(serializers.Serializer):
    """序列化模型的基本使用"""
    title = serializers.CharField()
    id = serializers.CharField()


'''
class UserSerializer(serializers.Serializer):
    """ 自定义序列化字段类"""
    id = serializers.IntegerField()  # 定义需要提取的序列化字段名称，与models中的字段名称一样

    username = serializers.CharField()
    password = serializers.CharField()
    # 等同于 sss = serializers.CharField(source="user_type"),此方法只能拿到user_type的key
    user_type = serializers.CharField()
    # 此方法可以取到user_type=((1, "普通用户"),(2, "会员"),)中的value,使用方法："get+下划线+要取得字段+下划线+display"
    user_type_display = serializers.CharField(source="get_user_type_display")
    # 序列化外键,直接source="该模型中外键+点+外链接模型的属性；本质拿到group对象，取title属性"
    user_group = serializers.CharField(source="user_group.title")
    # 多对多序列化方法一：
    user_role = serializers.SerializerMethodField()#序列化多对多键
    #定义一个方法名称为：get+下划线+上边的user_role 名字，参数穿self，和row,row代表User模型表中每行的对象
    def get_user_role(self,row):
      """ 自定义序列化"""
      roles = row.user_role.all().values()
      return list(roles)
'''


class UserSerializer(serializers.ModelSerializer):
    # 此方法可以取到user_type=((1, "普通用户"),(2, "会员"),)中的value,使用方法："get+下划线+要取得字段+下划线+display"
    user_type = serializers.CharField(source="get_user_type_display")
    # 序列化外键,直接source="该模型中外键+点+外链接模型的属性；本质拿到group对象，取title属性"
    user_group = serializers.CharField(source="user_group.title")
    user_role = serializers.SerializerMethodField()

    def get_user_role(self, row):
        roles = row.user_role.all().values()
        return list(roles)

    class Meta:
        model = User
        fields = ("id", "username", "password",
                  "user_type", "user_group", "user_role")


class UserSerializer1(serializers.ModelSerializer):
    user_group = serializers.HyperlinkedIdentityField(
        view_name='gp', lookup_field="user_group_id", lookup_url_kwarg='xxx')

    class Meta:
        model = User
        fields = ("id", "username", "password",
                  "user_type", "user_group", "user_role")
        depth = 1  # 系列化深度，1~10，建议使用不超过3


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = "__all__"
