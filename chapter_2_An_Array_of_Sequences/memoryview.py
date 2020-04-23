import array as array

"""
A memoryview is essentially a generalized NumPy array structure in Python itself (without the math).
It allows you to share memory between data-structures (things like PIL images, SQLlite databases, NumPy arrays, etc.)
without first copying. This is very important for large data sets.
"""

numbers = array.array('h', [-2, -1, 0, 1, 2])
mem = memoryview(numbers)
len(mem)

mem[0]

"""
memoryview.cast method lets you change the way multiple bytes are read or written as units without moving bits around
"""
# an example of changing a single byte of an array of 16-bit integers.

mem_oct = mem.cast('B')


print(mem_oct.tolist())

mem_oct[5] = 4
print(numbers)
