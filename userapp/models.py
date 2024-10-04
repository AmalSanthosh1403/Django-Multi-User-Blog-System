from django.db import models
from datetime import datetime
from django.utils import timezone

class usertbl(models.Model):
    username=models.CharField(max_length=255)
    userage=models.IntegerField()
    userplace=models.CharField(max_length=255)
    useremail=models.EmailField()
    userpassword=models.CharField(max_length=255)
    


class posttbl(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    likes=models.IntegerField(default=0)
    likeddetails=models.ManyToManyField(usertbl,related_name='liked_posts',blank=True)
    userid=models.ForeignKey(usertbl,on_delete=models.CASCADE)
    

class commenttbl(models.Model):
    commentcontent=models.CharField(max_length=500)
    created_updated_at = models.DateTimeField(auto_now=True)
    postidPF=models.ForeignKey(posttbl,on_delete=models.CASCADE,null=True,blank=True)
    useridUF=models.ForeignKey(usertbl,on_delete=models.CASCADE,null=True,blank=True)


