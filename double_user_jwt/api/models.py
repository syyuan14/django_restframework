""" 定义双认证模型 """
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, AbstractUser,BaseUserManager

class UserManager(BaseUserManager):
    """ 定义用户管理器 """
    pass


class User(AbstractBaseUser):
    """ 定义认证用户表 """
    sex_choice = (
      ("male", "男"),
      ("female", "女")
    )
    user_id = models.CharField(max_length=64, primary_key=True, unique=True)
    name = models.CharField(max_length=64)
    sex = models.CharField(max_length=32, choices=sex_choice, default="male")
    date_joined = models.DateField(auto_now_add=True)
    objects = UserManager()
    USERNAME_FIELD = 'user_id'


class Student(models.Model):
    """ 定义学生类 """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    major = models.CharField(max_length=64)

class Teacher(models.Model):
  """ 定义老师类 """
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  position = models.CharField(max_length=64)

