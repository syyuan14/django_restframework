""" 视图"""
from datetime import datetime
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

from .models import Airplane
from .utils.getdata import getdatescar, getmonthscar

from rest_framework.views import APIView


class ScarDateView(APIView):
    """ 返回伤痕数目"""

    def get(self, request):
        """默认获得七天内的伤痕统计"""
        # 设定默认值
        stop_date = datetime.now()
        start_date = datetime.fromtimestamp(stop_date.timestamp() - 6*24*60*60)
        keyword = Airplane.objects.all().first().TailNumber  # 此数值为默认值，设置飞机搜索关键字
        
        begin_time = request.query_params.get("start", start_date)
        stop_time = request.query_params.get("stop", stop_date)
        keyword = request.query_params.get("keyword", keyword)  # 获取飞机的搜索关键字


        airplane = Airplane.objects.filter(Q(TailNumber=keyword) | Q(
            LineNumber=keyword) | Q(AC_ASN=keyword) | Q(AC_Variable=keyword)).first()
        if not airplane:
            raise exceptions.NotFound("查找飞机不存在")
        
        scars = getdatescar(begin_time, stop_time, airplane)
        return Response(scars, status=status.HTTP_200_OK)


class ScarMonthView(APIView):
    """ 按月份返回伤痕统计 """

    def get(self, request):
        """ 根据查询的月份返回数据"""
        #设置默认参数
        date = datetime.now()
        keyword = Airplane.objects.all().first().TailNumber  # 指定默认搜索关键字

        # date表示年份加月份,从前端url中取到例如2019-02之类的数据
        date = request.query_params.get("date",date)
        keyword = request.query_params.get("keyword",keyword)
        
        airplane = Airplane.objects.filter(Q(TailNumber=keyword) | Q(
            LineNumber=keyword) | Q(AC_ASN=keyword) | Q(AC_Variable=keyword)).first()
        if not airplane:
            raise exceptions.NotFound("查找飞机不存在")
        
        scars = getmonthscar(date, airplane)
        
        return Response(scars, status=status.HTTP_200_OK)
