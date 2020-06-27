# The advantage of using a coroutine is that total and count can be simple local variables:
#  no instance attributes or closures are needed to keep the context between calls.

def averager():
    total = 0.0
    count = 0
    average = None
    # This infinite loop means this coroutine will keep on accepting values and producing results as long as the caller sends them.
    # This coroutine will only terminate when the caller calls .close() on it,
    # or when it’s garbage collected because there are no more references to it.
    while True:
        # The yield statement here is used to suspend the coroutine, produce a result to the caller,
        # and—later—to get a value sent by the caller to the coroutine, which resumes its infinite loop.
        term = yield average
        total += term
        count += 1
        average = total / count

# Create the coroutine object.
coro_avg = averager()

#  Prime it by calling next.
next(coro_avg)

#  Now we are in business: each call to .send(…) yields the current average.
print('coro_avg.send(10): ', coro_avg.send(10))

print('coro_avg.send(30): ', coro_avg.send(30))

print('coro_avg.send(5): ', coro_avg.send(5))
