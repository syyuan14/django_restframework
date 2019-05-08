""" 序列化类 """
from rest_framework import serializers, exceptions
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    """ 用户序列化类"""
    sex = serializers.CharField(source="get_sex_display")
    user_type = serializers.CharField(source="get_user_type_display")

    class Meta:
        model = User
        fields = ("email",  "name", "sex", "user_type", "mobile", "password")

    def create(self, validated_data):
        """ 创建用户 """
        # print(validated_data)
        try:
            user = User.objects.create(email=validated_data["email"], name=validated_data["name"],
                                       sex=validated_data["get_sex_display"], user_type=validated_data["get_user_type_display"],
                                       mobile=validated_data["mobile"]
                                       )
            user.set_password(validated_data["password"])
        except:
            raise exceptions.ValidationError("输入数据有误")
        user.save()
        return user

    def update(self, instance, validated_data):
        """ 更新用户 """
        # raise_errors_on_nested_writes('update', self, validated_data)
        print(instance.email)
        user = User.objects.filter(email=instance.email)
        user.update(email=validated_data["email"], name=validated_data["name"],
                    sex=validated_data["get_sex_display"], user_type=validated_data["get_user_type_display"],
                    mobile=validated_data["mobile"])

        user = User.objects.get(email=instance.email)
        user.set_password(validated_data["password"])
        user.save()
        return user
