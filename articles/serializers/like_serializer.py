from rest_framework import serializers
from articles.models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like

        fields=[
            "id",
            "article",
            "user",
            "created_at",
        ]
        read_only_fields=[
            "id",
            "user",
            "created_at",
        ]