from datetime import date

class Camel():
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date.today()
        self.walking = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

    def __str__(self):
      return f"{self.name} the {self.species}"

kyle_camel = Camel("Kyle", "Camel", "Afternoon", "Straw")
print(f'{kyle_camel} is available to pet during the {kyle_camel.shift} shift.')
print(kyle_camel.feed())

class Zoney():
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date.today()
        self.walking = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

    def __str__(self):
      return f"{self.name} the {self.species}"

zelda_zoney = Zoney("Zelda", "Zoney", "Evening", "Hay")
print(f'{zelda_zoney} is available to pet during the {zelda_zoney.shift} shift.')
print(zelda_zoney.feed())

class Skunk():
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date.today()
        self.walking = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

    def __str__(self):
      return f"{self.name} the {self.species}"

steve_skunk = Skunk("Steve", "Skunk", "Afternoon", "Garbage")
print(f'{steve_skunk} is available to pet during the {steve_skunk.shift} shift.')
print(steve_skunk.feed())

class Armadillo():
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date.today()
        self.walking = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

    def __str__(self):
      return f"{self.name} the {self.species}"

andy_armadillo = Armadillo("Andy", "Armadillo", "Morning", "Bugs")
print(f'{andy_armadillo} is available to pet during the {andy_armadillo.shift} shift.')
print(andy_armadillo.feed())

class Buffalo():
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date.today()
        self.walking = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')

    def __str__(self):
      return f"{self.name} the {self.species}"

bob_buffalo = Buffalo("Bob", "Buffalo", "Morning", "Buffalo Burger")
print(f'{bob_buffalo} is available to pet during the {bob_buffalo.shift} shift.')
print(bob_buffalo.feed())