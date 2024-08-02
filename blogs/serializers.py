from .models import Comment, Post
from rest_framework import serializers
from users.serializers import ReadUserSerializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'created_at', 'updated_at']


class ReadPostSerializer(serializers.ModelSerializer):
    author = ReadUserSerializer()
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'image', 'author', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'author', 'created_at', 'updated_at']

class ReadCommentSerializer(serializers.ModelSerializer):
    author = ReadUserSerializer()
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'author', 'created_at', 'updated_at']