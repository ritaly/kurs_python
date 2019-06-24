class Wojownik:
    def __init__(self):
        self._doswiadczenie = 0

    def __repr__(self):
        nazwa = self.__class__.__name__
        return f'{nazwa}: hp={self._zycie}, exp={self._doswiadczenie}'

    def maszeruj(self, dystans):
        nazwa = self.__class__.__name__
        print(f'{nazwa}: Przeszedłem {dystans}m')
        self._doswiadczenie += 0.02 * dystans


class Rycerz(Wojownik):
    def __init__(self):
        super().__init__()
        self._zycie = 60

    def atakuj(self):
        print('Rycerz: Machnąłem mieczem!')
        self._doswiadczenie += 0.3


class Lucznik(Wojownik):
    def __init__(self):
        super().__init__()
        self._zycie = 40

    def atakuj(self):
        print('Łucznik: Wypuściłem strzałę!')
        self._doswiadczenie += 0.4

def main():
    p = Rycerz()
    print(p)
    p.maszeruj(10)
    print(p)
    p.atakuj()
    print(p)

    l = Lucznik()
    print(l)
    l.maszeruj(15)
    print(l)
    l.atakuj()
    print(l)


if __name__ == '__main__':
    main()
