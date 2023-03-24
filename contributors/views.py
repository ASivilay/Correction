# contributors.views.py
from rest_framework.viewsets import ModelViewSet

from .models import Contributor
from .serializers import ContributorSerializer

# Create your views here.
class ContributorModelViewSet(ModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()