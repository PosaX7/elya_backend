from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, ExerciseViewSet, LibraryViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'libraries', LibraryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
