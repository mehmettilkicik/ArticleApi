from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404

from articles.models.article_model import Article
from articles.serializers.article_serializer import ArticleSerializer

class ArticleListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ArticleDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self,id):
        return get_object_or_404(Article,id=id)
    
    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        if article.author != request.user:
            return Response({'detail': 'Bu makaleyi güncelleme yetkiniz yok'},status=status.HTTP_403_FORBIDDEN)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        article = self.get_object(id)
        if article.author != request.user:
            return Response({'detail':'Bu makaleyi silmeye yetkiniz yok'},status=status.HTTP_403_FORBIDDEN)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)