# users.serializers.py

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['first_name', 
                  'last_name',
                  'email',
                  'password'] 

    '''def create(self, validated_data):
        return User.objects.create(validated_data)
    '''