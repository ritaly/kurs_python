# a teraz?

print('Początek programu')

try:
    num = 13 / 0
except ZeroDivisionError:
    print('Ktoś próbował dzielić przez zero!')

print('Program działa dalej.')