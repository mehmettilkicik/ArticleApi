from django.urls import path
from articles.views import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    #User
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),

    #Article
    path('articles/', ArticleListCreateView.as_view(),name='articles'),
    path('articles/<int:id>', ArticleDetailView.as_view(),name='article_detail'),

    #Comments
    path('articles/<int:id>/comments', CreateListCommentView.as_view(),name='comments')
]