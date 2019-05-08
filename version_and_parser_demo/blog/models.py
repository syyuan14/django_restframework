""" 数据库模型"""
from django.db import models


class UserGroup(models.Model):
    """
    用户组数据模型
    """
    title = models.CharField(max_length=64)


class User(models.Model):
    """
    用户数据模型
    """
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)

    user_group = models.ForeignKey(to="UserGroup", on_delete=models.CASCADE)

    user_role = models.ManyToManyField(to="UserRole")

class UserToken(models.Model):
    """
    用户token数据模型
    """
    user = models.OneToOneField(to="User", on_delete=models.CASCADE)
    token = models.CharField(max_length=64)


class UserRole(models.Model):
    """
    用户角色数据模型
    """
    title = models.CharField(max_length=32)
