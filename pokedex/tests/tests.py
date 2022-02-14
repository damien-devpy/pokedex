import pytest
from os import environ
from django.core import management
from django.test import TestCase
from pokedex.models import PokedexCreature


class MockResponse:
    def __init__(self, *args, **kwargs):
        self.text = ("#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary\n"
                +"1,Bulbasaur,Grass,Poison,318,45,49,49,65,65,45,1,False\n"
                +"2,Ivysaur,Grass,Poison,405,60,62,63,80,80,60,1,False\n"
                +"3,Venusaur,Grass,Poison,525,80,82,83,100,100,80,1,False\n"
                +"4,VenusaurMega Venusaur,Grass,Poison,625,80,100,123,122,120,80,1,False\n"
                +"4,Charmander,Fire,,309,39,52,43,60,50,65,1,False\n"
                +"5,,Fire,,405,58,64,58,80,65,80,1,False\n")

class MockRequest:
    def get(self, *args, **kwargs):
        return MockResponse()

@pytest.fixture
def mock_request(monkeypatch):
    monkeypatch.setattr("pokedex.management.commands.fill_pokedex.requests", MockRequest)


@pytest.mark.django_db
def test_fill_pokedex_successfully_fill_db(mock_request):
    url = 'https://random.url'
    management.call_command('fill_pokedex', url)

    creature = PokedexCreature.objects.all()

    assert creature.count() == 5
    assert creature.first().name == 'Bulbasaur'
    assert creature.first().primary_type == 'Grass'

@pytest.mark.django_db
def test_fill_pokedex_skip_wrong_data(mock_request):
    url = 'https//dummy.url'
    management.call_command('fill_pokedex', url)
    
    creature = PokedexCreature.objects.all()

    assert creature.last().name == "Charmander"