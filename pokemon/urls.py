from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PokemonViewSet 

router = DefaultRouter()
router.register('pokemon', PokemonViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]
