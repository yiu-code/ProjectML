from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse
from api.forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login, logout
from .Recommender import Recommender

from django.http import HttpRequest
from django.template import RequestContext
from .models import User, Product
from rest_framework.response import Response
from rest_framework.views import APIView
# from .serializers import ArticleSerializer
# Create your views here.


def PreInfoKnn(request):
    return render(request, 'algorithmDisclaimer.html')

# this path is for entering the algorithm view. however no user is selected therefore it returns top 10 recommend items
def TopRecommendation(request):
    dev = User.objects.all().filter(jobtitle = "Developer")      
    des = User.objects.all().filter(jobtitle = "Designer")
    off = User.objects.all().filter(jobtitle = "Office")
    test = Recommender(5)
    products = test.GetTopBorrowedItems(10)
        
    return render(request, 'topItem.html', {'products': products, 'developers': dev, 'designers': des, 'office': off})

def Knn(request, userId):
    #get selected user information 
    query = connection.cursor().execute("SELECT * FROM api_user WHERE id =" + str(userId))
    currentUser = query.fetchall()

    #Get UserHistory
    recommender = Recommender(userId)
    hist, haveHist = recommender.CheckAndGetHistory()
    recommendList = recommender.Knn(hist)

    print(currentUser)
    dev = User.objects.all().filter(jobtitle = "Developer")      
    des = User.objects.all().filter(jobtitle = "Designer")
    off = User.objects.all().filter(jobtitle = "Office") #required for side menu
    return render(request, 'knn.html', {'developers': dev, 'designers': des, 'office': off, 'currentUser': currentUser, 'history': haveHist, 'recommend': recommendList})

@login_required(login_url='/')
def Home(request):
    id = request.user.id
    recommender = Recommender(id)
    topItems = recommender.GetTopBorrowedItems(4)

    idList = []
    Recommended = []
    for item in topItems:
        idList.append(item[0])
    for item in idList:
        query = connection.cursor().execute("SELECT * FROM api_product WHERE id =" + str(item))
        product = query.fetchall()
        Recommended.append(product)
    print(Recommended)
    return render(request, "home.html", {'product' : Recommended})

def Register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = RegistrationForm()   
    return render(request, 'register.html', {'form': form})

def login_view(request):
    next = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/home')
    return render(request, "login.html", {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'api/home.html',
        {
            'title':'Home Page',
            
        }
    )

## Webpagina die Db info laat zien ##

def products(request):
    Product_list = Product.objects.all() ## Product List = Variabel, Objects.all() pakt alle producten in de DB ##
    return render(request, 'api/products.html', {'Product': Product_list}) 

def productsRecommended(request, userId):
#get selected user information 
    query = connection.cursor().execute("SELECT * FROM api_user WHERE id =" + str(userId))
    currentUser = query.fetchall()
    print()

    #Get UserHistory
    recommender = Recommender(userId)
    hist, haveHist = recommender.CheckAndGetHistory()
    recommendList = recommender.Knn(hist)
    #Gooit het resultaat van Id's in een lijst en pakt alle producten met die Id's. 
    idList = []
    Recommended = []
    for item in recommendList:
        idList.append(item[0])
    for item in idList:
        query = connection.cursor().execute("SELECT * FROM api_product WHERE id =" + str(item))
        product = query.fetchall()
        Recommended.append(product)

    return render(request, 'api/products.html', {'Product': Recommended, 'Recommended': True})

def productDetail(request, productId):
        
        
        return render(request, 'api/detailPage.html') 
