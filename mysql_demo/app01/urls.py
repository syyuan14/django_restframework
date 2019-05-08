""" 路由配置"""

from django.conf.urls import url, include
from .views import ScarDateView,ScarMonthView
urlpatterns = [
    url(r'^scardate/', ScarDateView.as_view()),
    url(r'^scarmonth/', ScarMonthView.as_view()),
]
