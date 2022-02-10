from .models import Post, User
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, FormView
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
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
    success_url = '/index'
    #
    # def get_queryset(self):
    #     return User.objects.filter(id=self.request.user.id)

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.author = self.request.user
        breakpoint()
        form.save()
        return super().form_valid(form)