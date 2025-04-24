from rest_framework import serializers
from articles.models import Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    article = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment

        fields = [
            "id",
            "content",
            "created_at",
            "author",
            "article",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "author",
            "article",
        ]
        
