""" 视图层 """
import django_filters
from rest_framework.viewsets import ModelViewSet

from .models import Server
from .serializers import ServerSerializer


class ServerFilter(django_filters.rest_framework.FilterSet):
    """ 物理服务器过滤类 """
    server_name = django_filters.CharFilter(
        field_name='server_name', lookup_expr='icontains')  # field_name指定对应的是model里的那个字段，look_expr是筛选条件
    brand = django_filters.CharFilter(field_name='brand', lookup_expr='icontains')
    # 不指定lookup_expr 即为精确查找，lookup_expr='exact'
    cpus = django_filters.NumberFilter(field_name='cpus')
    ram = django_filters.NumberFilter(field_name="ram")
    disk = django_filters.NumberFilter(field_name="disk")
    start = django_filters.NumberFilter(
        field_name="created_time", lookup_expr='second__gt')
    #second__gt ,minute__gt,hour__gt,day__gt,month__gt,year_gt
    stop = django_filters.NumberFilter(
        field_name="created_time", lookup_expr='second__lt')
    created_time = django_filters.DateTimeFilter()
    class Meta:
        model = Server
        fields = ['server_name', 'brand', 'cpus',
                  'ram', 'disk', 'start', 'stop','created_time']


class ServerViewSet(ModelViewSet):
    """ 服务器类视图类 """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    # 一指定过滤字段
    #filter_fields =('server_name','brand')#设置过滤字段,使用方法http://127.0.0.1:8000/servers/?brand=hp&server_name=data-serve
    # 二指定过滤类，应对复杂过滤
    filter_class = ServerFilter
    ordering = ("-created_time",)  # 设置默认排序类，按照创建时间从大到小排列

    search_fields = ("brand","cpus","ram","disk")#此方法用于模糊查询http://127.0.0.1:8000/servers/?search=64,hp,5000多条件查询时逗号分隔

    ordering_fields = ('cpus','ram','disk')#http://127.0.0.1:8000/servers/?ordering=ram,disk,先按照ram从小到大排序，接着按着disk从小到达排序