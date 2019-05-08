""" 用于构造数据库模型 """
from django.db import models


class User(models.Model):
    """
      用户信息模型
    """
    user_type_choices = (
        (1, "普通用户"),
        (2, "VIP"),
        (3, "SVIP"),
    )
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=128)
    user_type = models.SmallIntegerField(choices=user_type_choices, default=1)

    def __str__(self):
        return self.username


class Blog(models.Model):
    """
    博客数据模型
    """
    title = models.CharField(max_length=64)
    content = models.TextField()
    owner = models.ForeignKey(to="User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class UserToken(models.Model):
    """
    用户token数据模型
    """
    token = models.CharField(max_length=128)
    user = models.OneToOneField(to="User", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
