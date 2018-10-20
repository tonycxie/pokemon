from __future__ import unicode_literals
from django.db import models
from apps.log_reg.models import Trainers
from random import randint

class PokemonManager(models.Manager):
    def random(self, pokemon_list):
        count = pokemon_list.count()
        rand_index = randint(0, count - 1)
        return pokemon_list[rand_index]

class Pokemon(models.Model):
    name = models.CharField(max_length = 255)
    health = models.IntegerField()
    speed = models.IntegerField()
    tier = models.IntegerField()
    front_sprite = models.CharField(max_length = 255)
    back_sprite = models.CharField(max_length = 255)
    pokemons_trainer = models.ManyToManyField(Trainers, related_name = "trainers_pokemon")
    objects = PokemonManager()

class Types(models.Model):
    name = models.CharField(max_length = 255)
    types_pokemon = models.ManyToManyField(Pokemon, related_name = "pokemons_type")