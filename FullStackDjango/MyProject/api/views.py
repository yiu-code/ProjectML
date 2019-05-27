from django.shortcuts import render, redirect
from django.http import HttpResponse
from api.forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# def Login(request):
#     return HttpResponse('<h1>Login Page</h1>')

@login_required
def Home(request):
    return HttpResponse('<h1>Home Page </h1>')

def Register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = RegistrationForm()   
    return render(request, 'register.html', {'form': form})



