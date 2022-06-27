from rest_framework import serializers
from .models import Blog,Category,Comment
from user.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category"]

class BlogSerializer(serializers.ModelSerializer):
    category =CategorySerializer(read_only=True)
    comment =serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField()
    def get_comment(self,obj):
        comment_list =[{"comment_desc":comment.desc} for comment in obj.comment_set.all()]
        return comment_list
    def get_user(self,obj):
        return obj.user.username
    class Meta:
        model = Blog
        fields = ["user","category","comment","title","desc","create_date","edit_date",
                        "edit_date","exposure_end"]

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields =["user","create_date","desc"]
        