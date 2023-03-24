# projects.views.py
from rest_framework.viewsets import ModelViewSet

from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsAuthorOrContributor

#from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProjectModelViewSet(ModelViewSet):    
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrContributor]

    def get_queryset(self):
        return Project.objects.filter()
    #all()
    

    """
    permission_classes_by_action = {
    'create': (permissions.IsAdminUser,),
    'list': (permissions.IsAuthenticatedOrReadOnly,),
    'retrieve': (permissions.AllowAny,),
    'update': (permissions.AllowAny,),
    'destroy': (permissions.IsAdminUser,),
    'search': (permissions.IsAuthenticated,) 
    }
    """
            
