from social_network_app.models import Post, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):
    total_likes = Post.total_likes
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
