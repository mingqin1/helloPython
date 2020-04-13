import collections

"""
FrenchDeck implicitly inherits from object,4 its functionality is not inherited, but comes from leveraging the data model and composition.
By implementing the special methods __len__ and __getitem__, our FrenchDeck behaves like a standard Python sequence, allowing it to benefit
from core language features (e.g., iteration and slicing) and from the standard library, as shown by the examples using random.choice,
reversed, and sorted. Thanks to composition, the __len__ and __getitem__ implementations can hand off all the work to
a list object, self._cards.
"""

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        """
        listComps 
        """
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


"""
function that ranks cards by that rule, returning 0 for the 2 of clubs and 51 for the ace of spades:
"""

"""
ranking cards is by rank (with aces being highest), then by suit in the order of spades (highest),
then hearts, diamonds, and clubs (lowest)

"""
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):

    rank_value = FrenchDeck.ranks.index(card.rank)
    # 0 to 12 are rank value for
    print(rank_value)
    print(len(suit_values))
    print(suit_values[card.suit])
    print(rank_value * len(suit_values) + suit_values[card.suit])
    print("------------------------------")
    return rank_value * len(suit_values) + suit_values[card.suit]


deck = FrenchDeck()

for card in sorted(deck, key=spades_high):
    print(card)
