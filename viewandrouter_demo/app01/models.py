""" 数据库模型 """
from django.db import models


class Userinfo(models.Model):
    """ 用户模型 """
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)

    