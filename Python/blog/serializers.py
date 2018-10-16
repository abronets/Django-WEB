from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Post


class PostSerializer(ModelSerializer):
    user_fullname = serializers.CharField(source='user.get_full_name', read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'text', 'user_id', 'title', 'created_datetime',
                  'edited_datetime', 'is_published', 'user_fullname', 'user',)