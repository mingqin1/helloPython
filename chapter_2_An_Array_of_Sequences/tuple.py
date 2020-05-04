from collections import namedtuple
import os

"""
shows tuples being used as records.
"""
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

"""
A list of tuples of the form (country_code, passport_number).
"""
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]


for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)


lax_coordinates = (33.9425, -118.408056)
# tuple unpacking
latitude, longitude = lax_coordinates

for i in lax_coordinates:
    print('i: ', i)


"""
elegant application of tuple unpacking is swapping the values of variables without using a temporary variable:
"""
a, b = (1, 3)
b, a = a, b
print(b)
print(a)


"""
tuple unpacking is prefixing an argument with a star when calling a function:
"""
t = (20, 8)
print(divmod(*t))

quotient, remainder = divmod(*t)

print((quotient,  remainder))

"""
tuple unpacking: enabling functions to return multiple values in a way that is convenient to the caller
"""

_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')

print(filename)
print(_)  # a dummy variable like _ is used as placeholder


"""
USING * TO GRAB EXCESS ITEMS
"""
a, b, *rest = range(5)
print(rest)


"""
Nested Tuple Unpacking

The tuple to receive an expression to unpack can have nested tuples, like (a, b, (c, d)),
and Python will do the right thing if the expression matches the nesting structure.
"""

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
"""
By assigning the last field to a tuple, we unpack the coordinates
"""
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))


"""
Named Tuples
"""
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
tokyo
City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722,
                                                                 139.691667))
print(tokyo.population)

print(tokyo.coordinates)

print(tokyo[1])


"""
Tuples as Immutable Lists
"""
