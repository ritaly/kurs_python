class Hand(object):
    """ Ręka - karty do gry w ręku gracza. """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<pusta>"
        return rep

        def clear(self):
            self.cards = []

        def add(self, card):
            self.cards.append(card)

        def give(self, card, other_hand):
            self.cards.remove(card)
            other_hand.add(card)