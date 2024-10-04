from django.db import models

class admintbl(models.Model):
    adminname=models.CharField(max_length=255)
    adminemail=models.EmailField()
    adminpassword=models.CharField(max_length=150)