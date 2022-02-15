from .models import User, Post
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username', 'password1', 'password2']


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author', 'num_likes']