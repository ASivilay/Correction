# comments.serializers.py

from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        #fields = '__all__'
        fields = ['description',
                  'author_user_id',
                  'issue_id',
                  'created_time']