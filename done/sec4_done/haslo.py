print('''Podaj haslo:
      - powinno być dłuższe niż 7 znaków 
      - powinno składać się z liter i cyfr
      - zawierać conajmniej jedną wielką literę
      ''')

# pobranie hasla od uzytkownika
password = input()

# warunek 1 -> dlugosc hasla
correct_len = len(password) > 7

# warunek2 -> liter i cyfr
# - jest alfanumeryczne
# - nie składa się z samych liter
# - sie składa się z samych cyfr

alpha_num = password.isalnum()
not_all_letters = not password.isalpha()
not_all_digits = not password.isdigit()

correct_alnum = alpha_num and not_all_letters and not_all_digits

# warunek3 -> conajmniej jedna duza litera
one_upper = not password.islower() and not password.isupper()

if correct_len and correct_alnum and one_upper:
    print('twoje haslo jest prawidlowe')
else:
    print('popraw haslo')