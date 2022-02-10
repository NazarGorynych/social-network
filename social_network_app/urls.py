from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('new-post/', NewPostView.as_view(), name='new-post'),
    ]