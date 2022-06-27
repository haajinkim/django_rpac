from django.db import models
from user.models import User
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)
    
class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    edit_date = models.DateTimeField(auto_now=True)
    exposure_end = models.DateTimeField(auto_now_add=False)

    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.ForeignKey(Blog,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    desc = models.CharField(max_length=50)