# issues.models.py
from django.db import models

from users.models import User
from projects.models import Project

# Create your models here.
class Issue(models.Model):
        #issue_id = models.IntegerField(primary_key=True)
        title = models.CharField(max_length=255)
        description = models.CharField(max_length=255)
        tag = models.CharField(max_length=255)
        priority = models.CharField(max_length=255)
        project_id = models.IntegerField()
        #project_id = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='project', null=True)
        status = models.CharField(max_length=255)
        author_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='author', null=True)
        assignee_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='assignee', null=True)
        created_time = models.DateTimeField(auto_now_add=True)