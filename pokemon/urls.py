from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PokemonViewSet, CreateUserView

router = DefaultRouter()
router.register("pokemon", PokemonViewSet)

urlpatterns = [path("sign-up/", CreateUserView.as_view())]

urlpatterns += router.urls
