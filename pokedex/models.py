from django.db import models
from django.db.models import UniqueConstraint


class PokemonType(models.Model):
    pokemon_type = models.CharField(max_length=16) 

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['pokemon_type'],
                name='unique_pokemon_type'
            )
        ]

class PokedexCreature(models.Model):
    pokemon_id = models.IntegerField()
    name = models.CharField(max_length=32, blank=False)
    _primary_type = models.ForeignKey(PokemonType, on_delete=models.PROTECT, related_name='primary_type')
    _secoundary_type = models.ForeignKey(PokemonType, on_delete=models.PROTECT, null=True, related_name='secoundary_type')
    total = models.IntegerField()
    health_point = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_atk = models.IntegerField()
    sp_def = models.IntegerField()
    speed = models.IntegerField()
    generation = models.IntegerField()
    legendary = models.BooleanField(default=False)


    @classmethod
    def get_fields(cls):
        return [
            field.name 
            for field in cls._meta.concrete_fields
            if field.name != 'id'
        ]

    @classmethod
    def get_mandatory_fields(cls):
        return [
            field.name
            for field in cls._meta.concrete_fields
            if field.name != 'id' and not field.null 
        ]

    @property
    def primary_type(self):
        return self._primary_type.pokemon_type

    @property
    def secoundary_type(self):
        return self._secoundary_type.pokemon_type

    class Meta:
        ordering = ['pokemon_id']
        constraints = [
            UniqueConstraint(
                fields=['name'],
                name='unique_pokemon'
            )
        ]
