from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField
    first_name = models.CharField
    last_name = models.CharField
    email = models.EmailField
    password = models.CharField

    def __str__(self):
        return self.name
