from rest_framework import serializers

from .models import PokedexCreature


class PokedexCreatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokedexCreature
        fields = [
            "name",
            "total",
            "health_point",
            "legendary",
            "generation",
            "_secoundary_type",
            "_primary_type",
        ]
        depth = 1


class PokedexCreatureDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokedexCreature
        fields = "__all__"
        depth = 1
