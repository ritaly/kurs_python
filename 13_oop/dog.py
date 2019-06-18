class Dog:
    kingdom = 'Animals'

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self, sound='ufuf'):
        print(sound * self.age)

    def is_healthy(self, state=True):
        return 'Jest zdrowy: ' + str(state)


dyzio = Dog('Dyzio', 3, 'mops')
dyzio.bark()
dyzio.bark('auu')
print(dyzio.is_healthy())
print(dyzio.is_healthy(False))