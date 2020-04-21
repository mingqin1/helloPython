from functools import reduce
from operator import add


def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n - 1)


def reverse(word):
    return word[::-1]


# __doc__ is one of several attributes of function objects
factorial.__doc__
'return n!'

print(type(factorial))


# shows the “first class” nature of a function object.
fact = factorial
print(fact)
print(fact(5))
print(map(factorial, range(11)))

print(list(map(factorial, range(11))))

"""
 Higher-order Functions
"""
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))

# Sorting a list of words by their reversed spelling
print(sorted(fruits, key=reverse))

# Modern Replacements for map, filter, and reduce
# using map -Build a list of factorials from 0! to 5!.
list(map(fact, range(6)))
# using list comprehension
[fact(n) for n in range(6)]

# using filter and map -List of factorials of odd numbers up to 5!,
list(map(factorial, filter(lambda n: n % 2, range(6))))
# using list comprehesnion
[factorial(n) for n in range(6) if n % 2]

# using reduce -Sum of integers up to 99 performed with reduce and sum
reduce(add, range(100))
# using sum
sum(range(100))
