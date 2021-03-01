from django.db import models
from django.conf import settings


class Review(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.author.username
