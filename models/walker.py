from datetime import date

class Camel():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

kyle_camel = Camel("Kyle", "Camel")
print(kyle_camel.name)

class Zoney():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

zelda_zoney = Zoney("Zelda", "Zoney")
print(zelda_zoney.name)

class Skunk():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

steve_skunk = Skunk("Steve", "Skunk")
print(steve_skunk.name)

class Armadillo():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

andy_armadillo = Armadillo("Andy", "Armadillo")
print(andy_armadillo.name)

class Buffalo():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

bob_buffalo = Buffalo("Bob", "Buffalo")
print(bob_buffalo.name)