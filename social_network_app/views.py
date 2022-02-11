from .models import Post, User
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, FormView
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'social_network/layouts/main-layout.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class NewPostView(FormView, LoginRequiredMixin):
    template_name = 'social_network/new-post.html'
    form_class = PostForm
    success_url = '/post-feed'

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class PostFeedView(ListView):
    template_name = 'social_network/post-feed.html'
    model = Post
    context_object_name = 'all_posts'
    queryset = Post.objects.all()


def like_post(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.num_likes.add(request.user)
    return HttpResponseRedirect(reverse('post-feed'))