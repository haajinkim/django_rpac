from rest_framework import serializers
from .models import Blog,Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields = ["category"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =["title","create_date","desc"]


class BlogSerializer(serializers.ModelSerializer):
    category =CategorySerializer()
    comment =serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    def get_comment(self,obj):
        comment_list =[{"comment_desc":comment.desc} for comment in obj.comment_set.all()]
        print(comment_list)
        return comment_list
    def get_user(self,obj):
        return obj.user.username
    class Meta:
        model = Blog
        fields = ["user","category","comment","title","desc","create_date","edit_date",
                        "edit_date","exposure_end"]
