from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Trainer(models.Model):
    name = models.CharField(max_length=16)


class Pokemon(models.Model):
    pokedex_creature = models.ForeignKey(
        "pokedex.PokedexCreature", on_delete=models.PROTECT
    )
    trainer = models.ForeignKey(Trainer, null=True, on_delete=models.SET_NULL)
    surname = models.CharField(max_length=128)
    level = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)

    class Meta:
        ordering = ["pokedex_creature"]

    def __str__(self):
        return f"{self.surname} - Level {self.level} - {self.experience}/100 XP"

    def save(self, *args, **kwargs):
        """Overriding to make some custom changes.
        - Set default surname to PokedexCreature.name if not provided
        - Level up every 100 XP
        - Storing any left experience if needed

        >>> from pokedex.models import PokedexCreature
        >>> from pokemon.models import Pokemon
        >>> clefable = Pokemon(pokedex_creature=PokedexCreature.objects.get(pk=42))
        >>> clefable.save()
        # Default surname set auto
        >>> clefable.surname
        'Clefable'
        >>> clefable.experience
        0
        >>> clefable.level
        0
        >>> clefable.experience = 150
        >>> clefable.save()
        >>> clefable.experience
        50
        >>> clefable.level
        1
        """
        if not self.surname:
            self.surname = self.pokedex_creature.name
        self.level += self.experience // 100
        self.experience %= 100
        super().save(*args, **kwargs)
