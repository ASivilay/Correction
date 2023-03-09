#from django.shortcuts import render
#from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer

# Create your views here.
#class UserViewSet(viewsets.ModelViewSet):
class UserModelViewSet(ModelViewSet):
    serializer_class = UserSerializer
    #queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.all()