# Zadanie 11
# Stwórz grę ciepło zimno.
# Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf.
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz.
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random
comp_number = random.randint(1, 100)

guess_counter = 0
precision = 99

while guess_counter < 6:
    user_number = int(input('Podaj liczbę od 1 - 100: '))
    guess_counter += 1
    if user_number == comp_number:
        print('Brawo! Udało ci się zgadnąć', comp_number)
        break
    elif guess_counter == 6:
        print('Nie udało się. Liczba to', comp_number)
    else:
        if precision > abs(comp_number - user_number):
            precision = abs(comp_number - user_number)
            print('Cieplej!')
        elif precision < abs(comp_number - user_number):
            print('Zimniej!')
        else:
            print('Ani cieplej ani zimniej, spróbuj jeszcze raz!')

