from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    # The @property decorator marks the getter method of a property.
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    #  hashable vactor
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    #  Class method is modified by the classmethod decorator.
    #  to define a method that operates on the class and not on instances.
    #  classmethod changes the way the method is called, so it receives the class itself as the first
    #  argument, instead of an instance.


    #  alternative constructors
    #  rombytes actually uses the cls argument by invoking it to build a new instance: cls(*memv).
    #  By convention, the first parameter of a class method should be named cls
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)




"""
prevent accidental overwriting of a “private” attribute in a subclass.


To prevent this, if you name an instance attribute in the form __mood (two leading underscores and zero or at most one trailing underscore),
Python stores the name in the instance __dict__ prefixed with a leading underscore and the class name, so in the Dog class, __mood becomes _Dog__mood,
and in Beagle it’s _Beagle__mood. This language feature goes by the lovely name of name mangling.

To prevent this, if you name an instance attribute in the form __mood (two leading underscores and zero or at most one trailing underscore),
Python stores the name in the instance __dict__ prefixed with a leading underscore and the class name, so in the Dog class, __mood becomes _Dog__mood,
and in Beagle it’s _Beagle__mood. This language feature goes by the lovely name of name mangling.

"""
v1 = Vector2d(3, 4)
print(v1.__dict__)

print('v1._Vector2d__x: ', v1._Vector2d__x)
