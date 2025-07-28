from django.contrib import admin
from .models import NewsArticle

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'likes')
    search_fields = ('title', 'author')
    list_filter = ('created_at',)
