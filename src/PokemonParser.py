import os, random
from Pokemon import Pokemon
path = "/mnt/c/Users/le-zo/Documents/Programs/who's_that_pokemon/pokemon/"

def create_pokemon(file):
    new_pokemon = Pokemon()
    with open(path + file, 'r') as f:
        new_pokemon.name, new_pokemon.difficulty = f.readline().split(",")
        new_pokemon.image = f.read()
        return new_pokemon

def generate_rand_pokemon():
    rand_pokemon = random.choice(os.listdir(path))
    rand_pokemon = create_pokemon(rand_pokemon)
    return rand_pokemon
