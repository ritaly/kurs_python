class Book:
    has_cover = True

    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def show(self):
        print(self.title, self.author, self.year)

    def get_read_time(self):
        time_in_h = int(self.pages * 2.5 // 60)
        time_in_m = int(self.pages * 2.5 % 60)
        return str(time_in_h) + ':' +str(time_in_m)

ksiazka1 = Book('Granica', 'Zofia', '1889', 210)
ksiazka2 = Book('Lalka', 'Henio', '1880', 430)

print(ksiazka1.title)
print(ksiazka2.title)

ksiazka1.show()
t = ksiazka1.get_read_time()
print(t)
print('----------------')
t2 = Book.get_read_time(ksiazka2)
print(t2)
Book.show(ksiazka2)

print('----------------')

a = 'Abrakadabra'
print(a)
print(a.upper())
print(a.lower())
print(type(a))
print(type(ksiazka1))
print(str.upper(a))

