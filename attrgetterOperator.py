from collections import namedtuple
from operator import attrgetter
metro_data = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
              ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
              ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
              ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
              ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)), ]

"""Use namedtuple to define LatLong.
"""
LatLong = namedtuple('LatLong', 'lat long')
"""define Metropolis.
"""
Metropolis = namedtuple('Metropolis', 'name cc pop coord')

"""Build metro_areas list with Metropolis instances;
    note the nested tuple unpacking to extract (lat, long)
    and use them to build the LatLong for the coord attribute of Metropolis.
"""
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
               for name, cc, pop, (lat, long) in metro_data]
metro_areas[0]
print('metro_areas[0]: ', metro_areas[0])

"""Define an attrgetter to retrieve the name and the coord.lat nested attribute.
"""
name_lat = attrgetter('name', 'coord.lat')
"""Use attrgetter again to sort list of cities by latitude
"""
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))
