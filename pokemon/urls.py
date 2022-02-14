from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PokemonViewSet

router = DefaultRouter()
router.register("pokemon", PokemonViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
