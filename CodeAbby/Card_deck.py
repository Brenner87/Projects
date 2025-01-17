
import collections
import random

def main():

    Card = collections.namedtuple('Card', ['rank','suite'])
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(deck[-1])
    print (random.choice(deck))
    print(random.choice(deck))
    print (deck[:3])


class FrenchDeck(object):
    Card = collections.namedtuple('Card', ['rank','suite'])
    ranks=[str(n) for n in range(2,11)] + list('JQKA')
    suits='spades diamonds  clubs hearts'.split()
    def __init__(self):
        self._cards=[self.Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__=='__main__':
    main()