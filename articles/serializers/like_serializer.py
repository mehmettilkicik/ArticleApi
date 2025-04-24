from rest_framework import serializers
from models.like_model import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
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