from django.urls import path
from . import views


urlpatterns =  [
    path('home', views.Home, name="home-page"),
    path('', views.Login, name="login-page")
]