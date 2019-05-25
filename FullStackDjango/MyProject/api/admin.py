from django.contrib import admin
from .models import User
# Register your models here.
CustomUser = User
admin.site.register(CustomUser)
