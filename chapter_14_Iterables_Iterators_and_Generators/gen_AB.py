def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')

# The list comprehension eagerly iterates over the items yielded by the generator object produced by calling gen_AB(): 'A' and 'B'
res1 = [x*3 for x in gen_AB()]

#This for loop is iterating over the res1 list produced by the list comprehension
for i in res1:
    print('-->', i)

print('res1: ', res1)

# The generator expression returns res2. The call to gen_AB() is made, but that call returns a generator, which is not consumed here.
#  res2 is a generator object
res2 = (x*3 for x in gen_AB())

res2 = (x*3 for x in gen_AB())
for i in res2:
    print('-->', i)
print('res2: ', res2)

