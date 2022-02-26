from .models import Post, User
from .forms import PostForm, UserRegisterForm
from django.views.generic import CreateView, ListView, FormView
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from social_network_app.current_user import get_current_user
from django.contrib.messages.views import SuccessMessageMixin
from .serializers import *
from rest_framework import viewsets, permissions, renderers
from rest_framework.response import Response
from rest_framework.decorators import action


def index(request):
    return render(request, 'social_network/layouts/main-layout.html')


class SignUpView(CreateView, SuccessMessageMixin):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    success_message = 'Success!'


class NewPostView(FormView, LoginRequiredMixin):
    template_name = 'social_network/new-post.html'
    form_class = PostForm
    success_url = '/post-feed'

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.author = get_current_user()
        form.save()
        return super().form_valid(form)


class PostFeedView(ListView):
    template_name = 'social_network/post-feed.html'
    model = Post
    context_object_name = 'all_posts'
    queryset = Post.objects.all()


def dislike_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.num_likes.remove(request.user)
    return HttpResponseRedirect(reverse('post-feed'))


def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.num_likes.add(request.user)
    return HttpResponseRedirect(reverse('post-feed'))


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
