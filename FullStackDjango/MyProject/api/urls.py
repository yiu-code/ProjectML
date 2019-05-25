from django.urls import path
from .views import ArticleView
from . import views

app_name = "articles"

urlpatterns =  [
    path('home', views.Home, name="home-page"),
    path('', views.Login, name="login-page"),
    path('register/', views.Register, name="registration-page"),
    path('', views.home, name='home'),
    path('dbData', views.dbData, name='dbData'),
    path('login', views.Login, name="login-page"),
    #Ik wees eerlijk, ik heb niet echt een idee
    path('articles/<int:pk>', ArticleView.as_view()),
]