from django.db import models

class categoryContent(models.Model):
    tag=models.CharField(max_length=100)
    description = models.TextField(default=None)
    img = models.FileField(upload_to="uploads")
