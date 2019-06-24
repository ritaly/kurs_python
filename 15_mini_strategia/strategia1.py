class Rycerz:
    def __init__(self):
        self.zycie = 60
        self.doswiadczenie = 0

    def __repr__(self):
        return f'Rycerz: hp={self.zycie}, exp={self.doswiadczenie}'

    def maszeruj(self, dystans):
        print(f'Rycerz: Przeszedłem {dystans}m')
        self.doswiadczenie += 0.02 * dystans

    def atakuj(self):
        print('Rycerz: Machnąłem mieczem!')
        self.doswiadczenie += 0.3

def main():
    p = Rycerz()
    print(p)
    p.maszeruj(10)
    print(p)
    p.atakuj()
    print(p)

if __name__ == '__main__':
    main()
