from rest_framework import viewsets
from .models import Programme
from .serializers import ProgrammeSerializer

class ProgrammeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
