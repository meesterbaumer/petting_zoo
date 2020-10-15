from datetime import date

class Viper():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.slithering = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

    def __str__(self):
      return f"{self.name} is a {self.species}"

vicky_viper = Viper("Vicky", "Viper", "Rat")
print(vicky_viper)
print(vicky_viper.feed())

class Copperhead():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.slithering = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

    def __str__(self):
      return f"{self.name} is a {self.species}"

connie_copperhead = Copperhead("Connie", "Copperhead", "Rat")
print(connie_copperhead)
print(connie_copperhead.feed())

class Worm():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.slithering = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

    def __str__(self):
      return f"{self.name} is a {self.species}"

willy_worm = Worm("Willy", "Worm", "Dirt")
print(willy_worm)
print(willy_worm.feed())

class Leech():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.slithering = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

    def __str__(self):
      return f"{self.name} is a {self.species}"

leslie_leech = Leech("Leslie", "Leech", "Blood")
print(leslie_leech)
print(leslie_leech.feed())

class Rattlesnake():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.slithering = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

    def __str__(self):
      return f"{self.name} is a {self.species}"

rodney_rattlesnake = Rattlesnake("Rodney", "Rattlesnake", "Rat")
print(rodney_rattlesnake)
print(rodney_rattlesnake.feed())