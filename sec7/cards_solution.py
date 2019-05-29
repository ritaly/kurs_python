def is_visa(number):
    if len_of_number not in [13, 16]:
        return False
    else:
        if number[0] == '4':
            return True
        else:
            return False


def is_mastercard(number):
    if len_of_number != 16:
        return False
    else:
        if 51 <= int(number[:2]) <= 55:
            return True
        elif 2221 <= int(number[:4]) <= 2720:
            return True
        else:
            return False


def is_american_express(number):
    if len_of_number != 15:
        return False
    else:
        if number[:2] == '34' or number[:2] == '37':
            return True
        else:
            return False


def save_to_file(card_type, number):
    save_file = card_type + '.txt'
    with open(save_file, 'a') as sf:
        sf.write(number + '\n')


def check_card_type(number):
    # czy visa
    if is_visa(number):
        print("to visa")
        save_to_file('visa', number)
    # czy jest master
    elif is_mastercard(number):
        print("to mastercard")
        save_to_file('mastercard', number)
    # czy american
    elif is_american_express(number):
        print("yay american express to jeszcze istnieje?")
        save_to_file('americanexpress', number)
    else:
        print("nie znam twojej karty")


# pobrać dane z pliku
filename = 'cards_list.txt'
with open(filename, 'r') as fo:
    num_list = fo.readlines()

print(num_list)

# przekazac pojed. nr karty do funkcji check_card_type(number)
for num in num_list:
    num = num.replace('\n', '')
    len_of_number = len(num)
    if len_of_number not in [13, 15, 16]:
        print("Dlugosc nieprawidlowa: ", num)
        continue
    check_card_type(num)