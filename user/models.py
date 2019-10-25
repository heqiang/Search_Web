from django.db import models

# Create your models here.
from django.db import models
import django.utils.timezone as timezone
from django.db.backends.mysql.base import DatabaseFeatures # 关键设置
DatabaseFeatures.supports_microsecond_precision = False # 关键设置

class  User(models.Model):
    gender=(
        ('male',"男"),
        ('female',"女")
    )
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=255)
    email=models.EmailField(unique=True,blank=True)
    sex=models.CharField(max_length=32,choices=gender,default='男',blank=True)
    job=models.CharField(max_length=128,blank=True)
    description=models.TextField(blank=True)
    createtime=models.DateTimeField(auto_now_add=True)
    headimg=models.FileField(upload_to="headimg",blank=True)
class  Collect(models.Model):
    user=models.ForeignKey('User',on_delete=models.CASCADE)
    collecttitle=models.CharField(max_length=255)
    collecturl=models.CharField(max_length=128)
    collecttime=models.DateTimeField(auto_now_add=True)
class Search(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    searchtitle = models.CharField(max_length=255)
    searchurl = models.CharField(max_length=128,blank=True)
    searchtime = models.DateTimeField(auto_now_add=True)