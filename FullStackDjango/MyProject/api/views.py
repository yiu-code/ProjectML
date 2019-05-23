from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Author
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArticleSerializer
# Create your views here.

def Login(request):
    return HttpResponse('<h1>Login Page</h1>')

def Home(request):
    return HttpResponse('<h1>Home Page </h1>')

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