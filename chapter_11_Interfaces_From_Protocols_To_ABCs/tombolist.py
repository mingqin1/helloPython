from random import randrange

from tombola import Tombola

# Tombolist is registered as a virtual subclass of Tombola.
@Tombola.register
# Tombolist extends list.
class TomboList(list):

    def pick(self):
        # Tombolist inherits __bool__ from list, and that returns True if the list is not empty.
        if self:
            position = randrange(len(self))
            # Our pick calls self.pop, inherited from list, passing a random item index.
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')
    # Tombolist.load is the same as list.extend.
    load = list.extend

    def loaded(self):
        # loaded delegates to bool
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

# Tombola.register(TomboList)


issubclass(TomboList, Tombola)
print('issubclass(TomboList, Tombola): ', issubclass(TomboList, Tombola))

t = TomboList(range(100))
isinstance(t, Tombola)
print('isinstance (t, Tombola): ', isinstance(t, Tombola))

TomboList.__mro__
print('TomboList.__mro__: ', TomboList.__mro__)