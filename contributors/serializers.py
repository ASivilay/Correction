# contributors.serializers.py

from rest_framework import serializers
from .models import Contributor

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        #fields = '__all__'
        fields = ['user_id',
                  'project_id',
                  'permission',
                  'role']