from rest_framework import serializers

from .models import PokedexCreature

class PokedexCreatureSerializer(serializers.ModelSerializer):
    surname = serializers.CharField(required=False)
    class Meta:
        model = PokedexCreature
        fields = '__all__'
        depth = 1
