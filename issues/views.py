# issues.views.py
from rest_framework.viewsets import ModelViewSet

from .models import Issue
from .serializers import IssueSerializer

# Create your views here.
class IssueModelViewSet(ModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()
    