from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django import forms

from django.contrib.auth.models import AbstractBaseUser
from rest_framework import serializers
=======
from django.contrib.auth.models import AbstractBaseUser
>>>>>>> parent of b7159b70... Setup en Register

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
   


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
<<<<<<< HEAD
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    jobtitle = models.CharField(max_length=255, choices=Job_title_choices)
    firstname = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    timestamp = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    #This replaces the username field(which normally is used bij default) with email

    REQUIRED_FIELDS = []

    
    def get_full_name(self):
        return '%s %s' % (self.firstname, self.lastname)

    def get_first_name(self):
        return self.firstname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active

    objects = UserManager()

class Employee:
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    


    
=======
    
>>>>>>> parent of b7159b70... Setup en Register
