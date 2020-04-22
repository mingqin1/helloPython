import random


class BingoCage:

    #  __init__ accepts any iterable; building a local copy prevents unexpected side effects on any list passed as an argument.
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        # Raise exception with custom message if self._items is empty.
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo.pick())
print(bingo.pick())
print(bingo.pick())

print(callable(bingo))
