from rest_framework import status, viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Pokemon
from .serializers import (
    LevelUpSerializer,
    RetrieveOrListPokemonSerializer,
    PokemonSerializer,
    UpdatePokemonSerializer,
)


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()

    def get_serializer_class(self):
        if self.action in ("retrieve", "list"):
            return RetrieveOrListPokemonSerializer
        if self.action in ("update"):
            return UpdatePokemonSerializer
        if self.action == "give_xp":
            return LevelUpSerializer
        return PokemonSerializer

    @action(methods=["post"], detail=True)
    def give_xp(self, request, pk=None):
        pokemon = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            pokemon.experience += serializer.validated_data["experience"]
            pokemon.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
