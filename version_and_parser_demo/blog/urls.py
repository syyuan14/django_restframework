""" url 配置"""
from django.conf.urls import url
from .views import UserView
urlpatterns = [
    url(r'^user/$', UserView.as_view(), name="uuu")
]
