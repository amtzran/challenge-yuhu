"""
    URL CONFIGURATION
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

API_V1_ROUTER_ADMIN = DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", include_docs_urls(title="Project API")),
    path("api/v1/", include("api.urls")),
]
