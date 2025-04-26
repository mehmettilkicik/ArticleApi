from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404

from articles.models.article_model import Article
from articles.models.comment_model import Comment
from articles.serializers.comment_serializer import CommentSerializer


class CommentCreateListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self,request,id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            article = get_object_or_404(Article,id=id)
            serializer.save(author=request.user, article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id):
        comments = Comment.objects.filter(article_id=id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)