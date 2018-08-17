class Pokemon:
    name = ""
    difficulty = ""
    image = ""

    def print_pokemon(self):
        print self.image

    def equals(self, name):
        return self.name == name
