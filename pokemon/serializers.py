from rest_framework import serializers

from pokedex.serializers import PokedexCreatureSerializer

from .models import Pokemon, Trainer


class RetrieveOrListPokemonSerializer(serializers.ModelSerializer):
    pokedex_creature = PokedexCreatureSerializer()

    class Meta:
        model = Pokemon
        fields = "__all__"


class CreateOrUpdatePokemonSerializer(serializers.ModelSerializer):
    surname = serializers.CharField(required=False)

    class Meta:
        model = Pokemon
        fields = "__all__"


class LevelUpSerializer(serializers.Serializer):
    experience = serializers.IntegerField()
