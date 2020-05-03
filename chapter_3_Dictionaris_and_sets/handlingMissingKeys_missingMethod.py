import collections


class StrKeyDict(collections.UserDict):

    #   if you subclass dict and provide a __missing__ method, the standard dict.__getitem__ will
    #  call it whenever a key is not found, instead of raising KeyError.
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        # we can assume all stored keys are str and we can check on self.data
        return str(key) in self.data

    # __setitem__ converts any key to a str. This method is easier to overwrite when we can
    # delegate to the self.data attribute.
    def __setitem__(self, key, item):
        self.data[str(key)] = item


d = StrKeyDict([('2', 'two'), ('4', 'four')])


#  Tests for item retrieval using `d.get(key)` notation::
d.get(1, 'N/A')
print(d.get(1, 'N/A'))

# Tests for the `in` operator::
print(2 in d)
print(1 in d)
# Tests for item retrieval using `d[key]` notation::
print(d[1])
