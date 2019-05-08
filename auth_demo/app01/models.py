""" 数据模型 """
from django.db import models


class Userinfo(models.Model):
    """ 用户数据模型 """
    user_type_choices = (
        (1, "普通会员"),
        (2, "VIP"),
        (3, "SVIP")
    )
    sex_choices = (
        (1, "男"),
        (2, "女"),
    )
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=128)

    user_type = models.IntegerField(
        max_length=32, choices=user_type_choices, default=1)

    name = models.CharField(max_length=64,null=False)
    sex = models.IntegerField(choices=sex_choices, default=1, max_length=32,null=False)


class Usertoken(models.Model):
    """ 用户token模型 """
    user = models.OneToOneField(to="Userinfo", on_delete=models.CASCADE)
    token = models.CharField(max_length=128)
