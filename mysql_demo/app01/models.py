""" 统计分析模块数据模型"""
from django.db import models


class Airplane(models.Model):
    """ 飞机数据模型"""
    TailNumber = models.CharField(max_length=64)
    LineNumber = models.CharField(max_length=64)
    AC_ASN = models.CharField(max_length=64)
    AC_Variable = models.CharField(max_length=64)


class Scar(models.Model):
    """ 伤痕模型"""
    scar_type_choices = (
        (1, "crack"),
        (2, "perforation"),
        (3, "rivets"),
        (4, "scartch"),
        (5, "flake"),
    )
    #c_time = models.DateTimeField(auto_now_add=True)
    c_time = models.DateTimeField()
    c_date = models.DateField(null=True)
    scar_type = models.SmallIntegerField(choices=scar_type_choices, default=1)
    airplane = models.ForeignKey(to="Airplane", on_delete=models.CASCADE)
