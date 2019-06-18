class Player(object):
    """ Gracz w grze strzelance. """

    def blast(self, enemy):
        print('Gracz razi wroga.\n')
        enemy.die()


class Alien(object):
    """ Obcy w grze strzelance. """

    def die(self):
        print('Obcy z trudem łapie oddech, "To już koniec. Ale prawdziwie wielki koniec... \n',
              'Larwy moje pomszczą mnie pewnego dnia... \n',
              'Żegnaj, okrutny Wszechświecie!"')


if __name__ == '__main__':
    print('\t\tŚmierć Obcego\n')
    hero = Player()
    invader = Alien()
    hero.blast(invader)
    input('\n\nAby zakończyć program, naciśnij klawisz Enter.')