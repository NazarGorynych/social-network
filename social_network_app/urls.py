from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='social_network_app'),
    path('', include('django.contrib.auth.urls')),
    ]