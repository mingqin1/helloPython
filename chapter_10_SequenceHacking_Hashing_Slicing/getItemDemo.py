class MySeq:
    def __getitem__(self, index):
        return index


s = MySeq()
s[1]
print('s[1]: ', s[1])

s[1:4]
print('s[1:4]: ', s[1:4])

s[1:4:2]
# slice(1, 4, 2) means start at 1, stop at 4, step by 2.
print('s[1:4:2]: ', s[1:4:2])

# Surprise: the presence of commas inside the [] means __getitem__ receives a tuple.
s[1:4:2, 9]
print('s[1:4:2, 9]: ', s[1:4:2, 9])


# The tuple may even hold several slice objects.
s[1:4:2, 7:9]
print('s[1:4:2, 7:9]: ', s[1:4:2, 7:9])


# slice is a built-in type
slice
print('slice: ', slice)

dir(slice)
print('dir( slice): ', dir(slice))

help(slice.indices)
print('help( slice.indices): ', help(slice.indices))

slice("ABCDE")

slice(None, 10, 2).indices(5)
print('slice(None, 10, 2).indices(5): ', slice(None, 10, 2).indices(5))

slice(-3, None, None).indices(5)
print('slice(-3, None, None).indices(5): ', slice(-3, None, None).indices(5))