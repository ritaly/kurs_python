start = 0
limit = 200
step = 20

fahr = start
# wykonuj pętlę dopóki wartość fahr jest <= od zmiennej limit
while(fahr <= limit):
    # oblicz stopnie C i przypisz wynik do zmiennej lokalnej celsius
    celcius = 5/ 9 * (fahr - 32)
    # wypisz zmienne na ekran: fahr <tabulacja> celsius
    print(fahr, '\t', celcius)
    fahr += step
