from django.db import models

class BJPdata(models.Model):
    Date=models.DateTimeField(auto_now=True)
    Designation=models.CharField(max_length=64,blank=True)
    Name =models.CharField(max_length=64,blank=True)
    Place=models.CharField(max_length=64,blank=True)
    Contact=models.CharField(max_length=64,blank=True)
    Sess=models.CharField(max_length=20)
