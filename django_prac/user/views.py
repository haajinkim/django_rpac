from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponse
from rest_framework import status
from.serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout
# Create your views here.
class Loginview(APIView):
    def get(self, requset):
        return Response ({"messsge":"성공!"})

    def post(self, request):
        user = authenticate(request, **request.data)
        if user:
            login(request, user)
            response = HttpResponse('blah')
            response.set_cookie('cookie_name', 'cookie_value')
            # return Response({"messge":"로그인 성공!"},status=status.HTTP_200_OK)
            return response
        return Response({"messge":"존재하지않는 사용자거나 비밀번호가 틀립니다!"},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        logout(request)
        return Response({"messge":"로그아웃 성공!"},status=status.HTTP_200_OK)

class Userview(APIView):
    def get(self, request):
        pass
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response(user_serializer.data,status=status.HTTP_200_OK)

