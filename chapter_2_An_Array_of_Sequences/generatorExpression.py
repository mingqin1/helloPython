import array

"""
Generator expressions are enclosed in parentheses rather than brackets

using a generator expression would save the expense of building a list

genexp saves memory because it yields items one by one using the iterator protocol instead of building a whole
list just to feed another constructor.


"""
symbols = '$¢£¥€¤'
aTuple = tuple(ord(symbol) for symbol in symbols)
print(aTuple)

"""
The array constructor takes two arguments, so the parentheses around the generator expression are mandatory.

The first argument of the array constructor defines the storage type used for the numbers in the array

"""
anArray = array.array('I', (ord(symbol) for symbol in symbols))
print(anArray)


colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

"""
tshirts list builds up sequence consums memory
"""
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
