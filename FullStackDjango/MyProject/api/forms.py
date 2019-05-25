from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    

    class Meta:
        model = User
        fields = ('email', 'firstname', 'lastname', 'jobtitle', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']
        

        if commit:
            user.save()
        return user
