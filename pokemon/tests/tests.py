from os import environ

import pytest
from django.core import management
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from pokedex.models import PokedexCreature
from pokemon.models import Pokemon, User


class TestPokemonViewSet(TestCase):
    fixtures = ["pokedex.json"]

    def setUp(self):
        self.client = APIClient()
        user = self.create_user()
        self.client.force_authenticate(user=user)
        self.expected_data = {"pokedex_creature": 1}

    def create_user(self):
        user = User(username="login", password="password")
        user.save()
        return user

    def test_user_can_create_a_pokemon(self):
        response = self.client.post("/pokemon/", self.expected_data, format="json")
        _id = response.json()["id"]

        assert Pokemon.objects.get(pk=_id)
        assert (
            Pokemon.objects.get(pk=_id).pokedex_creature.id
            == self.expected_data["pokedex_creature"]
        )

    def test_user_can_create_a_pokemone_with_surname(self):
        self.expected_data["surname"] = "Surname"

        response = self.client.post("/pokemon/", self.expected_data, format="json")
        _id = response.json()["id"]
        pokemon = Pokemon.objects.get(pk=_id)

        assert pokemon
        assert pokemon.surname == self.expected_data["surname"]
        assert pokemon.pokedex_creature.id == self.expected_data["pokedex_creature"]

    def test_user_can_give_experience_to_existing_pokemon(self):
        response = self.client.post("/pokemon/", self.expected_data, format="json")
        pokemon_id = response.json()["id"]

        data = {
            "experience": 315,
        }
        self.client.post(f"/pokemon/{pokemon_id}/give_xp/", data, format="json")
        pokemon = Pokemon.objects.get(pk=pokemon_id)

        assert pokemon.experience == 15
        assert pokemon.level == 3

        data["experience"] = 125
        self.client.post(f"/pokemon/{pokemon_id}/give_xp/", data, format="json")
        pokemon.refresh_from_db()

        assert pokemon.experience == 40
        assert pokemon.level == 4

    def test_user_doing_wrong_request_get_expected_error(self):
        wrong_payload = {"wrong_payload": 42}

        response = self.client.post("/pokemon/", self.expected_data, format="json")
        pokemon_id = response.json()["id"]
        response = self.client.post(
            f"/pokemon/{pokemon_id}/give_xp/", wrong_payload, format="json"
        )

        assert response.status_code == 400
        assert "is required" in str(response.content)

    def test_user_can_update_surname_of_existing_pokemon(self):
        response = self.client.post("/pokemon/", self.expected_data, format="json")
        pokemon_id = response.json()["id"]
        old_surname = response.json()["surname"]

        data = {"surname": "pet"}
        response = self.client.put(f"/pokemon/{pokemon_id}/", data, format="json")

        assert response.json()["surname"] != old_surname
        assert response.json()["surname"] == data["surname"]

    def test_anonymous_user_is_read_only(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("/pokemon/")

        assert response.status_code == 200

        response = self.client.post("/pokemon/", self.expected_data, format="json")

        assert response.status_code == 403
