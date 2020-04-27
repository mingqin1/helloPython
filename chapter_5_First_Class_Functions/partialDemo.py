from operator import mul
from functools import partial
from keywordOnlyArguments import tag
import unicodedata
import functools

"""
 Given a function, a partial application produces a new callable with some of the arguments of the original function fixed.
 This is useful to adapt a function that takes one or more arguments to an API that requires a callback with fewer arguments.
"""


triple = partial(mul, 3)
triple(7)

list(map(triple, range(1, 10)))
print('list(map(triple, range(1, 10))): ', list(map(triple, range(1, 10))))

nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
s1, s2
print('s1, s2: ', s1, s2)

s1 == s2
print('s1 == s2: ', s1 == s2)

nfc(s1) == nfc(s2)
print('nfc(s1) == nfc(s2): ', nfc(s1) == nfc(s2))

picture = partial(tag, 'img', cls='pic-frame')
print('picture: ', picture)

picture.args
print('picture.args: ', picture.args)

picture.keywords
print('picture.keywords: ', picture.keywords)
