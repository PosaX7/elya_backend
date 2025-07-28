from rest_framework import serializers
from quizz.models import Quiz, QuizQuestion, QuizAnswer

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'category', 'subgroup', 'difficulty']

class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswer
        fields = ['id', 'text', 'number']

class QuizQuestionSerializer(serializers.ModelSerializer):
    answers = QuizAnswerSerializer(source='quizanswer_set', many=True)

    class Meta:
        model = QuizQuestion
        fields = ['id', 'text', 'answers']
