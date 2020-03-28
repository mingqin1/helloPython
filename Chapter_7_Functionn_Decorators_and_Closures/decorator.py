
"""deco returns its inner function object.

Returns:
    [type] -- [description]
"""


def deco(func):
    def inner():
        print('running inner()')
    return inner


"""
target is decorated by deco.
"""
@deco
def target():
    print('running target()')


"""
Invoking the decorated target actually runs inner
"""
target()

"""
Inspection reveals that target is a now a reference to inner.
"""
print(target)
