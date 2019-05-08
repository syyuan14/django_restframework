'''
""" 基于url的get传参方式：视图"""
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.versioning import QueryParameterVersioning


class UserView(APIView):
    """
    用户视图view
    """
    versioning_class = QueryParameterVersioning

    def get(self, request):
        """
        get请求
        """
        self.dispatch
        print(request.version)
        print(request.versioning_scheme)
        print(request.versioning_scheme.reverse(
            viewname="uuu", request=request))
        return HttpResponse("HELLO WORLD")
'''
'''
""" 基于url的正则表达式法获取版本号：视图"""
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.versioning import URLPathVersioning
class UserView(APIView):
    """
    用户视图view
    """
    versioning_class = URLPathVersioning

    def get(self, request, *args, **kwargs):
        """
        get请求
        """
        #self.dispatch
        print(request.version)
        print(request.versioning_scheme)
        print(request.versioning_scheme.reverse(
            viewname="uuu", request=request))
        return HttpResponse("HELLO WORLD")
'''
'''
""" 基于请求头获取版本号：视图"""
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.versioning import AcceptHeaderVersioning
from rest_framework.parsers import JSONParser

class UserView(APIView):
    """
    用户视图view
    """
    versioning_class = AcceptHeaderVersioning

    def get(self, request, *args, **kwargs):
        """
        get请求
        """
        self.dispatch
        print(request.version)
        print(request.versioning_scheme)
        print(request.versioning_scheme.reverse(
            viewname="uuu", request=request))
        return HttpResponse("HELLO WORLD")
'''
'''
""" 仅处理请求头content-type为application/x-www-form-urlencoded的请求体 """
from rest_framework.views import APIView
from rest_framework.parsers import FormParser
from rest_framework.response import Response
class UserView(APIView):
  """
  仅处理请求头content-type为application/json的请求体
  """
  parser_classes = (FormParser,)
  def post (self,request):
    return Response(request.data)
'''