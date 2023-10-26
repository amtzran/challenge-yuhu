from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from catalogues.urls import ADMIN_CATALOGUES_ROUTER

from .serializers import UserToken

API_V1_ROUTER_ADMIN = DefaultRouter()

API_V1_ROUTER_ADMIN.registry.extend(ADMIN_CATALOGUES_ROUTER.registry)
# API_V1_ROUTER_ADMIN.registry.extend(ADMIN_USERS_ROUTER.registry)

urlpatterns = [
    path(
        "auth/",
        TokenObtainPairView.as_view(serializer_class=UserToken),
        name="auth_get_token",
    ),
    path("auth/refresh/", TokenRefreshView.as_view(), name="auth_refresh_token"),
    path("admin/", include(API_V1_ROUTER_ADMIN.urls)),
]
