# Generated by Django 4.0.2 on 2022-02-14 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pokedex", "0002_alter_pokedexcreature_secoundary_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pokedexcreature",
            old_name="primary_type",
            new_name="_primary_type",
        ),
        migrations.RenameField(
            model_name="pokedexcreature",
            old_name="secoundary_type",
            new_name="_secoundary_type",
        ),
    ]
