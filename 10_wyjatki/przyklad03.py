user_file = input('Podaj nazwe pliku:')

try:
    fopen = open(user_file, 'r')
    content = fopen.read()
finally:
    fopen.close()
