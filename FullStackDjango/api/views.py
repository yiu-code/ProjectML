from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db import connection
from django.http import HttpResponse
from api.forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login, logout
from .Recommender import Recommender

from django.http import HttpRequest
from django.template import RequestContext
from .models import User, Product, Cart, CartItem, Cart_Items
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


def cart(request):
    #cart = CartItem.objects.all()
    #print(cart)

    double_list = []
    items_in_cart = []
    query = connection.cursor().execute("SELECT p.title, ci.quantity, p.price, c.total FROM api_product AS p JOIN api_cartitem AS ci ON p.id = ci.product_id JOIN api_cart AS c ON ci.product_id = c.product_id ORDER BY p.title, ci.quantity, c.total;")
    cartList = query.fetchall()
    double_list.append(cartList)
    for items in double_list:
        for single_item in items:
            items_in_cart.append(single_item)

    print(items_in_cart)
    context = {"cart": cart}
    template = "shoppingcart.html"
    return render(request, template, context)


def add_to_cart(request):
    pass

def remove_from_cart(request):
    pass

def update_cart(request, slug):
   pass

def complete(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'complete.html'
    )

## Webpagina die Db info laat zien ##

def products(request, selectedCategory):
    if selectedCategory == '0':
        Product_list = Product.objects.all() ## Product List = Variabel, Objects.all() pakt alle producten in de DB ##
    else: 
        query = connection.cursor().execute("SELECT * FROM api_product WHERE category = '" + str(selectedCategory) + "'")
        Product_list = query.fetchall()
        print(Product_list)
        print(Product_list[0])

    page = request.GET.get('page', 1)
    paginator = Paginator(Product_list, 10)
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)

    
    query = connection.cursor().execute("SELECT category FROM api_product GROUP BY category")
    categories = query.fetchall()
    if selectedCategory == '0':
        return render(request, 'api/products.html', {'Product': product, 'Categories': categories, 'enabledCategories': False}) 
    else:
        return render(request, 'api/products.html', {'Product': product, 'Categories': categories, 'enabledCategories': True, 'currentCategorie': str(selectedCategory)}) 
    


def productsRecommended(request):
    #get selected user information 
    id = request.user.id
    query = connection.cursor().execute("SELECT * FROM api_user WHERE id =" + str(id))
    currentUser = query.fetchall()
    print()

    #Get UserHistory
    recommender = Recommender(id)
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
