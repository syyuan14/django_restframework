""" 节流控制 """
'''
import time
from rest_framework.throttling import BaseThrottle
Visit_List = {}
class BlogVisitThrottle(object):
    """ 博客访问节流"""

    def __init__(self):
        self.histroy = None

    def allow_request(self, request, view):
        """ 自定义限流方法"""
        # 获取远程IP地址
        remote_addr = request.META.get("REMOTE_ADDR")
        # print(request.META)
        c_time = time.time()
        # 获取最近访问次数
        if remote_addr not in Visit_List:
            # 如果最近没有访问则返回True
            Visit_List[remote_addr] = [c_time, ]
            return True
        # 如果最近有访问：
        # 判断最近访问时间是否在当前访问时间-60秒内
        # 如果不在则pop掉，一直到list存放的最近访问时间都在60秒内
        history = Visit_List.get(remote_addr)
        self.history = history
        while history and history[-1] < c_time-10:
            history.pop()
        # 判断list的元素个数
        # 如果大于等于3个则返回false
        if len(history) >= 3:
            return False
        # 否则返回True
        history.insert(0, c_time)
        return True

    def wait(self):
        """ 自定义返回数据，此处用来返回还有几秒可以继续访问"""
        c_time = time.time()
        return 10-float(c_time - self.history[-1])

'''

'''
import time
from rest_framework.throttling import BaseThrottle
Visit_List = {}
class BlogVisitThrottle(BaseThrottle):
    """ 继承Basehrottle博客访问节流"""

    def __init__(self):
        self.histroy = None

    def allow_request(self, request, view):
        """ 自定义限流方法"""
        # 获取远程IP地址
        #remote_addr = request.META.get("REMOTE_ADDR")
        remote_addr = self.get_ident(request)
        # print(request.META)
        c_time = time.time()
        # 获取最近访问次数
        if remote_addr not in Visit_List:
            # 如果最近没有访问则返回True
            Visit_List[remote_addr] = [c_time, ]
            return True
        # 如果最近有访问：
        # 判断最近访问时间是否在当前访问时间-60秒内
        # 如果不在则pop掉，一直到list存放的最近访问时间都在60秒内
        history = Visit_List.get(remote_addr)
        self.history = history
        while history and history[-1] < c_time-10:
            history.pop()
        # 判断list的元素个数
        # 如果大于等于3个则返回false
        if len(history) >= 3:
            return False
        # 否则返回True
        history.insert(0, c_time)
        return True

    def wait(self):
        """ 自定义返回数据，此处用来返回还有几秒可以继续访问"""
        c_time = time.time()
        return 10-float(c_time - self.history[-1])
'''
'''
from rest_framework.throttling import SimpleRateThrottle
class BlogVisitThrottle(SimpleRateThrottle):
    """ 继承SimpleRateThrottle类实现访问节流"""
    scope = 'Luffy'  # 指定settings.py 文件中的key值
    def get_cache_key(self, request, view):
        """ 此方法的返回值表示的是按什么对用户访问做限制，例如此例是按照匿名用户的IP来做限制的"""
        return self.get_ident(request)
'''
from rest_framework.throttling import SimpleRateThrottle

class BlogVisitThrottle(SimpleRateThrottle):
  """ 继承SimpleRateThrottle来实现对登陆用户进行访问节流"""
  scope = 'username'
  def get_cache_key(self,request,view):
    return request.user.username