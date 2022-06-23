from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.serializers import BlogSerializer
from .models import Blog
# Create your views here.
class BlogView(APIView):
    def get(self, request):
        user = request.user
        blog = Blog.objects.filter(user=user)
        return Response(BlogSerializer(blog, many=True).data,status=status.HTTP_200_OK)
    def delete(self, request):
        pass