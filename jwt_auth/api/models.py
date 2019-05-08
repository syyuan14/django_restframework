"""" 用户模型 """
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

import django.contrib.auth.models
import rest_framework_jwt.authentication

class UserManager(BaseUserManager):
    """ 用户管理器 """
    use_in_migrations = True

    def create_user(self, email, password, name, sex, mobile, user_type):
        """ 创建用户 """
        if not email:
            raise ValueError("请输入邮件")
        user = self.model(email=email, name=name, sex=sex,
                          mobile=mobile, user_type=user_type)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        """ 创建超级用户 """
        if not email:
            raise ValueError("请输入邮件")
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    """ 自定义用户模型 """
    objects = UserManager()  # 定义用户管理器
    sex_choice = (
        (1, "男"),
        (2, "女"),
    )
    user_type_choice = (
        (1, "普通用户"),
        (2, "管理员"),
    )
    email = models.EmailField(max_length=255, unique=True)

    name = models.CharField(max_length=64)
    mobile = models.CharField(max_length=64)

    created_time = models.DateTimeField(auto_now_add=True)

    sex = models.SmallIntegerField(choices=sex_choice, default=1)
    user_type = models.SmallIntegerField(choices=user_type_choice, default=1)

    USERNAME_FIELD = 'email'  # 必须设置，设置认证标示，设置成标示的字段为unique=True
    #REQUIRED_FIELDS = ['name']  # 当通过createsuperuser管理命令创建一个用户时，用于提示的一个字段名称

    is_active = models.BooleanField(default=True)  # 用户是否活跃

    # is_staff = models.BooleanField(default=False)#是否用户访问admin界面
    # is_superuser = models.BooleanField(default=False)如若不使用admin可以不设置该属性

    def get_full_name(self):
        """ 必须定义long格式的用户表示"""
        return self.name

    def get_short_name(self):
        """ 必须定义short格式的用户表示"""
        return self.name
