"""
the types module provides a wrapper class called MappingProxyType, which, given a mapping,
returns a mappingproxy instance that is a read-only but dynamic view of the original mapping.
This means that updates to the original mapping can be seen in the mappingproxy, but changes cannot be made through it
"""
from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)

print('d_proxy: ', d_proxy)
# Items in d can be seen through d_proxy.
print(d_proxy[1])

d[2] = 'B'

# d_proxy is dynamic: any change in d is reflected.
print(d_proxy[2])

#  Changes cannot be made through d_proxy.
d_proxy[2] = 'x'
