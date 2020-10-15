from datetime import date

class Camel():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

kyle_camel = Camel("Kyle", "Camel", "Afternoon")
print(f'{kyle_camel.name} the {kyle_camel.species} is available to pet during the {kyle_camel.shift} shift.')

class Zoney():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

zelda_zoney = Zoney("Zelda", "Zoney", "Evening")
print(f'{zelda_zoney.name} the {zelda_zoney.species} is available to pet during the {zelda_zoney.shift} shift.')

class Skunk():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

steve_skunk = Skunk("Steve", "Skunk", "Afternoon")
print(f'{steve_skunk.name} the {steve_skunk.species} is available to pet during the {steve_skunk.shift} shift.')

class Armadillo():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

andy_armadillo = Armadillo("Andy", "Armadillo", "Morning")
print(f'{andy_armadillo.name} the {andy_armadillo.species} is available to pet during the {andy_armadillo.shift} shift.')

class Buffalo():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

bob_buffalo = Buffalo("Bob", "Buffalo", "Morning")
print(f'{bob_buffalo.name} the {bob_buffalo.species} is available to pet during the {bob_buffalo.shift} shift.')