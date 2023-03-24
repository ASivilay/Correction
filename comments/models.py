# comments.models.py
from django.db import models

from users.models import User
from issues.models import Issue

# Create your models here.
class Comment(models.Model):
    #comment_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="issue")
    created_time = models.DateTimeField(auto_now_add=True)