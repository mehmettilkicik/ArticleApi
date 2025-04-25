from rest_framework import serializers
from articles.models import Article
from django.contrib.auth.models import User
from .comment_serializer import CommentSerializer

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article

        fields = [
            'id',
            'title',
            'content',
            'created_at',
            'updated_at',
            'author',
            'like_count',
            'comment_count',
            'comments',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
            'author',
            'like_count',
            'comment_count',
            'comments',
        ]

        def get_like_count(self, obj):
            return obj.likes.count()
        
        def get_comment_count(self,obj):
            return obj.comments.count()