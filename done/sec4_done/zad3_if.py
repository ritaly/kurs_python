plot = int(input('podaj ocene 1-10 pod fabuly: '))

general = int(input('ogolne wrazenie 1-10:'))

cover = int(input('ocena okladki: '))

avg = (plot + general + cover) / 3


if avg > 7:
    print('ksiazka godna polecenia: ', avg)
elif avg >= 4:
    print('ksiązka srednia: ', avg)
else:
    print('ksiazka nie warta uwagi: ', avg)