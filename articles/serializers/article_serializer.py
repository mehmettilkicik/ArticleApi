from rest_framework import serializers
from articles.models import Article
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

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
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
            'author',
            'like_count',
            'comment_count',
        ]

        def get_like_count(self, obj):
            return obj.likes.count()
        
        def get_comment_count(self,obj):
            return obj.comments.count()