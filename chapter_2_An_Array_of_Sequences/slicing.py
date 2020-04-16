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

"""
Using + and * with Sequences
Both + and * always create a new object, and never change their operands.
Usually both operands of + must be of the same sequence type, and neither of them is modified but a new sequence of the same type is created as result of the concatenation.

"""
l = [1, 2, 3]
print(l * 5)

print(5 * 'abcd')

"""
WARNING
Beware of expressions like a * n when a is a sequence containing mutable items because the result may surprise you.
 For example, trying to initialize a list of lists as my_list = [[]] * 3
 will result in a list with three references to the same inner list, which is probably not what you want.
"""
# The outer list is made of three references to the same inner list.
weird_board = [['_'] * 3] * 3
print(weird_board)

# Placing a mark in row 1, column 2, reveals that all rows are aliases referring to the same object.
weird_board[1][2] = 'O'

print(weird_board)

# Create a list of three lists of three items each
board = [['_'] * 3 for i in range(3)]
print(board)

board[1][2] = 'X'
print(board)


"""
list.sort and the sorted Built-In Function

The list.sort method sorts a list in place—that is, without making a copy.
It returns None to remind us that it changes the target object, and does not create a new list.

In contrast, the built-in function sorted creates a new list and returns

"""

fruits = ['grape', 'raspberry', 'pear', 'banana']
print(sorted(fruits, reverse=True, key=len))
print(id(sorted(fruits)))

print(fruits)
print(id(fruits))
# This sorts the list in place, and returns None
print(fruits.sort(reverse=True, key=len))
#  now fruits is sorted
print(fruits)
