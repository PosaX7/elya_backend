from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from guide.models import Course, Exercise, Library
from news.models import NewsArticle
from quizz.models import Quiz
from .pagination import SearchPagination

class GlobalSearchView(APIView):
    pagination_class = SearchPagination()

    def get(self, request):
        query = request.GET.get('q', '')
        if not query:
            return Response({'error': 'Une requête est requise via ?q=...'}, status=status.HTTP_400_BAD_REQUEST)

        # Fusionner tous les résultats dans une seule liste avec un identifiant de type
        combined_results = []

        # Cours
        for item in Course.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)):
            combined_results.append({'type': 'course', 'id': item.id, 'title': item.title})

        # Exercices
        for item in Exercise.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)):
            combined_results.append({'type': 'exercise', 'id': item.id, 'title': item.title})

        # Articles
        for item in NewsArticle.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)):
            combined_results.append({'type': 'article', 'id': item.id, 'title': item.title})

        # Quizz
        for item in Quiz.objects.filter(title__icontains=query):
            combined_results.append({'type': 'quiz', 'id': item.id, 'title': item.title})

        # Bibliothèques
        for item in Library.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)):
            combined_results.append({'type': 'library', 'id': item.id, 'title': item.title})

        # Paginer la liste fusionnée
        page = self.pagination_class.paginate_queryset(combined_results, request, view=self)
        return self.pagination_class.get_paginated_response(page)
