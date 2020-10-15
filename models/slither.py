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

vicky_viper = Viper("Vicky", "Viper", "Rat")
print(vicky_viper.name)
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

connie_copperhead = Copperhead("Connie", "Copperhead", "Rat")
print(connie_copperhead.name)
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

willy_worm = Worm("Willy", "Worm", "Dirt")
print(willy_worm.name)
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

leslie_leech = Leech("Leslie", "Leech", "Blood")
print(leslie_leech.name)
print(vicky_viper.feed())

class Rattlesnake():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.slithering = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

rodney_rattlesnake = Rattlesnake("Rodney", "Rattlesnake", "Rat")
print(rodney_rattlesnake.name)