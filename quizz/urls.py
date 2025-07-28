from django.urls import path
from .views import QuizListView, QuizDetailView

urlpatterns = [
    path('api/quizzes/', QuizListView.as_view(), name='quiz-list'),
    path('api/quizzes/<int:quiz_id>/', QuizDetailView.as_view(), name='quiz-detail'),
]
