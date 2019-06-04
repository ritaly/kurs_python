n = int(input('podaj wielkosc: '))
a = [['-'] * n] * n

for row in a:
    print(' '.join(row))

# [print(' '.join(row)) for row in a]