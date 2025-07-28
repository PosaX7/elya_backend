from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)  # Non obligatoire
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def word_count(self):
        return len(self.content.split())
