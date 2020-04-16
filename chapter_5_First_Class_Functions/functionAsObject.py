

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
