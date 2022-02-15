from .models import Post, User
from .forms import PostForm, UserRegisterForm
from django.views.generic import CreateView, ListView, FormView
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from social_network_app.current_user import get_current_user
from django.contrib.messages.views import SuccessMessageMixin


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

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     dislike_check = []
    #     current_user = self.request.user
    #     for post in self.object_list:
    #         bool_query = Post.objects.filter(num_likes=current_user).exists()
    #         dislike_check.append(bool_query)
    #     context['dislike_check'] = dislike_check
    #     return super().get_context_data()


def dislike_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.num_likes.remove(request.user)
    return HttpResponseRedirect(reverse('post-feed'))


def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.num_likes.add(request.user)
    return HttpResponseRedirect(reverse('post-feed'))
