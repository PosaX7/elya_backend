from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from quizz.models import Quiz, QuizQuestion, QuizAnswer
from .serializers import QuizSerializer, QuizQuestionSerializer

class QuizListView(APIView):
    def get(self, request):
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)

class QuizDetailView(APIView):
    def get(self, request, quiz_id):
        questions = QuizQuestion.objects.filter(quiz__id=quiz_id)
        serializer = QuizQuestionSerializer(questions, many=True)
        return Response(serializer.data)
    