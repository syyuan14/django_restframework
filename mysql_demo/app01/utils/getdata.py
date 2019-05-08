""" 将queryset数据转换为list并格式化"""

import datetime
from datetime import timedelta
from django.db.models import Count
from rest_framework import exceptions

from app01.models import Scar


def todict(queryset, airplane):
    """补全一天伤痕统计中count为0的伤痕类型 """
    n = 5
    newlist = list(queryset)
    scars = [{'scar_type': i + 1, 'airplane': airplane, 'count': 0}
             for i in range(n)]

    if len(newlist) < n:
        for item in newlist:
            scars[item.get("scar_type") - 1]['count'] = item.get('count', 0)
        return sorted(scars, key=lambda i: i['scar_type'])
    scars = newlist
    return sorted(scars, key=lambda i: i['scar_type'])


# def formatdata(newlist, datalist):
#     """ 生成前端需要的数据格式"""
#     print(newlist)
#     if not newlist:
#         i = 0
#         while i < len(datalist):
#             datalist[i].get("data").append(0)
#             i += 1
#         return datalist
#     for item in newlist:
#         if item.get("scar_type") == 1:
#             datalist[0].get("data").append(item.get("count"))
#             continue
#         if item.get("scar_type") == 2:
#             datalist[1].get("data").append(item.get("count"))
#             continue
#         if item.get("scar_type") == 3:
#             datalist[2].get("data").append(item.get("count"))
#             continue
#         if item.get("scar_type") == 4:
#             datalist[3].get("data").append(item.get("count"))
#             continue
#         if item.get("scar_type") == 5:
#             datalist[4].get("data").append(item.get("count"))
#             continue
#         else:
#             raise exceptions.NotFound("伤痕类型不存在")
#     return datalist


def formatdata(newlist, datalist, filter_date):
    """ 生成前端需要的数据格式"""

    if not newlist:
        i = 0
        while i < len(datalist):
            datalist[i].get("data").append({"count": 0, "date": filter_date})
            i += 1
        return datalist

    def handler1(item, datalist):
        datalist[0].get("data").append(
            {"count": item.get("count"), "date": filter_date})
        return datalist

    def handler2(item, datalist):
        datalist[1].get("data").append(
            {"count": item.get("count"), "date": filter_date})
        return datalist

    def handler3(item, datalist):
        datalist[2].get("data").append(
            {"count": item.get("count"), "date": filter_date})
        return datalist

    def handler4(item, datalist):
        datalist[3].get("data").append(
            {"count": item.get("count"), "date": filter_date})
        return datalist

    def handler5(item, datalist):
        datalist[4].get("data").append(
            {"count": item.get("count"), "date": filter_date})
        return datalist

    switcher = {
        1: handler1,
        2: handler2,
        3: handler3,
        4: handler4,
        5: handler5,
    }

    def dispatch(item, datalist):
        handler = switcher[item.get("scar_type")]
        return handler(item, datalist)

    for item in newlist:
        if item.get("scar_type") not in range(1, 6):
            raise exceptions.NotFound("伤痕类型不存在")
        else:
            datalist = dispatch(item, datalist)

    return datalist


def getdatescar(start, stop, airplane):
    """ 获取指定日期的时间"""
    # 获取查询的飞机信息
    airplane_obj = {
        "TailNumber": None,
        "LineNumber": None,
        "AC_ASN": None,
        "AC_Variable": None,
    }
    for k in airplane_obj:
        airplane_obj[k] = getattr(airplane, k)

    datalist = [
        {"name": "Crack",
         "type": "line",
         "scar_type": 1,
         "airplane": airplane_obj,
         "data": []
         },
        {"name": "Perforation",
         "type": "line",
         "scar_type": 2,
         "airplane": airplane_obj,
         "data": []
         },
        {"name": "Rivets",
         "type": "line",
         "scar_type": 3,
         "airplane": airplane_obj,
         "data": []
         },
        {"name": "Scartch",
         "type": "line",
         "scar_type": 4,
         "airplane": airplane_obj,
         "data": []
         },
        {"name": "Flake",
         "type": "line",
         "scar_type": 5,
         "airplane": airplane_obj,
         "data": []
         },
    ]
    # 获取字符串格式的起止日期
    start_date = start
    stop_date = stop
    airplane_id = airplane.id
    if not isinstance(start_date, datetime.datetime) or not isinstance(stop_date, datetime.datetime):
        # 将字符串格式的日期转化为datetime,并计算出要取出多少天的数据
        try:
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            stop_date = datetime.datetime.strptime(stop_date, "%Y-%m-%d")
        except:
            raise exceptions.ParseError("输入日期错误")

    days = (stop_date-start_date).days

    filter_date_timestamp = start_date.timestamp()  # 将查询起始时间转换为时间戳
    while days >= 0:
        filter_date = datetime.datetime.fromtimestamp(
            filter_date_timestamp)  # 将所要查询的日期时间戳格式转为datetime
        scar = Scar.objects.filter(airplane_id=airplane_id).filter(c_date__year=filter_date.strftime("%Y")).filter(c_date__day=filter_date.strftime("%d")).values(
            'scar_type').annotate(count=Count('scar_type')).values('scar_type', 'count', 'airplane')
        # 当天什么伤痕类型都没有
        if not scar:
            datalist = formatdata(
                scar, datalist, filter_date.strftime("%Y-%m-%d"))
            filter_date_timestamp = filter_date.timestamp()+24*60*60  # 时间加一天
            days -= 1
            continue

        scar = todict(scar, airplane_id)  # 得到补全后的dict(一天的数据)

        datalist = formatdata(scar, datalist, filter_date.strftime(
            "%Y-%m-%d"))  # 得到前端需要的数据类型(一天的数据)
        filter_date_timestamp = filter_date.timestamp()+24*60*60  # 时间减一天
        days -= 1

    return datalist


def getmonthscar(date, airplane):
    """ 根据查询月份返回数据 """
    if not isinstance(date, datetime.datetime):
        try:
            date = datetime.datetime.strptime(date, "%Y-%m")
        except:
            raise exceptions.ParseError("输入日期错误")
    scar = Scar.objects.filter(airplane=airplane).filter(c_date__year=date.strftime("%Y")).filter(c_date__month=date.strftime("%m")).values(
        'scar_type').annotate(count=Count('scar_type')).values('scar_type', 'count', 'airplane')
    scar = todict(scar, airplane.id)
    for item in scar:
        item["airplane"] = {
            "TailNumber": airplane.TailNumber,
            "LineNumber": airplane.LineNumber,
            "AC_ASN": airplane.AC_ASN,
            "AC_Variable": airplane.AC_Variable,
        }
    return scar
