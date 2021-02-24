from django.db import models

class student(models.Model):
    Name=models.CharField(max_length=30)
    email=models.EmailField()
    pas=models.CharField(max_length=20)
    clas=models.IntegerField()
    sub1=models.IntegerField()
    sub2=models.IntegerField()
    sub3=models.IntegerField()
    sub4=models.IntegerField()
    sub5=models.IntegerField()
    sports=models.IntegerField()

    def __str__(self):
        return self.Name
