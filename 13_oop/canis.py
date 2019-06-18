class Canis:
    paws = 4

    def __init__(self):
        print("Canis is a genus, family: Canidae")

    def show_description(self):
        print(
            '''Species of this genus are distinguished
             by their moderate to large size, their massive,
             well-developed skulls and dentition,
             long legs, and comparatively short ears and tails''')


class Dog(Canis): # psy dziedziczą z klasy wilków

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


    def bark(self, sound='uf'):
        print(sound * self.age)


dyzio = Dog('Dyzio', 3, 'mops')

print(dyzio.paws)
dyzio.show_description()