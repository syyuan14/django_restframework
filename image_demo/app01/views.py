""" 视图"""
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser

from .models import Usericon


class UsericonSerializer(serializers.ModelSerializer):
    """ 序列化类"""
    class Meta:
        model = Usericon
        fields = "__all__"


class ImageView(APIView):
    """ 图片视图 """
    parser_classes = (MultiPartParser,)

    def get(self, request):
        """ 请求用户头像url"""
        images = Usericon.objects.all()
        serializer = UsericonSerializer(instance=images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """ 获得上传的用户头像"""
        serializer = UsericonSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print("hello")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
