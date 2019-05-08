""" 测试视图"""


from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from .permissions import SuperUserPermission

class UserViewSet(ModelViewSet):
    """ 获取用户信息列表 """
    permission_classes = (SuperUserPermission,)
    queryset = User.objects.filter(user_type=1)
    serializer_class = UserSerializer
