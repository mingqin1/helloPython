from functools import wraps
"""decorator for priming coroutine
"""
def coroutine(func):
    """Decorator: primes `func` by advancing to first `yield`"""
    @wraps(func)
    #  The decorated generator function is replaced by this primer function which, when invoked, returns the primed generator.
    def primer(*args, **kwargs):
        # Call the decorated function to get a generator object.
        gen = func(*args, **kwargs)
        # Prime the generator.
        next(gen)
        # Return it.
        return gen
    return primer
