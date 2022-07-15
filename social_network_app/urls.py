from django.urls import path, include
from . import views
from .views import *




urlpatterns = [
    # path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),

    # Api
    path('api/', include('api.urls')),

    # social_network_app
    path('signup/', SignUpView.as_view(), name='signup'),
    path('new-post/', NewPostView.as_view(), name='new-post'),
    path('post-feed/', PostFeedView.as_view(), name='post-feed'),
    path('like/<int:pk>', views.like_post, name='like_post'),
    path('dislike/<int:pk>', views.dislike_post, name='dislike_post'),
    ]