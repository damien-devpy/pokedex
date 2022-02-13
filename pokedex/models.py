from django.db import models


class PokemonType(models.Model):
    pokemon_type = models.CharField(max_length=16) 


class PokedexCreature(models.Model):
    pokemon_id = models.IntegerField()
    name = models.CharField(max_length=32, primary_key=True)
    primary_type = models.ForeignKey(PokemonType, on_delete=models.PROTECT, related_name='primary_type')
    secoundary_type = models.ForeignKey(PokemonType, on_delete=models.PROTECT, blank=True, related_name='secoundary_type')
    total = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_atk = models.IntegerField()
    sp_def = models.IntegerField()
    speed = models.IntegerField()
    generation = models.IntegerField()
    legendary = models.BooleanField(default=False)
