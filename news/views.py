from rest_framework import viewsets
from .models import NewsArticle
from .serializers import NewsArticleSerializer

class NewsArticleViewSet(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all().order_by('-created_at')
    serializer_class = NewsArticleSerializer
