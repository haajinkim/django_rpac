from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.serializers import BlogSerializer, CommentSerializer
from .models import Blog,Category, Comment
from user.models import User
from rest_framework import permissions
from django.db.models.query_utils import Q
from django.utils import timezone
# Create your views here.
class BlogView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        user = request.user
        print(timezone.now())
        blog = Blog.objects.filter(Q(user=user) & Q(exposure_end__gte=timezone.now()))
        # 작성자가 유저이며 만료날짜가 전까지인 게시물만 출력
        return Response(BlogSerializer(blog, many=True).data,status=status.HTTP_200_OK)
    def post(self, request):
        category = int(request.data.get("category", ""))
        category_qs = Category.objects.get(id=category)
        user =User.objects.get(id=request.user.id)
        blogserializer =BlogSerializer(data=request.data)
        if blogserializer.is_valid():
            blogserializer.save(category=category_qs,user=user)
            return Response(status=status.HTTP_200_OK)
        return Response(blogserializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, blog_id):    
        blog = Blog.objects.get(id=blog_id)
        blogserializer = BlogSerializer(blog, data=request.data, partial=True)
        if blogserializer.is_valid():
            # validator를 통과했을 경우 데이터 저장
            blogserializer.save() 
            return Response(status=status.HTTP_200_OK)
        return Response(blogserializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    def delete(self,request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        blog.delete()
        return Response({"messege":"삭제가 완료 되었습니다"},status=status.HTTP_200_OK)

class CommentView(APIView):
    def get(self, request, title_id):
        comment = Comment.objects.filter(title_id=title_id)
        return Response(CommentSerializer(comment, many=True).data,status=status.HTTP_200_OK)
    def post(self, request,title_id):
        user = request.user.id
        title_get = Blog.objects.get(id=title_id)
        user =User.objects.get(id=user)
        commentserializer = CommentSerializer(data=request.data)
        if commentserializer.is_valid():
            commentserializer.save(title=title_get, user=user)
            return Response(status=status.HTTP_200_OK)
        return Response(commentserializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, comment_id):
        comment_get = Comment.objects.get(id=comment_id)
        commentserializer = CommentSerializer(comment_get, data=request.data, partial=True)
        if commentserializer.is_valid():
            commentserializer.save() 
            return Response({"messege":"수정이 완료 되었습니다"},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return Response({"messege":"삭제가 완료 되었습니다"},status=status.HTTP_200_OK)      