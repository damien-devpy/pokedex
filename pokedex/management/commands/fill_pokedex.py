import csv

import requests
from django.core.management.base import BaseCommand, CommandError

from pokedex.models import PokedexCreature, PokemonType


class Command(BaseCommand):
    help = "Fill the Pokedex with new creatures from csv file"

    def add_arguments(self, parser):
        parser.add_argument("content", nargs="?", type=str)

    def handle(self, *args, **kwargs):
        content = requests.get(kwargs.get("content")).text.splitlines()

        reader = self._get_csv_reader(content)

        pokemon_type = set()

        for row in reader:
            # Cleaning data, we don't want empty string
            if row["_primary_type"]:
                pokemon_type.add(row["_primary_type"])
            if row["_secoundary_type"]:
                pokemon_type.add(row["_secoundary_type"])

        # First, fill the type
        PokemonType.objects.bulk_create(
            [PokemonType(pokemon_type=_type) for _type in pokemon_type],
            ignore_conflicts=True,
        )

        # Map the pokemon type string to its object in DB
        mapping = {obj.pokemon_type: obj for obj in PokemonType.objects.all()}

        reader = self._get_csv_reader(content)
        reader_with_type_id = self._replace_type_with_id(reader, mapping)

        # Now, fill the creatures
        PokedexCreature.objects.bulk_create(
            [PokedexCreature(**row) for row in reader_with_type_id],
            ignore_conflicts=True,
        )

    def _get_csv_reader(self, content):
        """Return an iterable from a csv file."""
        # Use DictReader so we will just have to unpack each row
        # And ensure column name match fields names
        reader = csv.DictReader(content, fieldnames=PokedexCreature.get_fields())
        # Skip the head line
        next(reader)
        return reader

    def _replace_type_with_id(self, reader, mapping):
        """Generator function that dynamically replace
        string pokemong type with their object equivalent."""
        # Skipping line were data might be missing
        for row in reader:
            if not all([row[key] for key in PokedexCreature.get_mandatory_fields()]):
                continue
            primary_type = row.get("_primary_type")
            secoundary_type = row.get("_secoundary_type")
            row["_primary_type"] = mapping.get(primary_type)
            if secoundary_type:
                row["_secoundary_type"] = mapping.get(secoundary_type)
            else:
                row["_secoundary_type"] = None
            yield row
