from django.db import models
from django.contrib.auth.models import User
from social_network_app.current_user import get_current_user


class Post(models.Model):
    published_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=80)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    text = models.TextField()
    num_likes = models.ManyToManyField(User, related_name='num_likes', blank=True)

    def dislike_check(self):
        ifexists = Post.objects.filter(num_likes=get_current_user()).exists()
        return ifexists


    def total_likes(self):
        return self.num_likes.count()

    def __str__(self):
        return f'{self.title}'
