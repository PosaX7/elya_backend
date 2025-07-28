from django.db import models
from django.contrib.auth.models import User

class QuizCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class QuizSubGroup(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE, related_name='subgroups')

    def __str__(self):
        return f"{self.category.name} - {self.name}"

class DifficultyLevel(models.Model):
    level = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return f"Niveau {self.level}"

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    subgroup = models.ForeignKey(QuizSubGroup, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    correct_answer_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.text[:50]

class QuizAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=300)
    number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Réponse {self.number}: {self.text}"

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - Score: {self.score}"
