from django.db import models

class client(models.Model):
    name=models.CharField(max_length=64)

    def __str__(self):
        return (self.name)

class report(models.Model):
    client=models.ForeignKey(client,on_delete=models.CASCADE)
    name=models.CharField(max_length=128)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return (self.name)

class user(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    pas=models.CharField(max_length=15)
    status = models.BooleanField(default=True)
    reports=models.ManyToManyField(report,blank=True)

    def rep(self):
        return [r.name for r in self.reports.all()]

    def __str__(self):
        return self.name
