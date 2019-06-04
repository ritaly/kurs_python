import random


def show_quote():
    quote = random.choice(content)
    print('Quote of the day:')
    print('*' * 70)
    print(quote.center(70))
    print('*' * 70)


filename = 'quote_list.txt'
with open(filename, 'r') as fopen:
    content = fopen.readlines()
show_quote()
