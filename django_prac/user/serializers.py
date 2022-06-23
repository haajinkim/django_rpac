from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email","password","fullname"]

        extra_kwargs = {
            "password" : {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password","")
        #받아온 데이터에서 password 만빼내서 따로저장
        user =User(**validated_data)
        user.set_password(password)
        user.save()
        return user
