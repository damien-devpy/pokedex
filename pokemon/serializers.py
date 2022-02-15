from rest_framework import serializers

from pokedex.serializers import PokedexCreatureSerializer

from .models import Pokemon, Trainer, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User()
        user.username = validated_data["username"]
        user.set_password(validated_data["password"])
        user.save()
        return user


class RetrieveOrListPokemonSerializer(serializers.ModelSerializer):
    pokedex_creature = PokedexCreatureSerializer()

    class Meta:
        model = Pokemon
        fields = "__all__"


class BasePokemonSerializer(serializers.ModelSerializer):
    surname = serializers.CharField(required=False)

    class Meta:
        model = Pokemon
        fields = "__all__"


class PokemonSerializer(BasePokemonSerializer):
    pass


class UpdatePokemonSerializer(BasePokemonSerializer):
    class Meta(BasePokemonSerializer.Meta):
        extra_kwargs = {"pokedex_creature": {"read_only": True}}

    def update(self, instance, validated_data):
        surname = validated_data.get("surname")
        if surname:
            instance.surname = surname
            instance.save()
        return instance


class LevelUpSerializer(serializers.Serializer):
    experience = serializers.IntegerField()
