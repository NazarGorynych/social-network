from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views
from .views import *

# post_list = PostViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# post_detail = PostViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# post_highlight = PostViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)



urlpatterns = [
    # path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),

    # Api
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # social_network_app
    path('signup/', SignUpView.as_view(), name='signup'),
    path('new-post/', NewPostView.as_view(), name='new-post'),
    path('post-feed/', PostFeedView.as_view(), name='post-feed'),
    path('like/<int:pk>', views.like_post, name='like_post'),
    path('dislike/<int:pk>', views.dislike_post, name='dislike_post'),
    ]