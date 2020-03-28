import time


def clock(func):
    """Define inner function clocked to accept any number of positional arguments.
    """
    def clocked(*args):
        t0 = time.perf_counter()

        """This line only works because the closure for clocked encompasses the func free variable.
        """
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        """Return the inner function to replace the decorated function.
        """
        return result
    return clocked
