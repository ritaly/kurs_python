"""
Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
Załóż, że spalanie na 100km wynosi 6,4 l,
trasa to 120km,
litr benzyny kosztuje 5,04 zł.
"""

fuel_per_100 = 6.4
distance = 120
price = 5.04

total_cost = fuel_per_100 * distance/100 * price

print('Wycieczka bedzie kosztowac', total_cost, 'zl.')
