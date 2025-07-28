from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Exercise, Library
from .serializers import CourseSerializer, ExerciseSerializer, LibrarySerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def exercises(self, request, pk=None):
        course = self.get_object()
        exercises = course.get_related_exercises()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    @action(detail=True, methods=['get'])
    def course(self, request, pk=None):
        exercise = self.get_object()
        course = exercise.course
        serializer = CourseSerializer(course)
        return Response(serializer.data)


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
