""" 路由配置 """
from django.conf.urls import url, include
from rest_framework import routers
from .views import ServerViewSet

ServerRouter = routers.DefaultRouter()
ServerRouter.register('', ServerViewSet)
urlpatterns = [
    url(r'^servers/', include(ServerRouter.urls))
]
