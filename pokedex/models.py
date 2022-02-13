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
    name = models.CharField(max_length=32)
    primary_type = models.ForeignKey(PokemonType, on_delete=models.PROTECT, related_name='primary_type')
    secoundary_type = models.ForeignKey(PokemonType, on_delete=models.PROTECT, blank=True, related_name='secoundary_type')
    total = models.IntegerField()
    health_point = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_atk = models.IntegerField()
    sp_def = models.IntegerField()
    speed = models.IntegerField()
    generation = models.IntegerField()
    legendary = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['name'],
                name='unique_pokemon'
            )
        ]
