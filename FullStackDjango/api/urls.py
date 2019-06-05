from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "api"

urlpatterns =  [
    path('home', views.Home, name="home-page"),
    path('register/', views.Register, name="registration-page"),
    path('products', views.dbData, name='products'),
    path('', LoginView.as_view(template_name='login.html'), name="login"),
    path('knn', views.PreInfoKnn, name="disclamer-algoritm-page"),
    path('knn/index', views.TopRecommendation, name="algorithm-page"),
    path('knn/<int:userId>/', views.Knn, name="knn-page")
]