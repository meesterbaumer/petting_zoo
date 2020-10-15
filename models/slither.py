from datetime import date

class Viper():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

vicky_viper = Viper("Vicky", "Viper")
print(vicky_viper.name)

class Copperhead():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

connie_copperhead = Copperhead("Connie", "Copperhead")
print(connie_copperhead.name)

class Worm():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

willy_worm = Worm("Willy", "Worm")
print(willy_worm.name)

class Leech():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

leslie_leech = Leech("Leslie", "Leech")
print(leslie_leech.name)

class Rattlesnake():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

rodney_rattlesnake = Rattlesnake("Rodney", "Rattlesnake")
print(rodney_rattlesnake.name)