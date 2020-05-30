from array import array
import reprlib
import math
import numbers
import functools
import operator


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
# two methods needed to make Vector behave as a sequence: __len__ and __getitem__
# (the latter now implemented to handle slicing correctly).

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        # Get the class of the instance (i.e., Vector) for later use.
        cls = type(self)
        # If the index argument is a slice…
        if isinstance(index, slice):
            # …invoke the class to build another Vector instance from a slice of the _components array.
            return cls(self._components[index])
        # If the index is an int or some other kind of integer…
        elif isinstance(index, numbers.Integral):
            # …just return the specific item from _components.
            return self._components[index]
        else:
            # Otherwise, raise an exception.
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        #  Get the Vector class for later use.
        cls = type(self)
        # If the name is one character, it may be one of the shortcut_names
        if len(name) == 1:
            # Find position of 1-letter name; str.find would also locate 'yz' and we don’t want that,
            # this is the reason for the test above.
            pos = cls.shortcut_names.find(name)
            # If the position is within range, return the array element.
            if 0 <= pos < len(self._components):
                return self._components[pos]
        # If either test failed, raise AttributeError with a standard message text.
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    #  customize the logic for setting attributes in our Vector class in order to avoid this inconsistency
    # def __setattr__(self, name, value):
    #     cls = type(self)
        #   Special handling for single-character attribute names.
    #     if len(name) == 1:
        # If name is one of xyzt, set specific error message.
    #         if name in cls.shortcut_names:
    #             error = 'readonly attribute {attr_name!r}'
        #   If name is lowercase, set error message about all single-letter names.
    #         elif name.islower():
    #             error = "can't set attributes 'a' to 'z' in {cls_name!r}"
    #         else:
        #   Otherwise, set blank error message.
    #             error = ''
        #  If there is a nonblank error message, raise AttributeError.
    #         if error:
    #             msg = error.format(cls_name=cls.__name__, attr_name=name)
    #             raise AttributeError(msg)
        #    Default case: call __setattr__ on superclass for standard behavior.
    #     super().__setattr__(name, value)

    #  Create a generator expression to lazily compute the hash of each component.
    #  Feed hashes to reduce with the xor function to compute the aggregate hash value; the third argument, 0,
    # is the initializer (see next warning).
    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes)

    def __eq__(self, other):
        # If the len of the objects are different, they are not equal.
        if len(self) != len(other):
            return False
        # zip produces a generator of tuples made from the items in each iterable argument.
        # See “The Awesome zip” if zip is new to you.
        # The len comparison above is needed because zip stops producing values without w
        # arning as soon as one of the inputs is exhausted.
        for a, b in zip(self, other):
            if a != b:
                return False
        return True



v7 = Vector(range(7))
# An integer index retrieves just one component value as a float.
v7[-1]
print('v7[-1]: ', v7[-1])

# A slice index creates a new Vector.
v7[1:4]
print('v7[1:4]: ', v7[1:4])

# A slice of len == 1 also creates a Vector.
v7[-1:]
print('v7[-1:]: ', v7[-1:])
# Vector does not support multidimensional indexing, so a tuple of indices or slices raises an error.
# v7[1, 2]

v = Vector(range(5))
print('v: ', v)

# Inappropriate behavior: assigning to v.x raises no error, but introduces an inconsistency
v.x
print('v.x: ', v.x)

v.x = 10
print('v.x: ', v.x)
print('v: ', v)
