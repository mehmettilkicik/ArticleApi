from django.db import models
from django.contrib.auth.models import User
from .article_model import Article

class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked {self.article.title}"

    class Meta:
        unique_together = ('article', 'user')
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        ordering = ['-created_at']