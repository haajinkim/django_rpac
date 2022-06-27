from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('blog/',views.BlogView.as_view()),
    path('blog/<int:blog_id>/',views.BlogView.as_view()),
    path('comment/',views.CommentView.as_view()),
    path('comment/<int:title_id>/',views.CommentView.as_view()),
    path('comment/put<int:comment_id>/',views.CommentView.as_view()),
    path('comment/delete<int:comment_id>/',views.CommentView.as_view()),
]
