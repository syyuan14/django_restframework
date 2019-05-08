""" 后台管理配置"""
from django.contrib import admin
from .models import User, UserGroup, UserRole, UserToken

admin.site.register(User)
admin.site.register(UserGroup)
admin.site.register(UserRole)
admin.site.register(UserToken)
