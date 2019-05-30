from django.urls import path
from .views import ArticleView
from . import views
from django.contrib.auth.views import LoginView


app_name = "articles"

urlpatterns =  [
    path('home', views.Home, name="home-page"),
    path('register/', views.Register, name="registration-page"),
    path('dbData', views.dbData, name='dbData'),
    path('', views.login_view, name="login"),
    path('logout', views.logout_view),
    #Ik wees eerlijk, ik heb niet echt een idee
    path('articles/<int:pk>', ArticleView.as_view()),
    
]