"""
A simple two-dimensional vector class

"""

from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        %r to obtain the standard representation of the attributes to be displayed

        %r placeholder in classic formatting with the % operator, and the !r conversion field
        in the new Format String Syntax used in the str.format method.

        """
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __str__(self):
        """
          Difference between __str__ and  __repr__
          https://stackoverflow.com/questions/1436703/difference-between-str-and-repr/1436756#1436756
          https://www.journaldev.com/22460/python-str-repr-functions
        """
        return 'Vector(x =' + str(self.x) + ', y=' + str(self.y) + ')'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v = Vector(1, 3)
# __str__() example
print(v)
print(v.__str__())
print(str(v))

# __repr__() example
print(v.__repr__())
print(repr(v))
