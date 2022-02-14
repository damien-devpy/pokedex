from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PokedexViewSet

router = DefaultRouter()
router.register('pokedex', PokedexViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]
