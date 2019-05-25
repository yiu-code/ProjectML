from django.db import models

# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=100)
    brand = models.TextField(max_length=20)
    image = models.TextField()
    price = models.IntegerField()