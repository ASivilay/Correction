# contributors.models.py
from django.db import models
from projects.models import Project
from users.models import User

class Contributor(models.Model):
    #user = models.IntegerField
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contributor")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="contributor")
    #permission = models.TextChoices[('True', 'Yes'),('False', 'No')]
    role = models.CharField(max_length=255)