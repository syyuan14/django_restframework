""" 自定义中间件 process_request ==> process_view ==> view ==> process_response """
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class Md1(MiddlewareMixin):
    """
    定义中间件1
    """

    def process_request(self, request):
        """ process_request """
        print("md1.process_request...")
        return HttpResponse("md1.process_request")

    def process_response(self, request, response):
        """ process_response """
        print("md1.process_response...")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        """
        callback:当前执行的视图函数
        calllback_args:当前执行的视图函数的args参数
        callback_kwargs:当前执行的视图函数的kwargs参数
        """
        print("md1.process_view")
        # return HttpResponse("md1.process_view")

    def process_exception(self, request, excepton):
        """ 
        视图函数执行发生异常时调用该函数
        """
        print("md1.process_exception")


class Md2(MiddlewareMixin):
    """
    定义中间件2
    """

    def process_request(self, request):
        """ process_request """
        print("md2.process_request...")
        # return HttpResponse("md1.process_request")

    def process_response(self, request, response):
        """ process_response """
        print("md2.process_response...")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        """
        callback:当前执行的视图函数
        calllback_args:当前执行的视图函数的args参数
        callback_kwargs:当前执行的视图函数的kwargs参数
        """
        print("md2.process_view")
        # return HttpResponse("md2.process_view")

    def process_exception(self, request, excepton):
        """ 
        视图函数执行发生异常时调用该函数
        """
        print("md2.process_exception")
