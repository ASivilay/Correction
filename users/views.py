# users.views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer

class UserModelViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    #permission_classes = [IsAuthenticated]

    '''
    def get_queryset(self):
        return User.objects.all()
    '''