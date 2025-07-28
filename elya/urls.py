from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from programmes.views import ProgrammeViewSet

router = DefaultRouter()
router.register(r'programmes', ProgrammeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('quizz.urls')),
    path('api/', include('news.urls')),
    path('api/guide/', include('guide.urls')),
    path('api/search/', include('search.urls')),
    path('api/', include('comments.urls')),
    path('api/stats/', include('stats.urls')),
]
