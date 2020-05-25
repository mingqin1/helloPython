from array import array
import reprlib
import math


class Vector:
    typecode = 'd'

    # The self._components instance “protected” attribute will hold an array with the Vector components.
    def __init__(self, components):
        self._components = array(self.typecode, components)

    # To allow iteration, we return an iterator over self._components.
    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        # Use reprlib.repr() to get a limited-length representation of self._components (e.g., array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])).
        components = reprlib.repr(self._components)
        # Remove the array('d', prefix and the trailing ) before plugging the string into a Vector constructor call.
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        # Build a bytes object directly from self._components.
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        # We can’t use hypot anymore, so we sum the squares of the components and compute the sqrt of that.
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        # The only change needed from the earlier frombytes is in the last line: we pass the memoryview directly to the constructor, without unpacking with * as we did before.
        return cls(memv)
