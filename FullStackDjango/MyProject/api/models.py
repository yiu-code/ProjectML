from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from rest_framework import serializers

# Create your models here.
#Models + __str__ dat ervoor zorgt dat hij bij een call de naam laat zien.
class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  def __str__(self):
      return self.name



class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.PROTECT)
    def __str__(self):
        return self.title
   


