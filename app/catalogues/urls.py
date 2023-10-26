from rest_framework.routers import SimpleRouter

from .views import ExampleViewSet

ADMIN_CATALOGUES_ROUTER = SimpleRouter()

ADMIN_CATALOGUES_ROUTER.register("examples", ExampleViewSet, basename="examples")
