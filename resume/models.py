from django.db import models


# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=40)
    domain = models.CharField(max_length=40)
    mobile = models.CharField(max_length=15)
    mail = models.TextField()
    image = models.ImageField(upload_to='images/')
    skill = models.TextField()
    about = models.TextField()
    hobby = models.TextField()
    address = models.TextField()
    password = models.CharField(max_length=30)
    project_name = models.TextField()
    project_description = models.TextField()
    summary = models.TextField()
    language = models.TextField()
    college = models.TextField()
    passout = models.TextField()
    cgpa = models.TextField()

