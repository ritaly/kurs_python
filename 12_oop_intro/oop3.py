class Student:

    university_name = 'Lans&Bans Academy'

    def __init__(self, name, last, age):
        self.name = name
        self.last = last
        self.age = age

    def email(self):
        return '{}.{}.university.com'.format(self.name, self.last)


obj_anna = Student('anna', 'kowalska', 23)
print(obj_anna.email)
obj_arek = Student('arkadiusz', 'nowak', 21)
print(obj_arek.email)

print('Studentka {} {}'.format(obj_anna.name.capitalize(), obj_anna.last.capitalize()))

print(obj_anna.email())
