from rest_framework import viewsets

from .models import PokedexCreature
from .serializers import PokedexCreatureSerializer

class PokedexViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PokedexCreature.objects.all()
    serializer_class = PokedexCreatureSerializer
