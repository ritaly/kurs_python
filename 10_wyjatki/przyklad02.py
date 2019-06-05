randomList = ['a', 0, 2, 5, 6]

for value in randomList:
    try:
        print("wartosc: ", value)
        div = 1/int(value)
        break
    except (ValueError, ZeroDivisionError) as error:
        print("Oops! Wystapil blad: ", error)
        print("Nastepna wartosc")
        print()

print("Dzielenie przez", value, "wynosi", div)