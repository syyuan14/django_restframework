""" 用户头像模型 """
from django.db import models


class Usericon(models.Model):
    """ 用户头像模型 """
    username = models.CharField(max_length=128)
    icon = models.ImageField(upload_to='usericon')
