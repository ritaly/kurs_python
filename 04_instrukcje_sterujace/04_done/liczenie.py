text = 'Py&0n17su%^&i5ve'

counter = len(text)
char_count = 0
digit_count = 0
symbol_count = 0

for char in text:
    if char.islower() or char.isupper():
        char_count += 1
    elif char.isnumeric():
        digit_count += 1
    else:
        symbol_count += 1

print('Suma znaków: ', counter)
print('Litery = ', char_count, 'Cyfry = ', digit_count, 'Symbole = ', symbol_count)
