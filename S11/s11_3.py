from random import shuffle
l = list(range(10))
shuffle(l)
print(l)

from PythonTest.S1.s1_1 import FrenchDeck
deck = FrenchDeck()

def set_card(deck, position, card):
    deck._cards[position] = card
FrenchDeck.__setitem__ = set_card
shuffle(deck)
print(deck[:5])