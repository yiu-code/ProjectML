from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns =  [
    path('home', views.Home, name="home-page"),
    path('', LoginView.as_view(template_name='login.html'), name="login"),
    path('register/', views.Register, name="registration-page")
]