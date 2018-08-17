from argparse import ArgumentParser
from PokemonParser import *
import sys

def read_input():
    return raw_input()


def print_ask():
    print "Type here: "

def print_intro():
    print "WHO'S THAT POKEMON!?"

def sanitize_input(input):
    lower = input.lower()

    if (input == 'e' or input == 'm' or input == 'h'):
        return input
    else:
        print "Usage: python src/main.py -d [e/m/h]"
        exit()


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument("-d", "--difficulty",
    help="Enter the difficulty level you want, choose between e (easy), m (medium) or h (hard)")
    args = parser.parse_args()

    difficulty = 'e'
    if args.difficulty != None:
        difficulty = sanitize_input(args.difficulty)

    print_intro()
    pokemon = generate_rand_pokemon(difficulty)
    pokemon.print_pokemon()
    print_ask()
    input = read_input()

    if pokemon.equals(input.lower()):
        print "You win!"
    else:
        print "You lose, the pokemon was " + pokemon.name

#http://www.world-of-nintendo.com/pictures/text/
