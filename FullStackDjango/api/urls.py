from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "api"

urlpatterns =  [
    path('home', views.Home, name="home-page"),
    path('register/', views.Register, name="registration-page"),
    path('dbData', views.dbData, name='dbData'),
    path('', views.login_view, name="login"),
    path('logout', views.logout_view),
    path('products', views.dbData, name='products'),
    path('knn', views.PreInfoKnn, name="disclamer-algoritm-page"),
    path('knn/index', views.TopRecommendation, name="algorithm-page"),
    path('knn/<int:userId>/', views.Knn, name="knn-page")
]