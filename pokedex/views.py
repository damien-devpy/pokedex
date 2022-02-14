from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import PokedexCreature
from .serializers import PokedexCreatureSerializer, PokedexCreatureDetailSerializer

class PokedexViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PokedexCreature.objects.all()
    serializer_class = PokedexCreatureSerializer

    def retrieve(self, request, pk=None):
        creature = self.get_object()
        serializer = PokedexCreatureDetailSerializer(instance=creature)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

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
