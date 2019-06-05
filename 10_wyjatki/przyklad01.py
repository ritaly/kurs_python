try:
    a = float(input('Gimme numeric value: '))
except ValueError as err:
    print('Your error returns:',err)
    a = 0

b = 10 + a
print(b)
