from rest_framework import serializers

from .models import PokedexCreature

class PokedexCreatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokedexCreature
        fields = '__all__'
