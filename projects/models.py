# projects.models.py
from django.db import models

from users.models import User

class Project(models.Model):
    #project_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
#on_delete=models.SET_NULL,