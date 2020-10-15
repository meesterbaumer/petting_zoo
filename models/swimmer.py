from datetime import date

class Beaver():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.swimming = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

    def __str__(self):
      return f"{self.name} is a {self.species}"

beth_beaver = Beaver("Beth", "Beaver", "Logs")
print(beth_beaver)
print(beth_beaver.feed())

class Otter():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.swimming = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

    def __str__(self):
      return f"{self.name} is a {self.species}"

otis_otter = Otter("Otis", "Otter", "Fish")
print(otis_otter)
print(otis_otter.feed())

class Octopus():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.swimming = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

    def __str__(self):
      return f"{self.name} is a {self.species}"

orvis_octopus = Octopus("Orvis", "Octopus", "Squid")
print(orvis_octopus)
print(orvis_octopus.feed())

class Walrus():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.swimming = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

    def __str__(self):
      return f"{self.name} is a {self.species}"

wally_walrus = Walrus("Wally", "Walrus", "Fish")
print(wally_walrus)
print(wally_walrus.feed())

class Piranha():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.swimming = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

    def __str__(self):
      return f"{self.name} is a {self.species}"

peggy_piranha = Piranha("Peggy", "Piranha", "Fingers")
print(peggy_piranha)
print(peggy_piranha.feed())