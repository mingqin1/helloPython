def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


factorial(42)

factorial.__doc__
'return n!'

type(factorial)

fact = factorial


list(map(fact, range(11)))

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

sorted(fruits, key=len, reverse=True)

