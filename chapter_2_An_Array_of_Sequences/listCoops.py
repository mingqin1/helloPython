symbols = '$¢£¥€¤'
"""
a listcomp is meant to do one thing only: to build a new list.
"""
codes = [ord(symbol) for symbol in symbols]
print(codes)
"""
Listcomps can generate lists from the Cartesian product of two or more iterables. The items that make up the
cartesian product are tuples made from items from every input iterable.

This generates a list of tuples arranged by color, then size
"""

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
