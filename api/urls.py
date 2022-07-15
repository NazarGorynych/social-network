from rest_framework_simplejwt.views import \
    TokenObtainPairView,\
    TokenRefreshView,\
    TokenVerifyView

from django.urls import include, path
from .routers import router


urlpatterns = [

    # Api
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ]