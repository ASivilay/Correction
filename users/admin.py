from django.contrib import admin
from users import models

# Register your models here.
# users/admin.py
admin.site.register(models.User)