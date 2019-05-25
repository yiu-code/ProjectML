from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django import forms


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff= False, is_admin=False, **extra_fields):
        if not email :
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(email = self.normalize_email(email), **extra_fields)
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using= self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True, is_admin=True)
        return user
    
    

class User(AbstractBaseUser):
    Job_title_choices = [('frontend', 'Frontend developer'),
                         ('backend', 'Backend developer'),
                         ('datascience', 'Datascience')
                        ]

    email = models.EmailField(max_length=255, unique=True)
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
    


    