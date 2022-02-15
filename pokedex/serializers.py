from rest_framework import serializers

from .models import PokedexCreature, PokemonType


class PokemonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonType
        fields = "__all__"


class PokedexCreatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokedexCreature
        fields = [
            "id",
            "pokemon_id",
            "name",
            "total",
            "health_point",
            "legendary",
            "generation",
            "primary_type",
            "secoundary_type",
        ]


class PokedexCreatureDetailSerializer(serializers.ModelSerializer):
    primary_type = PokemonTypeSerializer(source="_primary_type")
    secoundary_type = PokemonTypeSerializer(source="_secoundary_type")

    class Meta:
        model = PokedexCreature
        exclude = ["_primary_type", "_secoundary_type"]
        depth = 1
