# commments.views.py
from rest_framework.viewsets import ModelViewSet

from .models import Comment
from .serializers import CommentSerializer

# Create your views here.
class CommentModelViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()