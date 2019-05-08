""" 路由配置"""

from django.conf.urls import url
from .views import RolesView, UserView, UserView1, GroupView


urlpatterns = [
    url(r'roles/$', RolesView.as_view()),
    url(r'users/$', UserView.as_view()),
    url(r'users1/$', UserView1.as_view()),
    url(r'group/(?P<xxx>\d+)/$', GroupView.as_view(), name="gp"),
]
