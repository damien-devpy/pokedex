# Generated by Django 4.0.2 on 2022-02-13 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon_type', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='PokedexCreature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('total', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('sp_atk', models.IntegerField()),
                ('sp_def', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('generation', models.IntegerField()),
                ('legendary', models.BooleanField(default=False)),
                ('primary_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='primary_type', to='pokedex.pokemontype')),
                ('secoundary_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='secoundary_type', to='pokedex.pokemontype')),
            ],
        ),
    ]
