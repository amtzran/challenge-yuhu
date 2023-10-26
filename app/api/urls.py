from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from tasks.api.urls import TASKS_ROUTER

from .serializers import UserToken

API_V1_ROUTER_ADMIN = DefaultRouter()

API_V1_ROUTER_ADMIN.registry.extend(TASKS_ROUTER.registry)

urlpatterns = [
    path("authentication/token/", TokenObtainPairView.as_view(serializer_class=UserToken), name="auth_get_token"),
    path("authentication/refresh/", TokenRefreshView.as_view(), name="auth_refresh_token"),
    path("", include(API_V1_ROUTER_ADMIN.urls)),
]
