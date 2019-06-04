"""Stwórz grę wisielec “bez wisielca”.

Komputer losuje wyraz z dostępnej w programie listy wyrazów.

Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)

Użykownik podaje literę.

Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
“Trafione!” oraz napis ze znanymi literami.

W przeciwnym wpadku pokaż komunikat:
“Nie trafione, spróbuj jeszcze raz!”.

Możesz ograniczyć liczbę prób do np. 10."""

import random

def random_secret_word(list_of_words):
    secret_word = random.choice(list_of_words)
    return secret_word

def get_a_word():
    while True:
        print('------------- HANGMAN GAME -------------')
        lvl = input("Difficulty:\n 1 - easy mode\n 2 - hard mode\n")
        if lvl == '1':
            return random_secret_word(easy)
        elif lvl == '2':
            return random_secret_word(hard)
        else:
            print('Really? No such option, try again.')
            continue
            

def is_included(char):
    if char in password:
        return True
    else:
        return False

def make_a_guess(hangman):
    counter = 0
    while counter < 10:
        print('---------------------------------------')
        letter = input('Guess a letter: ')
        if is_included(letter):
            print ('Letter', letter, 'is included.')
            hangman = update_hangman(letter, hangman)
            print(hangman)
        else:
            print ('Sorry...NOPE!\n')

        if  is_winner(hangman):
            print('You win! End of game')
            break

        counter += 1

    return hangman

def update_hangman(char, new_hangman):
    for i in range(len(password)):
        if password[i] == char:
            new_hangman[i] = char

    return new_hangman

def is_winner(hangman):
    if  '_' not in hangman:
        return True
    else:
        return False
        
    

# start gry!
easy = ['banana', 'apple', 'watermelon', 'grape', 'strawberry', 'avocado', 'peach']
hard = ['rambutan', 'jackfruit', 'aguaje', 'cherimoya', 'pandanus', 'markutlime']
password = get_a_word()

dashes = ['_'] * len(password)
print('Tip: This is a fruit')
print('Your hangman:', dashes)

make_a_guess(dashes)

if is_winner(dashes) == False:
    print('You lose!')
    print('Secret password was: ', password)
            
