class Student:
    def __init__(self, name, last, age):
        self.name = name
        self.last = last
        self.age = age

    def __repr__(self):
        return f'Student: {self.name.capitalize()} {self.last.capitalize()}'

    @property
    def email(self):
        return f'{self.name}.{self.last}@university.com'

    @property
    def fullname(self):
        return f'{self.last}.{self.name}'

    @fullname.setter
    def fullname(self, last_name):
        self.last, self.name = last_name.split()

    @fullname.deleter
    def fullname(self):
        self.last, self.name = None, None
        print('Dane usuniete!')

obj_anna = Student('ana', 'kowalska', 23)
print(obj_anna)
print(obj_anna.email)
print('----------------------')
obj_anna.name = 'anna'
print(obj_anna)
print(obj_anna.email)

obj_anna.fullname = 'Zamężna Anna'
print(obj_anna)

del obj_anna.fullname