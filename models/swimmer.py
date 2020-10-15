from datetime import date

class Beaver():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

beth_beaver = Beaver("Beth", "Beaver")
print(beth_beaver.name)

class Otter():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

otis_otter = Otter("Otis", "Otter")
print(otis_otter.name)

class Octopus():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

orvis_octopus = Octopus("Orvis", "Octopus")
print(orvis_octopus.name)

class Walrus():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

wally_walrus = Walrus("Wally", "Walrus")
print(wally_walrus.name)

class Piranha():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

peggy_piranha = Piranha("Peggy", "Piranha")
print(peggy_piranha.name)