# Tombola is an ABC with two abstract methods and two concrete methods

import abc

# To define an ABC, subclass abc.ABC.


class Tombola(abc.ABC):
    # An abstract method is marked with the @abstractmethod decorator, and often its body is empty except for a docstring.
    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable."""

    # The docstring instructs implementers to raise LookupError if there are no items to pick.
    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it.

        This method should raise `LookupError` when the instance is empty.
        """
    # An ABC may include concrete methods.

    def loaded(self):
        """Return `True` if there's at least 1 item, `False` otherwise."""
        # Concrete methods in an ABC must rely only on the interface defined by the ABC (i.e., other concrete or abstract methods or properties of the ABC).
        return bool(self.inspect())

    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        # We can’t know how concrete subclasses will store the items, but we can build the inspect result by emptying the Tombola with successive calls to .pick()…
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        # …then use .load(…) to put everything back.
        self.load(items)
        return tuple(sorted(items))
