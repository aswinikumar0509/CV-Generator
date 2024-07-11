from django.db import models

# Create your models here.

class Profile(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000)
    degree1 = models.CharField(max_length=100)
    degree2 = models.CharField(max_length=100)
    skills = models.TextField(max_length=1000)
    projects = models.TextField(max_length=2000)
    experience = models.TextField(max_length=2000)
    language = models.CharField(max_length=100)

