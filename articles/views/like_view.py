from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from django.shortcuts import get_object_or_404

from articles.models.article_model import Article
from articles.models.like_model import Like
from articles.serializers.like_serializer import LikeSerializer


class LikeCreateDestroyView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post(self,request,id):
            article = get_object_or_404(Article,id=id)

            like_exists = Like.objects.filter(user=request.user, article=article).exists()

            if like_exists:
                return Response({"detail":"Already liked."},status=status.HTTP_400_BAD_REQUEST)
            
            Like.objects.create(user=request.user,article=article)

            return Response({"detail":"Liked"}, status=status.HTTP_201_CREATED)
    
    def delete(self,request,id):
         article = get_object_or_404(Article,id=id)

         like = Like.objects.filter(user = request.user, article = article).first()

         if like:
              like.delete()
              return Response({"detail":"Unliked"}, status=status.HTTP_204_NO_CONTENT)
         
         return Response({"detail":"Like doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
        
