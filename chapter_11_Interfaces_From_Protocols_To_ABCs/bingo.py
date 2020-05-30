import random

# BingoCage is a concrete subclass of Tombola

from tombola import Tombola

# This BingoCage class explicitly extends Tombola.


class BingoCage(Tombola):

    def __init__(self, items):
        #  random.SystemRandom implements the random API on top of the os.urandom(…) function,
        # which provides random bytes “suitable for cryptographic use” according to the os module docs.
        self._randomizer = random.SystemRandom()
        self._items = []
        # Delegate initial loading to the .load(…) method.
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        #  Instead of the plain random.shuffle() function, we use the .shuffle() method of our SystemRandom instance.
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    # It’s not needed to satisfy the Tombola interface, but there’s no harm in adding extra methods.

    def __call__(self):
        self.pick()
