#!/usr/bin/env python3

import numpy

l = [10, 20, 30, 40, 50, 60]
print(l[:2])  # split at 2

print(l[2:])

"""
slicing objects

s[a:b:c] can be used to specify a stride or step c,
causing the resulting slice to skip items. The stride can also be negative,
returning items in reverse.

slice [start:stop:step],
"""

s = 'bicycle'
print(s[::3])
print(s[0:6:3])

print(s[::-1])

print(s[6:0:-2])

"""
Multidimensional Slicing and Ellipsis

 a two-dimensional numpy.ndarray can be fetched using the syntax a[i, j] and
 a two-dimensional slice obtained with an expression like a[m:n, k:l].

 The ellipsis—written with three full stops (...) and not … (Unicode U+2026)—is recognized as a token by the Python parser.
 It is an alias to the Ellipsis object, the single instance of the ellipsis class.2 As such, it can be passed as an argument to
 functions and as part of a slice specification, as in f(a, ..., z) or a[i:...].
 NumPy uses ... as a shortcut when slicing arrays of many dimensions; for example,
 if x is a four-dimensional array, x[i, ...] is a shortcut for x[i, :, :, :,].

"""

a = numpy.arange(12)
print(a)
print(type(a))

#  Inspect the dimensions of the array: this is a one-dimensional, 12-element array.
print(a.shape)

# Change the shape of the array, adding one dimension, then inspecting the result.
a.shape = 3, 4
print(a)
print(a.shape)

# Get row at index 2.
print(a[2])

# Get element at index 2, 1.
print(a[2, 1])

#  Get column at index 1.
print(a[:, 1])

print(a.transpose())

"""
Assigning to Slices

Mutable sequences can be grafted, excised, and otherwise modified in place using slice notation
on the left side of an assignment statement or as the target of a del statement.
The next few examples give an idea of the power of this notation:
"""
l = list(range(10))
print(l)

l[2:5] = [20, 30]
print(l)

del l[5:7]
print(l)

l[3::2] = [11, 22]
print(l)

l[2:5] = [100]
print(l)
