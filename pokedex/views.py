from rest_framework import viewsets

from .models import PokedexCreature
from .serializers import PokedexCreatureSerializer

class PokedexViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PokedexCreature.objects.all()
    serializer_class = PokedexCreatureSerializer

    def get_queryset(self):
        """Filter given optionnal query parameters."""
        queryset = PokedexCreature.objects.all()

        generation = self.request.query_params.get('generation')
        legendary = self.request.query_params.get('legendary')
        primary_type = self.request.query_params.get('primary_type')
        secoundary_type = self.request.query_params.get('secoundary_type')
        not_secoundary_type = self.request.query_params.get('not_secoundary_type')

        if generation:
            queryset = queryset.filter(generation=generation)
        if legendary:
            queryset = queryset.filter(legendary=legendary)
        if primary_type:
            queryset = queryset.filter(_primary_type__pokemon_type=primary_type)
        if secoundary_type:
            queryset = queryset.filter(_secoundary_type__pokemon_type=secoundary_type)
        elif not_secoundary_type:
            queryset = queryset.filter(_secoundary_type__isnull=True)
        return queryset
