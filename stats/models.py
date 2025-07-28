from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Stat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stats')
    content_type = models.CharField(max_length=100)  # e.g. 'course', 'exercise', 'quiz'
    content_id = models.PositiveIntegerField()       # ID de l'élément (cours, exo, etc.)
    action = models.CharField(max_length=100)        # e.g. 'viewed', 'completed', 'started'
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.content_type} {self.action}"
