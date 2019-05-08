""" 用来注册模型，实现在后台进行查看管理数据"""

from django.contrib import admin
from .models import User, UserToken, Blog

admin.site.register(User)
admin.site.register(UserToken)
admin.site.register(Blog)
