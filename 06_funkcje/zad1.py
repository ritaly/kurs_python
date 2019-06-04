# Funkcja pyta uzytkownika o pary ksiazka ocena

# Funkcja pyta uzytkownika o ksiazke i wyswietla ocene

# Obsluga bledu uzytkownika


def uzupelnij_biblioteke():
    biblioteka = {}
    ile = int(input("Ile ksiazek? "))
    for i in range(ile):
        tytul = input("Podaj tytul ksiazki: ")
        ocena = int(input("Podaj ocene w skali 1-10: "))
        biblioteka[tytul] = ocena
    return biblioteka

def znajdz_ksiazke(tytul):
    print("Ocena wybranej ksiazki", tytul, " to: ",  bibl[tytul])


bibl = uzupelnij_biblioteke()
ksiazka = input("Jakiej ksiazki ocene chcesz sprawdzic: ")

if ksiazka in bibl:
    znajdz_ksiazke(ksiazka)
else:
    print("Nie mamy tej pozycji")


