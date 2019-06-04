def create_car(brand, type, year):
    car = {}
    car['marka'] = brand
    car['model'] = type
    car['rocznik'] = year
    return car

brand = input("Podaj markę auta: ")
type = input("Podaj model auta: ")
year = int(input("Podaj rocznik: "))

cars_dict = create_car(brand, type, year)

print(cars_dict)