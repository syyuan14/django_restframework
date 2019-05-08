""" 模型层 """
from django.db import models


class Server(models.Model):
    """物理服务器 """
    status_choice = (
        ('online', '上线'),
        ('offline', '下线'),
        ('normal', '正常'),
        ('abnormal', '异常'),
    )
    server_name = models.CharField(max_length=128)
    server_num = models.CharField(max_length=128)
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    cpus = models.IntegerField(default=0)  # cpu核数
    ram = models.IntegerField(default=0)  # 内存大小
    disk = models.IntegerField(default=0)  # 硬盘大小
    product_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=16, choices=status_choice)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
