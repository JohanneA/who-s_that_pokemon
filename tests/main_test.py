import unittest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.PokemonParser import *

class TestPokemon(unittest.TestCase):

    def setUp(self):
        pass

    def test_equals(self):
        charmander = create_pokemon('charmander.txt')
        self.assertEquals(charmander.name, 'charmander')

if __name__ == '__main__':
    unittest.main()
