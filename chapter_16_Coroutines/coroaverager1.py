# Import the coroutine decorator.
from coroutil import coroutine
from inspect import getgeneratorstate

"""a running average coroutine using the @coroutine decorator from coroutil.py
"""

#  Apply it to the averager function.
@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

# Call averager(), creating a generator object that is primed inside the primer function of the coroutine decorator.
coro_avg = averager()

# getgeneratorstate reports GEN_SUSPENDED, meaning that the coroutine is ready to receive a value.
print('getgeneratorstate(coro_avg): ', getgeneratorstate(coro_avg))

# You can immediately start sending values to coro_avg: that’s the point of the decorator.
print('coro_avg.send(10): ', coro_avg.send(10))

print('coro_avg.send(30): ', coro_avg.send(30))
