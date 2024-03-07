from rest_framework import generics
from .models import Article, News
from .serializers import ArticleSerializer, NewsSerializer


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

