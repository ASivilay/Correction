# projects.models.py
from django.db import models

from users.models import User
#from contributors.models import Contributor

class Project(models.Model):
    #project_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)#, related_name="author")
    contributors = models.ManyToManyField(User, through="Contributor")
    
#on_delete=models.SET_NULL,