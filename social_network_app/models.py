from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    published_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
    text = models.TextField()

    def __str__(self):
        return f'{self.title}'
