Catch Them All !

### Django/DRF technical test

[ER diagram](https://drive.google.com/file/d/1pwEx8WcwaotmdP_JcI5bnyQhjb0eyfvj/view?usp=sharing)

## How to play with it

You can use it locally, first fork/clone the repo

```
>>> git clone git@github.com:damien-devpy/pokedex.git && cd pokedex
```

Setup a virtualenv and install dependencies

```
>>> python -m venv .venv && source .venv/bin/activate
>>> pip install -r requirements.txt
```

Then, you're good to go, run a local server

```
>>> python manage.py runserver
```

## How it works

They are to applications into this project, a Pokedex app and a Pokemon app.
Each of this has his own API.

The Pokedex API is a read only API.

## Pokedex API

### pokedex/

```
>>> curl 127.0.0.1:8000/pokedex/ | jq
{
  "count": 800,
  "next": "http://127.0.0.1:8000/pokedex/?page=2",
  "previous": null,
  "results": [
    {
      "name": "Bulbasaur",
      "total": 318,
      "health_point": 45,
      "legendary": false,
      "generation": 1,
      "_secoundary_type": {
        "id": 5,
        "pokemon_type": "Poison"
      },
      "_primary_type": {
        "id": 2,
        "pokemon_type": "Grass"
      }
    },
    {
      "name": "Ivysaur",
      "total": 405,
      "health_point": 60,
      "legendary": false,
      "generation": 1,
      "_secoundary_type": {
        "id": 5,
        "pokemon_type": "Poison"
      },
      "_primary_type": {
        "id": 2,
        "pokemon_type": "Grass"
      }
    },
...
```

You can query filter as you wish. Let's say, we want only the legendary Pokemon
from the second generation that are flying

```
>>> curl 127.0.0.1:8000/pokedex/?generation=2&legendary=True&secoundary_type=Flying | jq
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "name": "Lugia",
      "total": 680,
      "health_point": 106,
      "legendary": true,
      "generation": 2,
      "_secoundary_type": {
        "id": 7,
        "pokemon_type": "Flying"
      },
      "_primary_type": {
        "id": 17,
        "pokemon_type": "Psychic"
      }
    },
    {
      "name": "Ho-oh",
      "total": 680,
      "health_point": 106,
      "legendary": true,
      "generation": 2,
      "_secoundary_type": {
        "id": 7,
        "pokemon_type": "Flying"
      },
      "_primary_type": {
        "id": 4,
        "pokemon_type": "Fire"
      }
    }
  ]
}
```

`pokedex/` route doesn't give all the details about a creature, you can use a second route
for that

### pokedex/{id}

```
>>> curl 127.0.0.1:8000/pokedex/1/ | jq
{
  "id": 1,
  "pokemon_id": 1,
  "name": "Bulbasaur",
  "total": 318,
  "health_point": 45,
  "attack": 49,
  "defense": 49,
  "sp_atk": 65,
  "sp_def": 65,
  "speed": 45,
  "generation": 1,
  "legendary": false,
  "_primary_type": {
    "id": 2,
    "pokemon_type": "Grass"
  },
  "_secoundary_type": {
    "id": 5,
    "pokemon_type": "Poison"
```

The Pokemon API on the other hand is a standard CRUD API.

🔐 : Routes with the locker expect an authenticate user. Do so through the browsable API
or by including X-CSRFTOKEN in your request

## Pokemon API

### GET pokemon/

```
>>> curl 127.0.0.1:8000/pokemon/ | jq
{
  "count": 0,
  "next": null,
  "previous": null,
  "results": []
}
```

### POST pokemon/ 🔐

```
>>> curl 127.0.0.1:8000/pokemon/ -H 'Content-Type:application/json' -d '{"pokedex_creature": 42}' | jq
{
  "id": 1,
  "surname": "Clefable",
  "level": 0,
  "experience": 0,
  "pokedex_creature": 42,
  "trainer": null
}
```

### GET pokemon/{id}/

```
>>> curl 127.0.0.1:8000/pokemon/1/ | jq
{
  "id": 1,
  "pokedex_creature": {
    "name": "Squirtle",
    "total": 314,
    "health_point": 44,
    "legendary": false,
    "generation": 1,
    "_secoundary_type": null,
    "_primary_type": {
      "id": 6,
      "pokemon_type": "Water"
    }
  },
  "surname": "Squirtle",
  "level": 0,
  "experience": 0,
  "trainer": null
}
```

### PUT pokemon/{id}/ 🔐

```
>>> curl -X PUT -H "Content-Type: application/json" -d '{"surname": "pet"}' 127.0.0.1:8000/pokemon/1/ | jq
{
  "id": 1,
  "surname": "pet",
  "level": 0,
  "experience": 0,
  "pokedex_creature": 42,
  "trainer": null
}
```

### Tests

You can also run the tests if needed

```
>>> pytest
```
