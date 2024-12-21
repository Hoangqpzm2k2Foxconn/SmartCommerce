
from rest_framework import generics
from ..models import Software
from .serializers import SoftwareSerializer

class SoftwareListView(generics.ListCreateAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer

class SoftwareDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
