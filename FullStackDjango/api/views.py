from django.shortcuts import render, redirect
from django.http import HttpResponse
from api.forms import RegistrationForm

from django.http import HttpRequest
from django.template import RequestContext
from .models import Article, Author, Product, User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArticleSerializer
# Create your views here.

def Algorithm(request):
    products = Product.objects.all()
    users = User.objects.all()
    return render(request, 'knn.html', {'products': products, 'users': users})

def Login(request):
    return HttpResponse('<h1>Login Page</h1>')

def Home(request):
    return render(request, 'home.html')

def Register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = RegistrationForm()   
    return render(request, 'register.html', {'form': form})





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
def dbData(request):
    Product_list = Product.objects.all() ## Article List = Variabel, Objects.all() pakt alle Artikelen in de DB ##
    return render(request, 'api/products.html', {'Product': Product_list}) ##Op de HTML bestand in Article een variable die hier de Article_list variable is ##


### BASIS API ###

class ArticleView(APIView):
    # GET METHOD - Laat de Artikelen zien. (In JSON natuurlijk)
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})
    # POST METHOD - Gaat probably niet gebruikt worden in project zelf, maar laat zien hoe je meerdere methods aan 1 ding doet. - Maakt het mogelijk om een artikel te adden via JSON.
    def post(self, request):
        article = request.data.get('article')

        # Create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})
    def delete(self, request, pk):
    # Get object with this pk
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204) 
